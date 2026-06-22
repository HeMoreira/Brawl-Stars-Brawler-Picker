"""
COMO USAR:

Execute a função `import_excel_to_db` passando o caminho do arquivo Excel como argumento no terminal Python do projeto.

Exemplo:
python manage.py shell
from brawler.utils import import_excel_to_db
import_excel_to_db('brawler_picker_v0.xlsx')

Se a execução falhar, verifique as mensagens de erro e os corrija.
Erros comuns:
- Remoção/Alteração acidental do "-" ao final de uma coluna de nome (ponto de parada na lógica da busca por brawlers classificados)
- Alteração acidental do nome de uma propriedade de Proficiency (Comumente, a automação será cancelada, apontando o nome da coluna não encontrada)
"""

import pandas as pd
from .models import Brawler
from proficiency.models import Proficiency
from additional_power.models import Gadget, StarPower, Hipercharge
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db import models as dj_models


def import_excel_to_db(file_path):
    """
    Importa dados de múltiplas abas de um arquivo Excel para os modelos Django.
    Orquestra a validação, coleta e persistência de dados.
    
    Abas esperadas:
    - BRAWLERS OFICIAL -> Brawler.base_proficiency
    - PRIMEIRO ACESSÓRIO -> Brawler.first_gadget
    - SEGUNDO ACESSÓRIO -> Brawler.second_gadget
    - PRIMEIRO PODER-DE-ESTRELA -> Brawler.first_starpower
    - SEGUNDO PODER-DE-ESTRELA -> Brawler.second_starpower
    - HIPERCARGA -> Brawler.hipercharge
    
    Levanta ValueError se houver qualquer erro de validação.
    """
    all_sheets = pd.read_excel(file_path, sheet_name=None, skiprows=1)
    proficiency_fields = _get_proficiency_fields()
    
    parsed_sheets, summary = validate_all_sheets(all_sheets, proficiency_fields)
    persist_parsed_data(parsed_sheets, summary)
    
    print("Importação concluída. Resumo:")
    for k, v in summary.items():
        print(f"- {k}: {v} linhas processadas")


def validate_all_sheets(all_sheets, proficiency_fields):
    """
    Valida todas as abas do Excel e coleta dados estruturados.
    
    Retorna (parsed_sheets, summary) onde:
    - parsed_sheets: {sheet_name: [row_dict, ...]}
    - summary: {sheet_name: count}
    
    Levanta ValueError se houver erros de validação.
    """
    sheets_of_interest = [
        'BRAWLERS OFICIAL',
        'PRIMEIRO ACESSÓRIO',
        'SEGUNDO ACESSÓRIO',
        'PRIMEIRO PODER-DE-ESTRELA',
        'SEGUNDO PODER-DE-ESTRELA',
        'HIPERCARGA',
    ]
    
    summary = {k: 0 for k in sheets_of_interest}
    all_errors = []
    parsed_sheets = {}
    
    for sheet in sheets_of_interest:
        df = all_sheets.get(sheet)
        if df is None:
            print(f"Aba '{sheet}' não encontrada no arquivo. Pulando.")
            continue
        
        # Remove a primeira coluna da aba (vazia em todas as planilhas)
        df = df.iloc[:, 1:].dropna(how='all')
        
        if df.empty:
            print(f"Aba '{sheet}' está vazia. Pulando.")
            continue
        
        sheet_rows, errors = process_single_sheet(sheet, df, proficiency_fields)
        all_errors.extend(errors)
        parsed_sheets[sheet] = sheet_rows
    
    # Se houver qualquer erro, levanta um ValueError com detalhes e não toca no banco.
    if all_errors:
        raise ValueError(
            f"\n{'='*60}\n"
            f"IMPORT ABORTED — {len(all_errors)} problem(s) found.\n"
            f"No data was saved. Fix the Excel file and try again.\n"
            f"{'='*60}\n"
            + "\n".join(all_errors)
            + f"\n{'='*60}"
        )
    
    return parsed_sheets, summary


