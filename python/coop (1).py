import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    time.sleep(3)

clear()
print("------------------------------------")
# estatisticas do jogador 1
p1hp = 100
p1maxHP = 100
if p1hp > p1maxHP:
    p1hp = p1maxHP
p1sp = 30
if p1sp > 30:
    p1sp = 30
p1atk = 0
p1atkBonus = 0
p1defBonus = 0
p1slashBonus = 0
speedTurns = 0
p1 = str(input("Nome do 1º jogador: "))
def p1stats():
    print("------------------------------------")
    print(f"HP do {p1}: {p1hp}/{p1maxHP}")
    print(f"SP do {p1}: {p1sp}/30")
    print(f"HP do inimigo: {enemyhp}/{enemyMaxHP}")
p1fireTurns = 0
p1Ult = 0
if p1Ult > 100:
    p1Ult = 100
skipP1 = False
p1block = False
p1MotivateATK = False
p1MotivateDEF = False
p1Defend = False
charge = False
lifeSteal = False
ult = False
abilityCharge = False
speed = False
invAccess = False
inventory = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
damageDealt = 0
damageTaken = 0
totalUpgrades = 0
p1Damage = 0

# estatisticas do jogador 2
p2hp = 80
if p2hp > 80:
    p2hp = 80
p2sp = 60
p2MaxSP = 60
if p2sp > p2MaxSP:
    p2sp = p2MaxSP
p2atk = 0
heal = 18
p2magBonus = 0
p2defBonus = 0
p2fireTurns = 0
p2ultCharge = 0
rabbitTurn = 0
p2Damage = 0
if p2ultCharge > 100:
    p2ultCharge = 100
p2 = str(input("Nome do 2º jogador: "))
def p2stats():
    print("------------------------------------")
    print(f"HP do {p2}: {p2hp}/80")
    print(f"SP do {p2}: {p2sp}/{p2MaxSP}")
    print(f"HP do inimigo: {enemyhp}/{enemyMaxHP}")
skipP2 = False
p2MotivateATK = False
p2MotivateDEF = False
p2Defend = False
p2Parry = False
p2Summon = False
p2Ult = False
parryActive = False
wolfActive = False
rabbitActive = False

# estatisticas do inimigo
enemyhp = 425
enemyMaxHP = 425
if enemyhp > enemyMaxHP:
    enemyhp = enemyMaxHP
turns = 0
skipEnemy = False
p1target = 0
p2target = 0
enemyfireTurns = 0
distressTurns = 0
playerChoice = 0
wolfTurns = 0
atkDebuffTurns = 0
defDebuffTurns = 0
atkDebuff = False
defDebuff = False
ragedEnemy = False

# abilities
p1onFire = False
p2onFire = False
enemyOnFire = False
enemyDistress = False

def p1Burn():
    global p1fireTurns, p1hp, p1onFire, damageTaken
    if not p1onFire:
        return
    p1fireTurns += 1
    if p1fireTurns <= 3:
        print(f"{p1} está queimando! -10HP")
        print("-------------------------------------------------------------")
        p1hp -= 10
        damageTaken += 10
        if p1hp < 0:
            p1hp = 0
        wait()
        clear()
    else:
        p1onFire = False
        p1fireTurns = 0
        print(f"O fogo de {p1} se passou...")
        wait()
        clear()

def p2Burn():
    global p2fireTurns, p2hp, p2onFire, damageTaken
    if not p2onFire:
        return
    p2fireTurns += 1
    if p2fireTurns <= 3:
        print(f"{p2} está queimando! -10HP")
        print("-------------------------------------------------------------")
        p2hp -= 10
        damageTaken += 10
        if p2hp < 0:
            p2hp = 0
        wait()
        clear()
    else:
        p2onFire = False
        p2fireTurns = 0
        print(f"O fogo de {p2} se passou...")
        wait()
        clear()

def p2Casts():
    global p2, p2sp, rabbitActive, wolfActive, wolfTurns, rabbitTurn
    while True:
        print(f"------------------------{p2} - Animais--------------------------")
        print("[1] Lobo - Ataca o inimigo continuosamente por 3 turnos. (20 SP)")
        print("[2] Coelho - Cura os aliados passivamente por 3 turnos. (20 SP)")
        print("[3] Voltar")
        castChoice = [1, 2, 3]
        try:
            animal = int(input("Qual sumonar? [1/2]: "))
        except ValueError:
            animal = 0
        while animal not in castChoice:
            try:
                animal = int(input("Escolha válido [1/2]: "))
            except ValueError:
                animal = 0
        if animal == 1:
            if p2sp < 20:
                print("SP insuficiente.")
                wait()
                clear()
                continue
            if rabbitActive == True or wolfActive == True:
                print("Um animal já está ativo!")
                print("-------------------------------------------------------------")
                wait()
                clear()
                return False
            else:
                wolfActive = True
                wolfTurns = 0
                p2sp -= 20
                if p2sp < 0:
                    p2sp = 0
                print("Sumonou o lobo!")
                print("-------------------------------------------------------------")
                wait()
                clear()
                return True
        elif animal == 2:
            if p2sp < 20:
                print("SP insuficiente.")
                wait()
                clear()
                continue
            if wolfActive == True or rabbitActive == True:
                print("Um animal já está ativo!")
                print("-------------------------------------------------------------")
                wait()
                clear()
                return False
            else:
                rabbitActive = True
                rabbitTurn = 0
                p2sp -= 20
                if p2sp < 0:
                    p2sp = 0
                print("Sumonou o coelho!")
                print("-------------------------------------------------------------")
                wait()
                clear()
                return True
        elif animal == 3:
            clear()
            return False

def burn():
    global enemyfireTurns, enemyhp, enemyOnFire, damageDealt, p1Damage
    if not enemyOnFire:
        return
    enemyfireTurns += 1
    if enemyfireTurns <= 3:
        print("O inimigo está queimando! -15HP")
        print("-------------------------------------------------------------")
        dano_burn = min(enemyhp, 15)
        enemyhp -= 15
        damageDealt += dano_burn
        p1Damage += dano_burn
        if enemyhp < 0:
            enemyhp = 0
        wait()
        clear()
    else:
        enemyOnFire = False
        enemyfireTurns = 0
        print("O fogo do inimigo se passou...")
        wait()
        clear()

def distress():
    global enemyDistress, distressTurns
    if not enemyDistress:
        return
    distressTurns += 1
    if distressTurns > 3:
        enemyDistress = False
        distressTurns = 0
        print("O distresse do inimigo passou...")
        print("-------------------------------------------------------------")
        wait()
        clear()

def pray():
    global p1, p1hp, p1maxHP, p2, p2hp, p2sp, heal
    if p2sp < 10:
        print("SP insuficiente.")
        wait()
        clear()
        return False
    while True:
        print(f"[1] {p1} ({p1hp}HP)")
        print(f"[2] {p2} ({p2hp}HP)")
        print("[3] Voltar")
        try:
            healChoice = int(input("Quem curar? [1/2]: "))
        except ValueError:
            healChoice = 0
        while healChoice not in [1, 2, 3]:
            try:
                healChoice = int(input("Escolha válida [1/2]: "))
            except ValueError:
                healChoice = 0
        if healChoice == 1:
            if p1hp <= 0:
                print(f"{p1} está morto! Não foi curado.")
                wait()
                clear()
                return False
            else:
                print(f"Curou {p1} com {heal + p2magBonus}HP!")
                wait()
                clear()
                p2sp -= 10
                if p2sp < 0:
                    p2sp = 0
                p1hp += (heal + p2magBonus)
                if p1hp > p1maxHP:
                    p1hp = p1maxHP
                return True
        elif healChoice == 2:
            if p2hp <= 0:
                print(f"{p2} está morto! Não foi curado.")
                wait()
                clear()
                return False
            else:
                print(f"Curou {p2} com {heal + p2magBonus}HP!")
                wait()
                clear()
                p2sp -= 10
                if p2sp < 0:
                    p2sp = 0
                p2hp += (heal + p2magBonus)
                if p2hp > 80:
                    p2hp = 80
                return True
        elif healChoice == 3:
            clear()
            return False

