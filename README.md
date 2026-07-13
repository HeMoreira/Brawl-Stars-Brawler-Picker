# Brawler Picker - BrawlStars

Análise de Matches da Ranked de Brawl Stars. Compare brawlers aliados e inimigos para formar as melhores equipes em tempo real!
> Projeto feito por fãs sem qualquer ligação com a equipe do jogo Brawl Stars da empresa Supercell.

## Funcionalidades mais marcantes

- Montagem rápida de equipes para Ranked, com foco em comparação entre brawlers aliados e inimigos.
- Análise profunda com base nas estatísticas de cada brawler, gadget, starpower e hipercharge.
- Cadastro detalhado de gadgets, Star Powers e Hipercharges para cada brawler.
- Painel administrativo para gerenciar brawlers, mapas, proficiências e poderes adicionais.
<!-- - Organização de builds mais comuns, facilitando a tomada de decisão durante o jogo. -->
<!-- - Suporte a diferentes mapas e modos, considerando multiplicadores específicos de cenário. -->

## Configuração

### 1. Acesse a subpasta principal
```bash
cd Brawl-Stars-Brawler-Picker
```
> Lembre-se de definir um ambiente virtual caso queira

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente
```bash
# Crie um arquivo .env e defina SECRET_KEY, DEBUG, ALLOWED_HOSTS e DATABASE_URL.
```
> Exemplo:
> ```bash
> SECRET_KEY=sua_chave_secreta
> DEBUG=True
> ALLOWED_HOSTS=127.0.0.1,localhost
> DATABASE_URL=sqlite:///db.sqlite3
> ```

### 4. Aplicar migrations
```bash
python manage.py migrate
```

### 5. Popular Banco de dados (opcional)
```bash
python manage.py loaddata dump.json
```
> Esse comando popula o banco de dados com dados definidos de cada brawler pelos criadores do projeto. Caso opte por pular essa etapa, precisará definir os objetos manualmente.

### 6. Criar superusuário (administrador)
```bash
python manage.py createsuperuser
```
> Contas de admin só podem ser criadas via terminal.

### 7. Rodar o servidor
```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000 ou https://localhost:8000

---

## Estrutura de apps

| App | Responsabilidade |
|-----|-----------------|
| `core`            | Funções de utilidade para testes |
| `main`            | Processamento completo da lógica das páginas |
| `proficiency`     | Gerenciamento de Proficiências, a base dos demais modelos desse projeto |
| `map`             | Gerenciamento de Mapas com seus modos |
| `additional_power`| Gerenciamento de complementos do Brawler (gadget, starpower, hipercharge) |
| `brawler`         | Gerenciamento de Brawlers, objeto principal de análise |

## Segurança

- Credenciais em variáveis de ambiente via `.env` (nunca no código)
- CSRF token em todos os formulários
<!-- - Todas as rotas protegidas por `@login_required` -->
<!-- - Validação de propriedade `obj.user == request.user` em toda operação (proteção IDOR) -->
<!-- - Escape automático de HTML pelo template engine do Django (proteção XSS) -->
<!-- - Acesso ao banco exclusivamente via Django ORM (proteção SQL Injection) -->