def process_single_sheet(sheet, df, proficiency_fields):
    """
    Processa uma aba do Excel e coleta os dados das linhas.
    
    Retorna (sheet_rows, errors) onde:
    - sheet_rows: lista de dicts com {brawler_name, proficiency_values, additional_power_name}
    - errors: lista de mensagens de erro encontradas
    """
    sheet_rows = []
    errors = []
    
    # Define quais colunas são necessárias para este sheet
    required_fields = ['name'] + [f.name for f in proficiency_fields if f.name != 'id']
    if sheet != 'BRAWLERS OFICIAL':
        required_fields.append('additional_power_name')
    
    # Valida existência de todas as colunas necessárias
    col_by_field = _validate_and_collect_all_columns(df, required_fields, sheet)
    if isinstance(col_by_field, tuple):
        # Houve erro na validação de colunas
        _, col_errors = col_by_field
        errors.extend(col_errors)
        return sheet_rows, errors
    
    for _, row in df.iterrows():
        brawler_name = row.get(col_by_field['name'])
        # Se encontrar "-" na coluna de nome, considera que é o fim dos dados relevantes para esta planilha e quebra o loop.
        if pd.isna(brawler_name) or str(brawler_name).strip() in ('', '-'):
            break
        brawler_name = str(brawler_name).strip()
        
        # Coleta e valida valores de Proficiency para esta linha
        prof_values, row_errors = _collect_proficiency_values(
            row, proficiency_fields, col_by_field, sheet, brawler_name
        )
        errors.extend(row_errors)
        
        additional_power_name = None
        if sheet != 'BRAWLERS OFICIAL':
            # Coleta o nome da power se presente e válido
            if not pd.isna(row.get(col_by_field.get('additional_power_name'))) and str(row.get(col_by_field.get('additional_power_name'))).strip() != '':
                additional_power_name = str(row.get(col_by_field.get('additional_power_name'))).strip()
            else:
                errors.append(
                    f"  [Aba '{sheet}' | Brawler '{brawler_name}'] Campo 'additional_power_name' está vazio ou inválido nesta linha."
                )
        
        sheet_rows.append({
            'brawler_name': brawler_name,
            'proficiency_values': prof_values,
            'additional_power_name': additional_power_name,
        })
    
    return sheet_rows, errors


def persist_parsed_data(parsed_sheets, summary):
    """
    Persiste os dados validados no banco de dados dentro de uma transação atômica.
    
    Atualiza o dicionário summary com a contagem de linhas processadas.
    """
    sheets_of_interest = [
        'BRAWLERS OFICIAL',
        'PRIMEIRO ACESSÓRIO',
        'SEGUNDO ACESSÓRIO',
        'PRIMEIRO PODER-DE-ESTRELA',
        'SEGUNDO PODER-DE-ESTRELA',
        'HIPERCARGA',
    ]
    
    with transaction.atomic():
        for sheet in sheets_of_interest:
            sheet_rows = parsed_sheets.get(sheet)
            if not sheet_rows:
                continue
            
            for row_data in sheet_rows:
                brawler_name = row_data['brawler_name']
                prof_values = row_data['proficiency_values']
                additional_name = row_data['additional_power_name']
                icon_name = f"{brawler_name.lower().replace(' ', '')}_icon.png"
                
                if sheet == 'BRAWLERS OFICIAL':
                    _upsert_brawler_base(brawler_name, prof_values, icon_name)
                    summary[sheet] += 1
                    continue
                
                ModelClass, target_attr = _resolve_sheet_type(sheet)
                if ModelClass is None:
                    print(f"Tipo da aba '{sheet}' não reconhecido. Pulando linha para '{brawler_name}'.")
                    continue
                
                brawler = Brawler.objects.filter(name__iexact=brawler_name).first()
                _upsert_additional_power(
                    brawler, target_attr, additional_name, prof_values
                )
                summary[sheet] += 1


def _strip_header(s):
    return str(s).strip()

def _find_column(columns, exact_name):
    # Busca por correspondência exata (após strip) com um nome específico.
    # Se não encontrar, retorna None e a execução será abortada na validação.
    for col in columns:
        if _strip_header(col) == exact_name:
            return col
    return None

def _get_proficiency_fields():
    # Retorna todos os campos concretos (não automáticos) do modelo Proficiency.
    return [
        f for f in Proficiency._meta.get_fields()
        if getattr(f, 'concrete', False) and not getattr(f, 'auto_created', False)
    ]

def _cast_proficiency_value(field_obj, raw_value):
    # Para campos de `Proficiency`, multiplica por 10, arredonda e converte para int.
    # Retorna `None` se o valor estiver ausente ou inválido.
    if pd.isna(raw_value):
        return None
    if isinstance(field_obj, (dj_models.IntegerField, dj_models.SmallIntegerField)):
        try:
            return int(round(float(raw_value) * 10))
        except (TypeError, ValueError):
            return None
    return raw_value