def block(dmg):
    global p1hp, p1, p1block, p1defBonus, p1Defend, damageTaken
    if p1block:
        p1absorb = dmg // 2
        dmg -= p1absorb
        p1absorbFinal = max(0, p1absorb - p1defBonus)
        if p1Defend:
            p1absorbFinal //= 2
        p1hp -= p1absorbFinal
        damageTaken += p1absorbFinal
        if p1hp < 0:
            p1hp = 0
        print(f"{p1} bloqueou e absorveu {p1absorbFinal} do dano!")
        p1block = False
    return dmg

def motivate():
    global p2sp, p1MotivateATK, p2MotivateATK, p1MotivateDEF, p2MotivateDEF, p1, p2, p1hp, p2hp
    if p2sp < 15:
        print("SP Insuficiente.")
        wait()
        clear()
        return False
    while True:
        print("-------------------------------------------------------------")
        print(f"[1] {p1}")
        print(f"[2] {p2}")
        print(f"[3] Voltar")
        try:
            mot = int(input("Motivar quem: "))
        except ValueError:
            mot = 0
        while mot not in [1, 2, 3]:
            try:
                mot = int(input("Escolha 1 ou 2: "))
            except ValueError:
                mot = 0
        if mot == 1:
            if p1hp <= 0:
                print(f"{p1} está morto! Não foi motivado.")
                wait()
                clear()
                return False
            p1MotivateATK = True
            p1MotivateDEF = True
            print(f"{p1} foi motivado! ATK+ e DEF+")
            wait()
            clear()
            p2sp -= 15
            if p2sp < 0:
                p2sp = 0
            return True
        elif mot == 2:
            if p2hp <= 0:
                print(f"{p2} está morto! Não foi motivado.")
                wait()
                clear()
                return False
            p2MotivateATK = True
            p2MotivateDEF = True
            print(f"{p2} foi motivado! ATK+ e DEF+")
            wait()
            clear()
            p2sp -= 15
            if p2sp < 0:
                p2sp = 0
            return True
        elif mot == 3:
            clear()
            return False

def isCharged():
    global p1sp, abilityCharge
    if p1sp < 12:
        print("SP insuficiente.")
        wait()
        clear()
        return False
    abilityCharge = True
    p1sp -= 12
    if p1sp < 0:
        p1sp = 0
    print("Carregou o próximo ataque físico!")
    print("-------------------------------------------------------------")
    wait()
    clear()
    return True

