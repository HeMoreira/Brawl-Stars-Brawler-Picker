from django.db import models

# Create your models here.
class Proficiency(models.Model):
    proficiency_id = models.IntegerField(primary_key=True)

    # Ataques: Dano e resistência
    durability = models.SmallIntegerField(verbose_name="Durability", help_text="capacidade de resistir a muitos ataques")
    counter_durability = models.SmallIntegerField(verbose_name="Counter Durability", help_text="capacidade de causar problemas para brawlers resistentes")
    attack_distance = models.SmallIntegerField(verbose_name="Attack-Distance", help_text="capacidade de causar danos em um alcance longo")
    counter_attack_distance = models.SmallIntegerField(verbose_name="capacidade de evitar danos a um longo alcance")
    surprise_attack = models.SmallIntegerField(verbose_name="Surprise-Attack", help_text="capacidade de rushar em inimigos rapidamente")
    counter_surprise_attack = models.SmallIntegerField(verbose_name="Counter Surprise-Attack", help_text="capacidade de impedir Rushs de Assasinos")
    burst_damage = models.SmallIntegerField(verbose_name="Burst-Damage", help_text="capacidade de aplicar descargas de dano massivo")
    counter_burst_damage = models.SmallIntegerField(verbose_name="Counter Burst-Damage", help_text="capacidade de resistir a descargas de dano massivo")
    objects_burst_attack = models.SmallIntegerField(verbose_name="Objects-Burst-Damage", help_text="capacidade de aplicar descargas de dano massivo em objetos que não se movem")
    counter_objects_burst_damage = models.SmallIntegerField(verbose_name="Counter Objects-Burst-Damage", help_text="Capacidade de resistir a descargas de dano massivo em objetos que não se movem")
    indirect_damage = models.SmallIntegerField(verbose_name="Indirect-Damage", help_text="capacidade de causar dano através de muros ou covers")
    counter_indirect_damage = models.SmallIntegerField(verbose_name="Counter Indirect-Damage", help_text="capacidade de evitar danos por detrás de muros e covers")
    area_denial = models.SmallIntegerField(verbose_name="Area-Denial", help_text="capacidade de impedir a passagem de inimigos por espaços")
    counter_area_denial = models.SmallIntegerField(verbose_name="Counter Area-Denial", help_text="capacidade de ignorar o impedimento de passagem por espaços")
    multiple_enemies = models.SmallIntegerField(verbose_name="Multiple-Enemies", help_text="capacidade de fazer pressão com o spawn de mais inimigos")
    counter_multiple_enemies = models.SmallIntegerField(verbose_name="Counter Multiple-Enemies", help_text="capacidade de lidar com a pressão de múltiplos inimigos em cena")
    turret_power = models.SmallIntegerField(verbose_name="Turret-Control", help_text="capacidade de gerar torretas que incomodam inimigos e são dificilmente destruíveis")
    counter_turret_power = models.SmallIntegerField(verbose_name="Counter Turret-Power", help_text="capacidade de destruir torretas que incomodam dos inimigos")
    wide_attack = models.SmallIntegerField(verbose_name="Wide-Attack", help_text="capacidade de atingir grandes áreas com seus ataques")
    counter_wide_attack = models.SmallIntegerField(verbose_name="Counter Wide-Attack", help_text="capacidade de enfrentar brawlers com áreas de ataque grandes")

    # Controle direto: Muros e Pressão
    lane_pressure = models.SmallIntegerField(verbose_name="Lane-Pressure", help_text="capacidade de manter inimigos recuados")
    counter_lane_pressure = models.SmallIntegerField(verbose_name="Counter Lane-Pressure", help_text="capacidade de se aproximar perante pressão inimiga")
    wall_break_efficiency = models.SmallIntegerField(verbose_name="Wall-Break-Efficiency", help_text="capacidade de destruição de muros")
    counter_wall_break_efficiency = models.SmallIntegerField(verbose_name="Counter Wall-Break-Efficiency", help_text="capacidade de evitar problemas mesmo em mapas sem muros")
    grass_break_efficiency = models.SmallIntegerField(verbose_name="Grass-Break-Efficiency", help_text="capacidade de destruição de moitas")
    counter_grass_break_efficiency = models.SmallIntegerField(verbose_name="Counter Grass-Break-Efficiency", help_text="capacidade de evitar problemas mesmo em mapas sem moitas")
    enemy_position_manipulation = models.SmallIntegerField(verbose_name="Enemy-Position-Manipulation", help_text="capacidade de manipular a posição de inimigos com puxões ou empurrões")
    counter_enemy_position_manipulation = models.SmallIntegerField(verbose_name="Counter Enemy-Position-Manipulation", help_text="capacidade de evitar problemas relacionados a puxões e empurrões de inimigos")

    # Buffs: Suporte e seus counters
    heal_buffing = models.SmallIntegerField(verbose_name="Heal-Buffing", help_text="capacidade de regenerar a vida de aliados")
    counter_heal_buffing = models.SmallIntegerField(verbose_name="Counter Heal-Buffing", help_text="capacidade de reduzir eficácia de regeneração de vida")
    poison_debuffing = models.SmallIntegerField(verbose_name="Poison-Debuffing", help_text="capacidade de aplicação de dano contínuo")
    counter_poison_debuffing = models.SmallIntegerField(verbose_name="Counter Poison-Debuffing", help_text="capacidade de reduzir eficácia de dano contínuo")
    stun_debuffing = models.SmallIntegerField(verbose_name="Stun-Debuffing", help_text="capacidade de aplicação de stun (paralisia)")
    counter_stun_debuffing = models.SmallIntegerField(verbose_name="Counter Stun-Debuffing", help_text="capacidade de reduzir eficácia de stun (paralisia)")
    slowness_debuffing = models.SmallIntegerField(verbose_name="Slowness-Debuffing", help_text="capacidade de aplicação de lentidão")
    counter_slowness_debuffing = models.SmallIntegerField(verbose_name="Counter Slowness-Debuffing", help_text="capacidade de reduzir eficácia de lentidão")
    block_attacks_debuffing = models.SmallIntegerField(verbose_name="Block-Attacks-Debuffing", help_text="capacidade de anular ataques inimigos")
    counter_block_attacks_debuffing = models.SmallIntegerField(verbose_name="Counter Block-Attacks-Debuffing", help_text="capacidade de reduzir eficácia de anulação de ataques")
    delayed_attack = models.SmallIntegerField(verbose_name="Delayed-Attack", help_text="capacidade de dar um tempo antes de atacar, comum em ataques fortes")
    counter_delayed_attack = models.SmallIntegerField(verbose_name="Counter Delayed-Attack", help_text="capacidade de cancelar ataques que demoram para acontecer")