def _validate_and_collect_all_columns(df, required_field_names, sheet, brawler_name=None):
    # Valida que todas as colunas necessárias existem no DataFrame.
    # Retorna um dicionário {field_name: column_name} se todas forem encontradas.
    # Caso contrário, retorna (None, error_list).
    col_by_field = {}
    errors = []
    
    for field_name in required_field_names:
        col = _find_column(df.columns, field_name)
        if col is None:
            ctx = f" | Brawler '{brawler_name}'" if brawler_name else ""
            errors.append(
                f"  [Aba '{sheet}'{ctx}] Coluna '{field_name}' não encontrada. "
                f"Colunas presentes: {list(df.columns)}"
            )
        else:
            col_by_field[field_name] = col
    
    return col_by_field if not errors else (None, errors)

def _collect_proficiency_values(row, proficiency_fields, col_by_field, sheet, brawler_name):
    # Coleta e valida valores de Proficiency para uma linha específica.
    # Retorna (values_dict, errors_list).
    errors, values = [], {}
    for f in proficiency_fields:
        if f.name == 'id':
            continue
        col = col_by_field.get(f.name)
        if col is None:
            # Coluna não foi encontrada na validação anterior, pula
            continue
        val = _cast_proficiency_value(f, row.get(col))
        if val is None:
            errors.append(
                f"  [Aba '{sheet}' | Brawler '{brawler_name}'] Campo '{f.name}' está vazio ou inválido nesta linha."
            )
        else:
            values[f.name] = val
    return values, errors

_SHEET_TARGET = {
    'ACESS': (Gadget,      'first_gadget',    'second_gadget'),
    'PODER': (StarPower,   'first_starpower', 'second_starpower'),
    'HIPER': (Hipercharge, 'hipercharge',     'hipercharge'),
}

def _resolve_sheet_type(sheet):
    for key, (model, first_attr, second_attr) in _SHEET_TARGET.items():
        if key in sheet:
            return model, (first_attr if 'PRIMEIRO' in sheet else second_attr)
    return None, None

def _apply_proficiency_values(prof, values):
    for k, v in values.items():
        setattr(prof, k, v)
    prof.save()

def _upsert_brawler_base(brawler_name, prof_values, icon_name):
    brawler = Brawler.objects.filter(name__iexact=brawler_name).first()
    if brawler:
        if brawler.base_proficiency is None:
            brawler.base_proficiency = Proficiency.objects.create(**prof_values)
        else:
            _apply_proficiency_values(brawler.base_proficiency, prof_values)
        if not brawler.icon_name:
            brawler.icon_name = icon_name
        brawler.save()
    else:
        base_prof = Proficiency.objects.create(**prof_values)
        first_g_prof = Gadget.objects.create(additional_power_name="Placeholder Gadget", icon_name="placeholdergadget_icon.png", base_proficiency=Proficiency.objects.create(**prof_values))
        second_g_prof = Gadget.objects.create(additional_power_name="Placeholder Gadget", icon_name="placeholdergadget_icon.png", base_proficiency=Proficiency.objects.create(**prof_values))
        first_s_prof = StarPower.objects.create(additional_power_name="Placeholder StarPower", icon_name="placeholderstarpower_icon.png", base_proficiency=Proficiency.objects.create(**prof_values))
        second_s_prof = StarPower.objects.create(additional_power_name="Placeholder StarPower", icon_name="placeholderstarpower_icon.png", base_proficiency=Proficiency.objects.create(**prof_values))
        hip_prof = Hipercharge.objects.create(additional_power_name="Placeholder Hipercharge", icon_name="placeholderhipercharge_icon.png", base_proficiency=Proficiency.objects.create(**prof_values))
        brawler = Brawler.objects.create(
            name=brawler_name.title(),
            icon_name=icon_name,
            primary_class='AT',
            secondary_class='M',
            base_proficiency=base_prof,
            first_gadget=first_g_prof,
            second_gadget=second_g_prof,
            first_starpower=first_s_prof,
            second_starpower=second_s_prof,
            hipercharge=hip_prof,
        )
    return brawler

def _get_related_object(instance, attr_name):
    try:
        return getattr(instance, attr_name)
    except ObjectDoesNotExist:
        return None

def _upsert_additional_power(brawler, target_attr, additional_name, prof_values):
    power_icon_name = f"{additional_name.lower().replace(' ', '')}_icon.png"
    power_obj = _get_related_object(brawler, target_attr) if brawler else None

    # Poder já existe: atualizar a Proficiency associada e metadados
    if power_obj.base_proficiency is None:
        power_obj.base_proficiency = Proficiency.objects.create(**prof_values)
    else:
        _apply_proficiency_values(power_obj.base_proficiency, prof_values)
    power_obj.additional_power_name = additional_name.title()
    power_obj.icon_name = power_icon_name
    power_obj.save()
 
    setattr(brawler, target_attr, power_obj)
    brawler.save()
    return brawler