# ações                               
def p1menu():
    global p1hp, p1sp, p1atk, p1atkBonus, p2hp, p2sp, p2MaxSP, enemyhp, skipP1, skipP2, skipEnemy, p1MotivateATK, p1maxHP, abilityCharge, rabbitTurn, rabbitActive, defDebuff, defDebuffTurns, p1MotivateDEF, p2MotivateATK, p2MotivateDEF, ult, p1Ult, p2Ult, p2ultCharge, inventory, p1Defend, p1block, damageDealt, p1Damage
    if p1hp <= 0:
        return
    p1Defend = False
    p1block = False
    if p1hp > p1maxHP:
        p1hp = p1maxHP
    if skipP1:
        p1stats()
        print(f"{p1} não pode se mexer!")
        skipP1 = False
        wait()
        clear()
        return
    if rabbitActive and p1hp > 0:
        if rabbitTurn < 3:
            print(f"O coelho curou {p1} com 10 HP!")
            p1hp += 10
            if p1hp > p1maxHP:
                p1hp = p1maxHP
    while True:
        if p1hp <= 0 or enemyhp <= 0:
            return
        p1stats()
        print(f"------------------------{p1} - Ações--------------------------")
        print("[1] Atacar - Dano básico com baixa chance de crítico")
        print("[2] Habilidades - Menu de habilidades")
        print("[3] Defender - Restora SP e reduz dano tomado")
        actOption = [1, 2, 3]
        if invAccess == True:
            actOption.append(4)
            print("[4] Itens - Utiliza um item da mochila")
        if skipEnemy == True and p2hp > 0:
            actOption.append(5)
            print(f"[5] Trocar - Passa seu turno extra para {p2}")
        try:
            p1action = int(input("O que fazer: "))
        except ValueError:
            p1action = 0
        while p1action not in actOption:
            try:
                p1action = int(input("Escolha ação válida: "))
            except ValueError:
                p1action = 0
        if p1action == 1:
            p1dmg = random.randint(6, 24) + p1atk + p1atkBonus
            if abilityCharge:
                crit = random.randint(3, 6)
            else:
                crit = random.randint(1, 6)
            if p1MotivateATK == True or abilityCharge == True:
                p1dmg *= 2
                p1MotivateATK = False
                abilityCharge = False
            if defDebuff:
                p1dmg += 7
                defDebuffTurns += 1
                if defDebuffTurns >= 3:
                    defDebuff = False
                    defDebuffTurns = 0
            if crit == 6:
                p1dmg = int(p1dmg * 1.5)
                print(f"Crítico! {p1} atacou e deu {p1dmg} de dano! Derrubou o inimigo!")
                print("-------------------------------------------------------------")  
                skipEnemy = True
                dano_causado = min(enemyhp, p1dmg)
                damageDealt += dano_causado
                p1Damage += dano_causado
                enemyhp -= p1dmg
                if enemyhp < 0:
                    enemyhp = 0
                wait()
                clear()
                if enemyhp <= 0:
                    return
                print("-------------------------TURNO EXTRA!------------------------")
                continue
            else:
                print(f"{p1} atacou e deu {p1dmg} de dano!")
                print("-------------------------------------------------------------")
                dano_causado = min(enemyhp, p1dmg)
                damageDealt += dano_causado
                p1Damage += dano_causado
                enemyhp -= p1dmg
                if enemyhp < 0:
                    enemyhp = 0
                wait()
                clear()
                return
        elif p1action == 2:
            clear()
            res = p1abilities()
            if res == "extra":
                if enemyhp <= 0 or p1hp <= 0:
                    return
                print("-------------------------TURNO EXTRA!------------------------")
                continue
            elif res == True:
                return
        elif p1action == 3:
            p1sp += 10
            if p1sp > 30:
                p1sp = 30
            p1Defend = True
            print(f"{p1} defendeu e recuperou 10 SP!")
            print("-------------------------------------------------------------")
            wait()
            clear()
            return
        elif p1action == 4:
            clear()
            print(f"------------------------{p1} - Itens--------------------------")
            if 1 in inventory:
                print("[1] Poção de vida")
            if 2 in inventory:
                print("[2] Poção de vida")
            if 3 in inventory:
                print("[3] Poção de motivação")
            if 4 in inventory:
                print("[4] Menta da vida")
            if 5 in inventory:
                print("[5] Refrescador")
            if 6 in inventory:
                print("[6] Poção de energia")
            if 7 in inventory:
                print("[7] Poção de energia")
            if 8 in inventory:
                print("[8] Poção de motivação")
            if 9 in inventory:
                print("[9] Menta da vida")
            if 10 in inventory:
                print("[10] Proteína pura")
            print("[0] Voltar")
            try:
                item = int(input("Escolha um item: "))
            except ValueError:
                item = -1
            while item not in inventory:
                try:
                    item = int(input("Escolha um item válido: "))
                except ValueError:
                    item = -1
            if item == 0:
                clear()
                continue
            elif item == 1 or item == 2:
                print("Poção de vida - Cura 20 de HP")
                print(f"[1] {p1}")
                print(f"[2] {p2}")
                print("[0] Voltar")
                try:
                    playerItem = int(input("Em quem usar: "))
                except ValueError:
                    playerItem = -1
                while playerItem not in [1, 2, 0]:
                    try:
                        playerItem = int(input("Escolha um jogador: "))
                    except ValueError:
                        playerItem = -1
                if playerItem == 0:
                    clear()
                    continue
                elif playerItem == 1:
                    p1hp += 20
                    if p1hp > p1maxHP:
                        p1hp = p1maxHP
                    print(f"{p1} consumiu a Poção de vida!")
                    wait()
                    clear()
                    inventory.remove(item)
                    return
                elif playerItem == 2:
                    if p2hp <= 0:
                        print(f"{p2} está morto! Não foi curado.")
                        wait()
                        clear()
                        continue
                    else:
                        p2hp += 20
                        if p2hp > 80:
                            p2hp = 80
                        print(f"{p2} consumiu a Poção de vida!")
                        wait()
                        clear()
                        inventory.remove(item)
                        return
            elif item == 3 or item == 8:
                print("Poção de motivação - Motiva um jogador")
                print(f"[1] {p1}")
                print(f"[2] {p2}")
                print("[0] Voltar")
                try:
                    playerItem = int(input("Em quem usar: "))
                except ValueError:
                    playerItem = -1
                while playerItem not in [1, 2, 0]:
                    try:
                        playerItem = int(input("Escolha um jogador: "))
                    except ValueError:
                        playerItem = -1
                if playerItem == 0:
                    clear()
                    continue
                elif playerItem == 1:
                    p1MotivateATK = True
                    p1MotivateDEF = True
                    print(f"{p1} consumiu a Poção de motivação!")
                    wait()
                    clear()
                    inventory.remove(item)
                    return
                elif playerItem == 2:
                    if p2hp <= 0:
                        print(f"{p2} está morto! Não foi motivado.")
                        wait()
                        clear()
                        continue
                    else:
                        p2MotivateATK = True
                        p2MotivateDEF = True
                        print(f"{p2} consumiu a Poção de motivação!")
                        wait()
                        clear()
                        inventory.remove(item)
                        return
            elif item == 4 or item == 9:
                print(f"Menta da vida - Revive {p2}")
                if p2hp > 0:
                    print(f"{p2} já está vivo!")
                    wait()
                    clear()
                    continue
                else:
                    p2hp = 40
                    print(f"{p2} foi revivido pela Menta da vida!")
                    wait()
                    clear()
                    inventory.remove(item)
                    return
            elif item == 5:
                print("Refrescador - Restaura o HP e SP ao máximo")
                print(f"[1] {p1}")
                print(f"[2] {p2}")
                print("[0] Voltar")
                try:
                    playerItem = int(input("Em quem usar: "))
                except ValueError:
                    playerItem = -1
                while playerItem not in [1, 2, 0]:
                    try:
                        playerItem = int(input("Escolha um jogador: "))
                    except ValueError:
                        playerItem = -1
                if playerItem == 0:
                    clear()
                    continue
                elif playerItem == 1:
                    p1hp = p1maxHP
                    p1sp = 30
                    print(f"{p1} consumiu o Refrescador!")
                    wait()
                    clear()
                    inventory.remove(5)
                    return
                elif playerItem == 2:
                    if p2hp <= 0:
                        print(f"{p2} está morto! Não foi restaurado.")
                        wait()
                        clear()
                        continue
                    else:
                        p2hp = 80
                        p2sp = p2MaxSP
                        print(f"{p2} consumiu o Refrescador!")
                        wait()
                        clear()
                        inventory.remove(5)
                        return
            elif item == 6 or item == 7:
                print("Poção de energia - Recupera 20 de SP")
                print(f"[1] {p1}")
                print(f"[2] {p2}")
                print("[0] Voltar")
                try:
                    playerItem = int(input("Em quem usar: "))
                except ValueError:
                    playerItem = -1
                while playerItem not in [1, 2, 0]:
                    try:
                        playerItem = int(input("Escolha um jogador: "))
                    except ValueError:
                        playerItem = -1
                if playerItem == 0:
                    clear()
                    continue
                elif playerItem == 1:
                    p1sp += 20
                    if p1sp > 30:
                        p1sp = 30
                    print(f"{p1} consumiu a Poção de energia!")
                    wait()
                    clear()
                    inventory.remove(item)
                    return
                elif playerItem == 2:
                    if p2hp <= 0:
                        print(f"{p2} está morto! Não recuperou SP.")
                        wait()
                        clear()
                        continue
                    else:
                        p2sp += 20
                        if p2sp > p2MaxSP:
                            p2sp = p2MaxSP
                        print(f"{p2} consumiu a Poção de energia!")
                        wait()
                        clear()
                        inventory.remove(item)
                        return
            elif item == 10:
                print("Proteína pura - Aumenta a carga do ult para 100%")
                print(f"[1] {p1}")
                print(f"[2] {p2}")
                print("[0] Voltar")
                try:
                    playerItem = int(input("Em quem usar: "))
                except ValueError:
                    playerItem = -1
                while playerItem not in [1, 2, 0]:
                    try:
                        playerItem = int(input("Escolha um jogador: "))
                    except ValueError:
                        playerItem = -1
                if playerItem == 0:
                    clear()
                    continue
                elif playerItem == 1:
                    if ult == False:
                        print(f"{p1} não tem o ult desbloqueado!")
                        wait()
                        clear()
                        continue
                    else:
                        p1Ult = 100
                        print(f"{p1} consumiu a Proteína pura! Ult em 100%!")
                        wait()
                        clear()
                        inventory.remove(10)
                        return
                elif playerItem == 2:
                    if p2hp <= 0:
                        print(f"{p2} está morto!")
                        wait()
                        clear()
                        continue
                    elif p2Ult == False:
                        print(f"{p2} não tem o ult desbloqueado!")
                        wait()
                        clear()
                        continue
                    else:
                        p2ultCharge = 100
                        print(f"{p2} consumiu a Proteína pura! Ult em 100%!")
                        wait()
                        clear()
                        inventory.remove(10)
                        return
        elif p1action == 5:
            print(f"Passou para {p2}!")
            time.sleep(2)
            clear()
            p2menu()
            return

def p1abilities():
    global p1hp, p1sp, p1atk, p1atkBonus, p1slashBonus, p1maxHP, p2hp, p2sp, enemyhp, skipP1, skipP2, skipEnemy, p1block, p1MotivateATK, abilityCharge, p1Ult, defDebuff, defDebuffTurns, speed, speedTurns, enemyOnFire, enemyfireTurns, damageDealt, p1Damage
    while True:
        p1stats()
        print(f"------------------------{p1} - Habilidades--------------------------")
        print("[5] Slash - Dano físico com média chance de crítico (25 HP)")
        print("[6] Block - Absorve 50% do dano do aliado, se for atacado. (6 SP)")
        print("[7] Fire - Dano de fogo com baixa chance de Burn (8 SP)")
        print("[8] Adrenaline - Jogadores tem chance de desviar de ataques por 3 turnos (9 SP)")
        abilityChoice = [5, 6, 7, 8, 0]
        if lifeSteal == True:
            print("[9] Life Steal - Rouba 25 HP do inimigo para si mesmo. (10 SP)")
            abilityChoice.append(9)
        if charge == True:
            print("[10] Charge - Aumenta o ataque e a chance de crítico pro próximo ataque (12 SP)")
            abilityChoice.append(10)
        if ult == True:
            print(f"[11] Ult - 75 de dano ao inimigo, pula o próximo turno dele e recupera 15 HP para todos os aliados. (20 SP) ({p1Ult}%)")
            abilityChoice.append(11)
            
        print("[0] Voltar")
        try:
            p1ability = int(input("O que fazer: "))
        except ValueError:
            p1ability = -1
        while p1ability not in abilityChoice:
            try:
                p1ability = int(input("Escolha habilidade válida: "))
            except ValueError:
                p1ability = -1
        if p1ability == 5:
            if p1hp <= 25:
                print("HP insuficiente!")
                wait()
                clear()
                continue
            slash = random.randint(10, 40) + p1atk + p1atkBonus + p1slashBonus
            if abilityCharge:
                slashCrit = random.randint(2, 3)
            else:
                slashCrit = random.randint(1, 3)
            if p1MotivateATK == True or abilityCharge == True:
                slash *= 2
                p1MotivateATK = False
                abilityCharge = False
            if defDebuff:
                slash += 7
                defDebuffTurns += 1
                if defDebuffTurns >= 3:
                    defDebuff = False
                    defDebuffTurns = 0
            if slashCrit == 3:
                slash = int(slash * 1.5)
                print(f"Crítico! {p1} usou Slash e deu {slash} de dano! Derrubou o inimigo!")
                print("-------------------------------------------------------------")  
                skipEnemy = True
                dano_causado = min(enemyhp, slash)
                damageDealt += dano_causado
                p1Damage += dano_causado
                enemyhp -= slash
                if enemyhp < 0:
                    enemyhp = 0
                p1hp -= 25
                if p1hp < 0:
                    p1hp = 0
                wait()
                clear()
                return "extra"
            else:
                print(f"{p1} usou Slash e deu {slash} de dano!")
                print("-------------------------------------------------------------")
                wait()
                clear()
                dano_causado = min(enemyhp, slash)
                damageDealt += dano_causado
                p1Damage += dano_causado
                enemyhp -= slash
                if enemyhp < 0:
                    enemyhp = 0
                p1hp -= 25
                if p1hp < 0:
                    p1hp = 0
                return True
        elif p1ability == 6:
            if p1sp < 6:
                print("SP insuficiente!")
                wait()
                clear()
                continue
            if p2hp <= 0:
                print(f"{p2} está morto!")
                wait()
                clear()
                continue
            p1sp -= 6
            if p1sp < 0:
                p1sp = 0
            p1block = True
            print(f"Protegeu {p2}! Dano será dividido entre os dois.")
            print("-------------------------------------------------------------")
            wait()
            clear()
            return True
        elif p1ability == 7:
            if p1sp < 8:
                print("SP insuficiente!")
                wait()
                clear()
                continue
            fire = random.randint(8, 32) + p1atk + p1atkBonus
            if p1MotivateATK == True:
                fire *= 2
                p1MotivateATK = False
            if defDebuff:
                fire += 7
                defDebuffTurns += 1
                if defDebuffTurns >= 3:
                    defDebuff = False
                    defDebuffTurns = 0
            dano_causado = min(enemyhp, fire)
            damageDealt += dano_causado
            p1Damage += dano_causado
            enemyhp -= fire
            if enemyhp < 0:
                enemyhp = 0
            p1sp -= 8
            if p1sp < 0:
                p1sp = 0
            print(f"{p1} usou Fire e deu {fire} de dano!")
            p1Apply = random.randint(1, 3)
            if p1Apply == 3 and enemyhp > 0:
                enemyOnFire = True
                enemyfireTurns = 0
                print("O inimigo pegou fogo!")
            print("-------------------------------------------------------------")
            wait()
            clear()
            return True
        elif p1ability == 8:
            if p1sp < 9:
                print("SP insuficiente!")
                wait()
                clear()
                continue
            speed = True
            speedTurns = 0
            print("Aumentou os reflexos dos jogadores por 3 turnos!")
            p1sp -= 9
            if p1sp < 0:
                p1sp = 0
            wait()
            clear()
            return True
        elif p1ability == 9:
            if p1sp < 10:
                print("SP insuficiente!")
                wait()
                clear()
                continue
            print("Roubou 25 HP do inimigo!")
            dano_causado = min(enemyhp, 25)
            damageDealt += dano_causado
            p1Damage += dano_causado
            enemyhp -= 25
            if enemyhp < 0:
                enemyhp = 0
            p1sp -= 10
            if p1sp < 0:
                p1sp = 0
            p1hp += 25
            if p1hp > p1maxHP:
                p1hp = p1maxHP
            print("-------------------------------------------------------------")
            wait()
            clear()
            return True
        elif p1ability == 10:
            if isCharged():
                return True
        elif p1ability == 11:
            if p1sp < 20:
                print("SP insuficiente!")
                wait()
                clear()
                continue
            if p1Ult < 100:
                print("Carga insuficiente!")
                wait()
                clear()
                continue
            else:
                p1sp -= 20
                if p1sp < 0:
                    p1sp = 0
                p1Ult = 0
                print("Usou o ataque supremo! Carga voltou para 0.")
                skipEnemy = True
                dano_causado = min(enemyhp, 75)
                damageDealt += dano_causado
                p1Damage += dano_causado
                enemyhp -= 75
                if enemyhp < 0:
                    enemyhp = 0
                p1hp += 15
                if p1hp > p1maxHP:
                    p1hp = p1maxHP
                if p2hp > 0:
                    p2hp += 15
                    if p2hp > 80:
                        p2hp = 80
                wait()
                clear()
                return True
        elif p1ability == 0:
            clear()
            return False

def p1cards():
    global p1atkBonus, p1defBonus, p1slashBonus, lifeSteal, ult, p1, p1sp, p1hp, p1maxHP, charge, turns, invAccess, totalUpgrades
    print(f"------------------{p1} - UPGRADE-----------------")
    print("[1] ATK++  |  Aumenta seu ataque.")
    print("[2] DEF++  |  Aumenta sua defesa.")
    print("[3] HP++   |  Aprimora seu HP máximo.")
    options = [1, 2, 3]
    if turns >= 6 and lifeSteal == False:
        print("[4] STEAL  |  Desbloqueia a habilidade Life Steal.")
        options.append(4)
    if turns >= 9 and charge == False:
        print("[5] CHRG   |  Desbloqueia a habilidade Charge.")
        options.append(5)
    if turns >= 12 and ult == False:
        print("[6] ULT    |  Desbloqueia seu potencial.")
        options.append(6)
    invDrop = random.randint(1, 5)
    if invDrop == 5 and invAccess == False:
        print("[7] INV    |  Drop raro! Recebe uma mochila de itens.")
        options.append(7)
    try:
        p1upgrade = int(input("Escolha seu upgrade: "))
    except ValueError:
        p1upgrade = 0
    while p1upgrade not in options:
        try:
            p1upgrade = int(input("Escolha um upgrade válido: "))
        except ValueError:
            p1upgrade = 0
    totalUpgrades += 1
    if p1upgrade == 1:
        print("Aumentou ataque por 3. Restaurou 5 SP.")
        print("------------------------------------")
        wait()
        clear()
        p1atkBonus += 3
        p1sp += 5
        if p1sp > 30:
            p1sp = 30
    elif p1upgrade == 2:
        print("Aumentou defesa por 3. Restaurou 5 SP.")
        print("------------------------------------")
        wait()
        clear()
        p1defBonus += 3
        p1sp += 5
        if p1sp > 30:
            p1sp = 30
    elif p1upgrade == 3:
        print("Aumentou seu HP máximo por 10. Restaurou 5 SP.")
        print("------------------------------------")
        wait()
        clear()
        p1maxHP += 10
        p1hp += 10
        p1sp += 5
        if p1sp > 30:
            p1sp = 30
    elif p1upgrade == 4:
        print("Recebeu a habilidade Life Steal.")
        wait()
        clear()
        lifeSteal = True
    elif p1upgrade == 5:
        print("Recebeu a habilidade Charge.")
        wait()
        clear()
        charge = True
    elif p1upgrade == 6:
        print("Recebeu seu ataque supremo.")
        wait()
        clear()
        ult = True
    elif p1upgrade == 7:
        print("Recebeu a mochila de itens.")
        wait()
        clear()
        invAccess = True

def p2menu():
    global p1hp, p1sp, p1atk, p2hp, p2sp, p2MaxSP, enemyhp, skipP1, skipP2, skipEnemy, p2MotivateATK, p2Summon, rabbitTurn, rabbitActive, defDebuff, defDebuffTurns, p2Defend, enemyDistress, distressTurns, parryActive, damageDealt, p2Damage
    if p2hp <= 0:
        return
    p2Defend = False
    parryActive = False
    if skipP2:
        p2stats()
        print(f"{p2} não pode se mexer!")
        skipP2 = False
        wait()
        clear()
        return
    if rabbitActive and p2hp > 0:
        if rabbitTurn < 3:
            print(f"O coelho curou {p2} com 10 HP!")
            p2hp += 10
            if p2hp > 80:
                p2hp = 80
    while True:
        if p2hp <= 0 or enemyhp <= 0:
            return
        p2stats()
        print(f"------------------------{p2} - Ações--------------------------")
        print("[1] Atacar - Ataque básico com baixa chance de Distresse")
        print("[2] Magia - Menu de feitiços")
        print("[3] Defender - Restora SP e reduz dano tomado")
        p2Option = [1, 2, 3]
        if p2Summon == True:
            print("[4] Sumonar - Menu de animais")
            p2Option.append(4)
        try:
            p2action = int(input("O que fazer: "))
        except ValueError:
            p2action = 0
        while p2action not in p2Option:
            try:
                p2action = int(input("Escolha uma ação válida: "))
            except ValueError:
                p2action = 0
        if p2action == 1:
            p2dmg = random.randint(4, 16) + p2atk
            if p2MotivateATK == True:
                p2dmg *= 2
                p2MotivateATK = False
            if defDebuff:
                p2dmg += 7
                defDebuffTurns += 1
                if defDebuffTurns >= 3:
                    defDebuff = False
                    defDebuffTurns = 0
            dano_causado = min(enemyhp, p2dmg)
            damageDealt += dano_causado
            p2Damage += dano_causado
            enemyhp -= p2dmg
            if enemyhp < 0:
                enemyhp = 0
            print(f"{p2} atacou e deu {p2dmg} de dano!")
            p2Distress = random.randint(1, 6)
            if p2Distress == 6 and enemyhp > 0:
                enemyDistress = True
                distressTurns = 0
                print("O inimigo ficou distressado! -ATK")
            print("-------------------------------------------------------------")
            wait()
            clear()
            return
        elif p2action == 2:
            clear()
            if p2magic():
                return
        elif p2action == 3:
            p2sp += 15
            if p2sp > p2MaxSP:
                p2sp = p2MaxSP
            p2Defend = True
            print(f"{p2} defendeu e recuperou 15 SP!")
            print("-------------------------------------------------------------")
            wait()
            clear()
            return
        elif p2action == 4:
            clear()
            if p2Casts():
                return

def p2magic():
    global p1hp, p1sp, p1atk, p1maxHP, p2hp, p2sp, p2MaxSP, enemyhp, heal, skipP1, skipP2, p1, p2, p2MotivateATK, p2Parry, p2Ult, parryActive, p2ultCharge, defDebuff, defDebuffTurns, atkDebuff, atkDebuffTurns, skipEnemy, damageDealt, p2Damage
    while True:
        p2stats()
        print(f"------------------------{p2} - Magia--------------------------")
        print("[5] Ice - Ataque de gelo com média chance de Freeze (9 SP)")
        print(f"[6] Pray - Restaura {heal + p2magBonus} HP para o jogador de escolha (10 SP)")
        print("[7] Motivate - Aumenta a defesa e dobra o dano do próximo ataque do jogador de escolha (15 SP)")
        print(f"[8] Health Song - Cura ambos os jogadores ou revive {p1} (20 SP)")
        print("[0] Voltar")
        magicOptions = [5, 6, 7, 8, 0]
        if p2Parry == True:
            print("[9] Parry - Prepara uma postura por 1 turno que reflete o ataque e derruba o inimigo (18 SP)")
            magicOptions.append(9)
        if p2Ult == True:
            print(f"[10] Ult - 50 de dano ao inimigo, diminui o ataque e defesa dele, e restaura SP por completo. (40 HP) ({p2ultCharge}%)")
            magicOptions.append(10)
        try:
            p2action = int(input("O que fazer: "))
        except ValueError:
            p2action = -1
        while p2action not in magicOptions:
            try:
                p2action = int(input("Escolha ação válida: "))
            except ValueError:
                p2action = -1
        if p2action == 5:
            if p2sp < 9:
                print("SP insuficiente!")
                wait()
                clear()
                continue
            ice = random.randint(8, 36) + p2atk + p2magBonus
            if p2MotivateATK == True:
                ice *= 2
                p2MotivateATK = False
            if defDebuff:
                ice += 7
                defDebuffTurns += 1
                if defDebuffTurns >= 3:
                    defDebuff = False
                    defDebuffTurns = 0
            dano_causado = min(enemyhp, ice)
            damageDealt += dano_causado
            p2Damage += dano_causado
            enemyhp -= ice
            if enemyhp < 0:
                enemyhp = 0
            p2sp -= 9
            if p2sp < 0:
                p2sp = 0
            print(f"{p2} usou Ice e deu {ice} de dano!")
            if random.randint(1, 3) == 3 and enemyhp > 0:
                skipEnemy = True
                print("Congelou o inimigo!")
            print("-------------------------------------------------------------")
            wait()
            clear()
            return True
        elif p2action == 6:
            if pray():
                return True
        elif p2action == 7:
            if motivate():
                return True
        elif p2action == 8:
            if p2sp < 20:
                print("SP insuficiente!")
                wait()
                clear()
                continue
            songOption = [1, 0]
            print(f"[1] Curar todos")
            if p1hp <= 0:
                print(f"[2] Reviver {p1}")
                songOption.append(2)
            print("[0] Voltar")
            try:
                songChoice = int(input("Qual música: "))
            except ValueError:
                songChoice = -1
            while songChoice not in songOption:
                try:
                    songChoice = int(input("Escolha uma válida: "))
                except ValueError:
                    songChoice = -1
            if songChoice == 0:
                clear()
                continue
            elif songChoice == 1:
                p2sp -= 20
                if p2sp < 0:
                    p2sp = 0
                print(f"{p2} cantou uma música motivadora! Jogadores foram ambos curados por {15 + p2magBonus} HP")
                print("-------------------------------------------------------------")
                wait()
                clear()
                if p1hp > 0:
                    p1hp += (15 + p2magBonus)
                    if p1hp > p1maxHP:
                        p1hp = p1maxHP
                if p2hp > 0:
                    p2hp += (15 + p2magBonus)
                    if p2hp > 80:
                        p2hp = 80
                return True
            elif songChoice == 2:
                p2sp -= 20
                if p2sp < 0:
                    p2sp = 0
                print(f"{p2} cantou uma música rejuvenecedora! {p1} foi revivido!")
                print("-------------------------------------------------------------")
                wait()
                clear()
                p1hp = int(p1maxHP / 2)
                return True
        elif p2action == 9:
            if p2sp < 18:
                print("SP insuficiente!")
                wait()
                clear()
                continue
            parryActive = True
            print("Entrou em postura de parry por 1 turno!")
            print("-------------------------------------------------------------")
            p2sp -= 18
            if p2sp < 0:
                p2sp = 0
            wait()
            clear()
            return True
        elif p2action == 10:
            if p2ultCharge < 100 or p2hp < 41:
                print("Carga ou HP insuficiente!")
                wait()
                clear()
                continue
            else:
                p2ultCharge -= 100
                p2hp -= 40
                if p2hp < 0:
                    p2hp = 0
                print("Descarregou o ataque supremo!")
                print("-------------------------------------------------------------")
                atkDebuff = True
                atkDebuffTurns = 0
                defDebuff = True
                defDebuffTurns = 0
                p2sp = p2MaxSP
                dano_causado = min(enemyhp, 50)
                damageDealt += dano_causado
                p2Damage += dano_causado
                enemyhp -= 50
                if enemyhp < 0:
                    enemyhp = 0
                wait()
                clear()
                return True
        elif p2action == 0:
            clear()
            return False

def p2cards():
    global p2magBonus, p2defBonus, p2sp, p2, p2MaxSP, p2Summon, p2Parry, p2Ult, turns, totalUpgrades
    print(f"------------------{p2} - UPGRADE-----------------")
    print("[1] MAG++  |  Melhora sua magia.")
    print("[2] DEF++  |  Aumenta sua defesa.")
    print("[3] SP++   |  Aprimora seu SP máximo.")
    p2options = [1, 2, 3]
    if turns >= 6 and p2Parry == False:
        print("[4] PARRY  |  Desbloqueia a habilidade Parry.")
        p2options.append(4)
    if turns >= 9 and p2Summon == False:
        print("[5] ANIM   |  Desbloqueia o livro de animais.")
        p2options.append(5)
    if turns >= 12 and p2Ult == False:
        print("[6] ULT    |  Desbloqueia seu potencial.")
        p2options.append(6)
    try:
        p2upgrade = int(input("Escolha seu upgrade: "))
    except ValueError:
        p2upgrade = 0
    while p2upgrade not in p2options:
        try:
            p2upgrade = int(input("Escolha um válido: "))
        except ValueError:
            p2upgrade = 0
    totalUpgrades += 1
    if p2upgrade == 1:
        p2magBonus += 3
        p2sp += 5
        if p2sp > p2MaxSP:
            p2sp = p2MaxSP
        print("Melhorou habilidades de magia por +3! Recebeu 5 SP.")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2upgrade == 2:
        p2defBonus += 3
        p2sp += 5
        if p2sp > p2MaxSP:
            p2sp = p2MaxSP
        print("Aumentou a defesa por +3! Recebeu 5 SP.")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2upgrade == 3:
        p2MaxSP += 10
        p2sp += 15
        if p2sp > p2MaxSP:
            p2sp = p2MaxSP
        print("Aumentou SP máximo por 10!")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2upgrade == 4:
        p2Parry = True
        print("Desbloqueou a habilidade Parry.")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2upgrade == 5:
        p2Summon = True
        print("Recebeu o livro de sumonar animais.")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2upgrade == 6:
        p2Ult = True
        print("Desbloqueou seu potencial.")
        print("-------------------------------------------------------------")
        wait()
        clear()

def aplicar_dano_p1(dano):
    global p1hp, p1defBonus, p1MotivateDEF, p1Defend, damageTaken
    dano = max(0, dano - p1defBonus)
    if p1MotivateDEF:
        dano //= 2
        p1MotivateDEF = False
    if p1Defend:
        dano //= 2
    p1hp -= dano
    damageTaken += dano
    if p1hp < 0:
        p1hp = 0
    return dano

def aplicar_dano_p2(dano):
    global p2hp, p2defBonus, p2MotivateDEF, p2Defend, damageTaken
    dano = block(dano)
    dano = max(0, dano - p2defBonus)
    if p2MotivateDEF:
        dano //= 2
        p2MotivateDEF = False
    if p2Defend:
        dano //= 2
    p2hp -= dano
    damageTaken += dano
    if p2hp < 0:
        p2hp = 0
    return dano

def enemyActions():
    global p1hp, p1sp, p2hp, p2sp, enemyhp, enemyMaxHP, p1target, p2target, skipEnemy, skipP1, skipP2, playerChoice, p1block, wolfActive, wolfTurns, parryActive, atkDebuff, atkDebuffTurns
    global p1MotivateDEF, p2MotivateDEF, ragedEnemy, speed, speedTurns, enemyDistress, p1onFire, p1fireTurns, p2onFire, p2fireTurns, damageDealt, p2Damage
    if p1hp <= 0 and p2hp <= 0:
        return
    if skipEnemy:
        print("O inimigo não pode se mexer!")
        skipEnemy = False
        wait()
        clear()
        if parryActive:
            parryActive = False
            print(f"A postura de parry de {p2} acabou...")
            print("-------------------------------------------------------------")
            wait()
            clear()
        if speed:
            speedTurns += 1
            if speedTurns >= 3:
                speed = False
                speedTurns = 0
                print("A adrenalina passou...")
                print("-------------------------------------------------------------")
                wait()
                clear()
        return

    extra_turns = 1
    combo_usado = False
    while extra_turns > 0:
        extra_turns -= 1
        if (p1hp <= 0 and p2hp <= 0) or enemyhp <= 0:
            break

        if p1hp > 0 and p2hp > 0:
            peso_p1 = 50
            if p1hp < p2hp:
                peso_p1 += 25
                if p1hp <= 30:
                    peso_p1 += 10
            elif p2hp < p1hp:
                peso_p1 -= 25
                if p2hp <= 30:
                    peso_p1 -= 10
            if parryActive:
                peso_p1 = min(90, peso_p1 + 30)
            if skipP1 and p1hp <= 45:
                peso_p1 = min(95, peso_p1 + 15)
            elif skipP2 and p2hp <= 45:
                peso_p1 = max(5, peso_p1 - 15)
            playerTarget = 1 if random.randint(1, 100) <= peso_p1 else 2
        elif p1hp > 0:
            playerTarget = 1
        else:
            playerTarget = 2

        hp_ratio = enemyhp / enemyMaxHP
        target_hp = p1hp if playerTarget == 1 else p2hp
        target_burning = p1onFire if playerTarget == 1 else p2onFire
        target_stunned = skipP1 if playerTarget == 1 else skipP2

       
        decidiu_curar = False
        if enemyhp < enemyMaxHP - 15:
            if hp_ratio <= 0.25:
                chance_cura = 65
            elif hp_ratio <= 0.45:
                chance_cura = 45
            elif hp_ratio <= 0.65:
                chance_cura = 20
            else:
                chance_cura = 0
            if playerChoice == 4:
                chance_cura //= 2
            if target_hp <= 22 and chance_cura > 0:
                chance_cura = max(5, chance_cura - 25)
            if enemyDistress and hp_ratio < 0.75:
                chance_cura += 15
            if chance_cura > 0 and random.randint(1, 100) <= chance_cura:
                decidiu_curar = True

        if decidiu_curar:
            enemyChoice = 2
            enemySpell = 3
        else:
            w_atk = 35
            w_fire = 30
            w_ice = 30
            w_aoe = 35 if (ragedEnemy and p1hp > 0 and p2hp > 0) else (15 if ragedEnemy else 0)


            if target_stunned:
                w_ice = 5
                w_atk += 30
                w_fire += 20


            if not target_burning:
                w_fire += 20
            else:
                w_fire = 10
                w_atk += 15
                if not target_stunned:
                    w_ice += 15

            if enemyDistress:
                w_fire += 20
                w_ice += 20
                w_atk = 15
                w_aoe = max(0, w_aoe - 20)

            if target_hp <= 25:
                w_atk += 25
                w_fire += 15
                w_ice = 10

            if ragedEnemy and p1hp > 0 and p2hp > 0 and not parryActive:
                w_aoe += 15

            total_w = w_atk + w_fire + w_ice + w_aoe
            roll = random.randint(1, total_w)
            if roll <= w_atk:
                enemyChoice = 1
                enemySpell = 0
            elif roll <= w_atk + w_fire:
                enemyChoice = 2
                enemySpell = 1
            elif roll <= w_atk + w_fire + w_ice:
                enemyChoice = 2
                enemySpell = 2
            else:
                enemyChoice = 2
                enemySpell = 4

        if enemyChoice == 1:
            playerChoice = 1
            if playerTarget == 1:
                if ragedEnemy == True:
                    enemyatk = random.randint(10, 35) + p1target
                    if skipP1:
                        enemyatk = int(enemyatk * 1.25)
                        print(f"O inimigo aproveitou a guarda aberta de {p1}!")
                    if enemyDistress:
                        enemyatk //= 2
                    enemyCrit = random.randint(1, 4)
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou {p1} mas ele(a) desviou!")
                        print("-------------------------------------------------------------")
                        wait()
                        clear()
                    else:
                        if enemyCrit == 4:
                            enemyatk = int(enemyatk * 1.5)
                            dano_final = aplicar_dano_p1(enemyatk)
                            skipP1 = True
                            print(f"Crítico! O inimigo atacou {p1} e deu {dano_final} de dano! Derrubou {p1}!")
                            print("-------------------------------------------------------------")
                            wait()
                            clear()
                            if not combo_usado:
                                combo_usado = True
                                extra_turns += 1
                        else:
                            dano_final = aplicar_dano_p1(enemyatk)
                            print(f"O inimigo atacou {p1} e deu {dano_final} de dano!")
                            print("-------------------------------------------------------------")
                            wait()
                            clear()
                else:
                    enemyatk = random.randint(7, 28) + p1target
                    if skipP1:
                        enemyatk = int(enemyatk * 1.25)
                        print(f"O inimigo aproveitou a guarda aberta de {p1}!")
                    if enemyDistress:
                        enemyatk //= 2
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou {p1} mas ele(a) desviou!")
                        print("-------------------------------------------------------------")
                        wait()
                        clear()
                    else:
                        if atkDebuff:
                            enemyatk = max(0, enemyatk - 7)
                            atkDebuffTurns += 1
                            if atkDebuffTurns >= 3:
                                atkDebuff = False
                                atkDebuffTurns = 0
                        dano_final = aplicar_dano_p1(enemyatk)
                        print(f"O inimigo atacou {p1} e deu {dano_final} de dano!")
                        wait()
                        clear()
            elif playerTarget == 2:
                if ragedEnemy == True:
                    enemyatk = random.randint(10, 35) + p2target
                    if skipP2:
                        enemyatk = int(enemyatk * 1.25)
                        print(f"O inimigo aproveitou a guarda aberta de {p2}!")
                    if enemyDistress:
                        enemyatk //= 2
                    enemyCrit = random.randint(1, 4)
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou {p2} mas ele(a) desviou!")
                        print("-------------------------------------------------------------")
                        wait()
                        clear()
                    elif parryActive:
                        if enemyCrit == 4:
                            enemyatk = int(enemyatk * 1.5)
                        dano_refletido = min(enemyhp, enemyatk)
                        damageDealt += dano_refletido
                        p2Damage += dano_refletido
                        enemyhp -= enemyatk
                        if enemyhp < 0:
                            enemyhp = 0
                        skipEnemy = True
                        print(f"{p2} deu um parry no ataque do inimigo! -{enemyatk} HP e derrubou o inimigo!")
                        print("-------------------------------------------------------------")
                        parryActive = False
                        wait()
                        clear()
                    else:
                        if enemyCrit == 4:
                            enemyatk = int(enemyatk * 1.5)
                            dano_final = aplicar_dano_p2(enemyatk)
                            skipP2 = True
                            print(f"Crítico! O inimigo atacou {p2} e deu {dano_final} de dano! Derrubou {p2}!")
                            print("-------------------------------------------------------------")
                            wait()
                            clear()
                            if not combo_usado:
                                combo_usado = True
                                extra_turns += 1
                        else:
                            dano_final = aplicar_dano_p2(enemyatk)
                            print(f"O inimigo atacou {p2} e deu {dano_final} de dano!")
                            print("-------------------------------------------------------------")
                            wait()
                            clear()
                else:
                    enemyatk = random.randint(7, 28) + p2target
                    if skipP2:
                        enemyatk = int(enemyatk * 1.25)
                        print(f"O inimigo aproveitou a guarda aberta de {p2}!")
                    if enemyDistress:
                        enemyatk //= 2
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou {p2} mas ele(a) desviou!")
                        print("-------------------------------------------------------------")
                        wait()
                        clear()
                    else:
                        if atkDebuff:
                            enemyatk = max(0, enemyatk - 7)
                            atkDebuffTurns += 1
                            if atkDebuffTurns >= 3:
                                atkDebuff = False
                                atkDebuffTurns = 0
                        if parryActive:
                            dano_refletido = min(enemyhp, enemyatk)
                            damageDealt += dano_refletido
                            p2Damage += dano_refletido
                            enemyhp -= enemyatk
                            if enemyhp < 0:
                                enemyhp = 0
                            skipEnemy = True
                            print(f"{p2} deu um parry no ataque do inimigo! -{enemyatk} HP e derrubou o inimigo!")
                            print("-------------------------------------------------------------")
                            parryActive = False
                            wait()
                            clear()
                        else:
                            dano_final = aplicar_dano_p2(enemyatk)
                            print(f"O inimigo atacou {p2} e deu {dano_final} de dano!")
                            wait()
                            clear()
        elif enemyChoice == 2:
            if enemySpell == 1:
                playerChoice = 2
                if playerTarget == 1:
                    if ragedEnemy:
                        enemyFire = random.randint(12, 40) + p1target
                    else:
                        enemyFire = random.randint(10, 36) + p1target
                    if skipP1:
                        enemyFire = int(enemyFire * 1.25)
                        print(f"O inimigo incinerou {p1} enquanto estava imobilizado!")
                    if enemyDistress:
                        enemyFire //= 2
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou {p1} mas ele(a) desviou!")
                        print("-------------------------------------------------------------")
                        wait()
                        clear()
                    else:
                        if atkDebuff:
                            enemyFire = max(0, enemyFire - 7)
                            atkDebuffTurns += 1
                            if atkDebuffTurns >= 3:
                                atkDebuff = False
                                atkDebuffTurns = 0
                        dano_final = aplicar_dano_p1(enemyFire)
                        print(f"O inimigo usou fogo contra {p1}! Tomou {dano_final} de dano.")
                        enemyBurn = random.randint(1, 3 if skipP1 else 4)
                        if enemyBurn == 1 and p1hp > 0:
                            p1onFire = True
                            p1fireTurns = 0
                            print(f"{p1} pegou fogo!")
                        wait()
                        clear()
                elif playerTarget == 2:
                    if ragedEnemy:
                        enemyFire = random.randint(12, 40) + p2target
                    else:
                        enemyFire = random.randint(10, 36) + p2target
                    if skipP2:
                        enemyFire = int(enemyFire * 1.25)
                        print(f"O inimigo incinerou {p2} enquanto estava imobilizado!")
                    if enemyDistress:
                        enemyFire //= 2
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou {p2} mas ele(a) desviou!")
                        print("-------------------------------------------------------------")
                        wait()
                        clear()
                    else:
                        if atkDebuff:
                            enemyFire = max(0, enemyFire - 7)
                            atkDebuffTurns += 1
                            if atkDebuffTurns >= 3:
                                atkDebuff = False
                                atkDebuffTurns = 0
                        if parryActive:
                            dano_refletido = min(enemyhp, enemyFire)
                            damageDealt += dano_refletido
                            p2Damage += dano_refletido
                            enemyhp -= enemyFire
                            if enemyhp < 0:
                                enemyhp = 0
                            skipEnemy = True
                            print(f"{p2} deu um parry no ataque do inimigo! -{enemyFire} HP e derrubou o inimigo!")
                            print("-------------------------------------------------------------")
                            parryActive = False
                            wait()
                            clear()
                        else:
                            dano_final = aplicar_dano_p2(enemyFire)
                            print(f"O inimigo usou fogo contra {p2}! Tomou {dano_final} de dano.")
                            enemyBurn = random.randint(1, 3 if skipP2 else 4)
                            if enemyBurn == 1 and p2hp > 0:
                                p2onFire = True
                                p2fireTurns = 0
                                print(f"{p2} pegou fogo!")
                            wait()
                            clear()
            elif enemySpell == 2:
                playerChoice = 3
                if playerTarget == 1:
                    if ragedEnemy:
                        enemyIce = random.randint(10, 35) + p1target
                    else:
                        enemyIce = random.randint(8, 30) + p1target
                    if enemyDistress:
                        enemyIce //= 2
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou {p1} mas ele(a) desviou!")
                        print("-------------------------------------------------------------")
                        wait()
                        clear()
                    else:
                        if atkDebuff:
                            enemyIce = max(0, enemyIce - 7)
                            atkDebuffTurns += 1
                            if atkDebuffTurns >= 3:
                                atkDebuff = False
                                atkDebuffTurns = 0
                        dano_final = aplicar_dano_p1(enemyIce)
                        print(f"O inimigo usou gelo contra {p1}! Tomou {dano_final} de dano.")
                        if ragedEnemy:
                            enemyFreeze = random.randint(1, 2)
                        else:
                            enemyFreeze = random.randint(1, 3)
                        if enemyFreeze == 1 and p1hp > 0:
                            skipP1 = True
                            time.sleep(2)
                            print(f"Congelou! {p1} não pode se mexer!")
                            if ragedEnemy and not combo_usado:
                                print("O inimigo prepara um golpe em seguida!")
                                combo_usado = True
                                extra_turns += 1
                        wait()
                        clear()
                elif playerTarget == 2:
                    if ragedEnemy:
                        enemyIce = random.randint(10, 35) + p2target
                    else:
                        enemyIce = random.randint(8, 30) + p2target
                    if enemyDistress:
                        enemyIce //= 2
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou {p2} mas ele(a) desviou!")
                        print("-------------------------------------------------------------")
                        wait()
                        clear()
                    else:
                        if atkDebuff:
                            enemyIce = max(0, enemyIce - 7)
                            atkDebuffTurns += 1
                            if atkDebuffTurns >= 3:
                                atkDebuff = False
                                atkDebuffTurns = 0
                        if parryActive:
                            dano_refletido = min(enemyhp, enemyIce)
                            damageDealt += dano_refletido
                            p2Damage += dano_refletido
                            enemyhp -= enemyIce
                            if enemyhp < 0:
                                enemyhp = 0
                            skipEnemy = True
                            print(f"{p2} deu um parry no ataque do inimigo! -{enemyIce} HP e derrubou o inimigo!")
                            print("-------------------------------------------------------------")
                            parryActive = False
                            wait()
                            clear()
                        else:
                            dano_final = aplicar_dano_p2(enemyIce)
                            print(f"O inimigo usou gelo contra {p2}! Tomou {dano_final} de dano.")
                            if ragedEnemy:
                                enemyFreeze = random.randint(1, 2)
                            else:
                                enemyFreeze = random.randint(1, 3)
                            if enemyFreeze == 1 and p2hp > 0:
                                skipP2 = True
                                time.sleep(2)
                                print(f"Congelou! {p2} não pode se mexer!")
                                if ragedEnemy and not combo_usado:
                                    print("O inimigo prepara um golpe em seguida!")
                                    combo_usado = True
                                    extra_turns += 1
                            wait()
                            clear()
            elif enemySpell == 3:
                playerChoice = 4
                if ragedEnemy == True:
                    enemyhp += 50
                    if enemyhp > enemyMaxHP:
                        enemyhp = enemyMaxHP
                    print("O inimigo se curou com 50 HP.")
                    wait()
                    clear()
                else:
                    enemyhp += 30
                    if enemyhp > enemyMaxHP:
                        enemyhp = enemyMaxHP
                    print("O inimigo se curou com 30 HP.")
                    wait()
                    clear()
            elif enemySpell == 4:
                playerChoice = 5
                dano_area = 35 // 2 if enemyDistress else 35
                if p1hp > 0:
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou loucamente! Mas {p1} desviou!")
                    else:
                        dano_p1_area = int(dano_area * 1.25) if skipP1 else dano_area
                        if skipP1:
                            print(f"{p1} estava vulnerável ao ataque em área!")
                        dano_final_p1 = aplicar_dano_p1(dano_p1_area)
                        print(f"O inimigo atacou loucamente! {p1} foi atingido por {dano_final_p1} HP.")
                if p2hp > 0:
                    if speed and random.randint(1, 4) == 1:
                        print(f"O inimigo atacou loucamente! Mas {p2} desviou!")
                    elif parryActive:
                        dano_refletido = min(enemyhp, dano_area)
                        damageDealt += dano_refletido
                        p2Damage += dano_refletido
                        enemyhp -= dano_area
                        if enemyhp < 0:
                            enemyhp = 0
                        skipEnemy = True
                        parryActive = False
                        print(f"{p2} deu um parry no ataque louco do inimigo! -{dano_area} HP e derrubou o inimigo!")
                    else:
                        dano_p2_area = int(dano_area * 1.25) if skipP2 else dano_area
                        if skipP2:
                            print(f"{p2} estava vulnerável ao ataque em área!")
                        dano_final_p2 = aplicar_dano_p2(dano_p2_area)
                        print(f"O inimigo atacou loucamente! {p2} foi atingido por {dano_final_p2} HP.")
                wait()
                clear()

    if parryActive:
        parryActive = False
        print(f"A postura de parry de {p2} acabou...")
        print("-------------------------------------------------------------")
        wait()
        clear()

    if speed:
        speedTurns += 1
        if speedTurns >= 3:
            speed = False
            speedTurns = 0
            print("A adrenalina passou...")
            print("-------------------------------------------------------------")
            wait()
            clear()

# o jogo
clear()
print("-----------------------------------")
print("        Batalha iniciada!")
print("-----------------------------------")
wait()
clear()

while (p1hp > 0 or p2hp > 0) and enemyhp > 0:
    if enemyOnFire:
        burn()
    if enemyhp <= 0:
        break
    if enemyDistress:
        distress()
    if wolfActive:
        if wolfTurns < 3:
            dano_lobo = min(enemyhp, 15)
            enemyhp -= 15
            damageDealt += dano_lobo
            p2Damage += dano_lobo
            if enemyhp < 0:
                enemyhp = 0
            print("O lobo atacou e deu 15 HP de dano!")
            print("-------------------------------------------------------------")
            wolfTurns += 1
            wait()
            clear()
        if wolfTurns == 3:
            wolfActive = False
            wolfTurns = 0
            print("O lobo dissipou...")
            print("-------------------------------------------------------------")
            wait()
            clear()
    if enemyhp <= 0:
        break

    if p1hp > 0:
        if p1onFire:
            p1Burn()
        if p1hp > 0:
            if turns != 0 and turns % 3 == 0:
                p1cards()
            p1menu()
    if enemyhp <= 0:
        break

    if p2hp > 0:
        if p2onFire:
            p2Burn()
        if p2hp > 0:
            if turns != 0 and turns % 3 == 0:
                p2cards()
            p2menu()
    if enemyhp <= 0:
        break

    if rabbitActive:
        rabbitTurn += 1
        if rabbitTurn >= 3:
            rabbitActive = False
            rabbitTurn = 0
            print("O coelho dissipou...")
            print("-------------------------------------------------------------")
            wait()
            clear()

    if enemyhp <= 125 and ragedEnemy == False:
        print("O inimigo está furioso! Ataque e magia subiram!")
        enemyhp += 150
        enemyMaxHP += 75
        if enemyhp > enemyMaxHP:
            enemyhp = enemyMaxHP
        ragedEnemy = True
        wait()
        clear()
    enemyActions()

    turns += 1
    if ult == True:
        p1Ult += 10
        if p1Ult > 100:
            p1Ult = 100
    if p2Ult == True:
        p2ultCharge += 10
        if p2ultCharge > 100:
            p2ultCharge = 100

if p1Damage > p2Damage:
    melhor_jogador = f"{p1} ({p1Damage} de dano)"
elif p2Damage > p1Damage:
    melhor_jogador = f"{p2} ({p2Damage} de dano)"
else:
    melhor_jogador = f"Empate ({p1Damage} de dano cada)"

if p1hp <= 0 and p2hp <= 0:
    print("------Estatísticas de derrota------")
    print("Os jogadores perderam... womp womp")
    print(f"\nTotal de turnos: {turns}")
    print(f"Dano total levado: {damageTaken}")
    print(f"Dano total causado: {damageDealt}")
    print(f"Dano de {p1}: {p1Damage}")
    print(f"Dano de {p2}: {p2Damage}")
    print(f"Upgrades totais: {totalUpgrades}")
    print(f"Melhor jogador: {melhor_jogador}")
elif enemyhp <= 0:
    print("------Estatísticas de vitória------")
    print("Os jogadores venceram! yippie!")
    print(f"\nTotal de turnos: {turns}")
    print(f"Dano total levado: {damageTaken}")
    print(f"Dano total causado: {damageDealt}")
    print(f"Dano de {p1}: {p1Damage}")
    print(f"Dano de {p2}: {p2Damage}")
    print(f"Upgrades totais: {totalUpgrades}")
    print(f"Melhor jogador: {melhor_jogador}")