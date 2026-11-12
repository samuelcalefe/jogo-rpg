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

# estatisticas do jogador 2
p2hp = 80
if p2hp > 80:
    p2hp = 80
p2sp = 60
p2MaxSP = 60
if p2sp > p2MaxSP:
    p2sp = p2MaxSP
p2atk = 0
heal = 20
p2magBonus = 0
p2defBonus = 0
p2fireTurns = 0
p2ultCharge = 0
rabbitTurn = 0
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
turns = 1
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
    global p1fireTurns, p1hp, p1onFire
    p1fireTurns += 1
    while p1fireTurns % 3 != 0:
        p1onFire = True
        print(f"{p1} está queimando! -10HP")
        print("-------------------------------------------------------------")
        p1hp -= 10
        return
    else:
        p1onFire = False
        print("O fogo se passou...")

def p2Burn():
    global p2fireTurns, p2hp, p2onFire
    p2fireTurns += 1
    while p2fireTurns % 3 != 0:
        p2onFire = True
        print(f"{p2} está queimando! -10HP")
        print("-------------------------------------------------------------")
        p2hp -= 10
        return
    else:
        p2onFire = False
        print("O fogo se passou...")

def p2Casts():
    global p2, p2sp, rabbitActive, wolfActive
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
        animal = int(input("Escolha válido [1/2]:"))
    if animal == 1:
        if rabbitActive == True:
            print("Um animal já está ativo!")
            print("-------------------------------------------------------------")
            wait()
            clear()
            p2menu()
        else:
            wolfActive = True
            p2sp -= 20
            print("Sumonou o lobo!")
            print("-------------------------------------------------------------")
            wait()
            clear()
    elif animal == 2:
        if wolfActive == True:
            print("Um animal já está ativo!")
            print("-------------------------------------------------------------")
            wait()
            clear()
            p2menu()
        else:
            rabbitActive = True
            p2sp -= 20
            print("Sumonou o coelho!")
            print("-------------------------------------------------------------")
            wait()
            clear()
    elif animal == 3:
        clear()
        p2menu()

def burn():
    global enemyfireTurns, enemyhp, enemyOnFire
    enemyfireTurns += 1
    while enemyfireTurns % 3 != 0 and enemyfireTurns != 0:
        enemyOnFire = True
        print("O inimigo está queimando! -15HP")
        print("-------------------------------------------------------------")
        enemyhp -= 15
        wait()
        clear()
        return
    else:
        enemyOnFire = False
        print("O fogo do inimigo se passou...")
        wait()
        clear()

def distress():
    global p1target, p2target, enemyDistress, distressTurns
    distressTurns += 1
    while distressTurns % 3 != 0 and distressTurns != 0:
        enemyDistress = True
        print("O inimigo está distressado! -ATK")
        wait()
        clear()
        print("-------------------------------------------------------------")
        p1target //= 2
        p2target //= 2
    else:
        enemyDistress = False
        print("O distresse passou...")

def pray():
    global p1, p1hp, p2, p2hp, p2sp, heal
    if p2sp < 10:
        print("SP insuficiente.")
        wait()
        clear()
        p2menu()
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
        print(f"Curou {p1} com {heal + p2magBonus}HP!")
        wait()
        clear()
        p2sp -= 10
        p1hp += (heal + p2magBonus)
    elif healChoice == 2:
        print(f"Curou {p2} com {heal + p2magBonus}HP!")
        wait()
        clear()
        p2sp -= 10
        p2hp += (heal + p2magBonus)
    elif healChoice == 3:
        clear()
        p2magic()

def block():
    global p1hp, p1sp, p2, p2hp, p2target, p1block, playerChoice
    if p1block:
        p1absorb = p2target // 2
        p1hp -= p1absorb
        print(f"Absorveu {p1absorb} do dano!")
        p1block = False
        wait()
        clear()

def motivate():
    global p2sp, p1MotivateATK, p2MotivateATK, p1MotivateDEF, p2MotivateDEF, p1, p2
    if p2sp < 15:
        print("SP Insuficiente.")
        wait()
        clear()
        p2menu()
        return
    print("-------------------------------------------------------------")
    print(f"[1] {p1}")
    print(f"[2] {p2}")
    print(f"[3] Voltar")
    try:
        mot = int(input("Motivar quem: "))
    except ValueError:
        mot = 0
    while mot not in [1, 2, 3]:
        mot = int(input("Escolha 1 ou 2: "))
    if mot == 1:
        p1MotivateATK = True
        p2MotivateDEF = True
        print(f"{p1} foi motivado! ATK+ e DEF+")
        wait()
        clear()
        p2sp -= 15
    elif mot == 2:
        p2MotivateATK = True
        p2MotivateDEF = True
        print(f"{p2} foi motivado! ATK+ e DEF+")
        wait()
        clear()
        p2sp -= 15
    elif mot == 3:
        clear()
        p2magic()

def isCharged():
    global p1sp, abilityCharge
    abilityCharge = True
    p1sp -= 12
    print("Carregou o próximo ataque físico!")
    print("-------------------------------------------------------------")
    wait()
    clear()

# ações                               
def p1menu():
    global p1hp, p1sp, p1atk, p2hp, p2sp, enemyhp, skipP1, skipP2, skipEnemy, p1MotivateATK, p1maxHP, abilityCharge, rabbitTurn, rabbitActive, defDebuff, defDebuffTurns
    if p1hp <= 0:
        return
    if p1hp > p1maxHP:
        p1hp = p1maxHP
    p1stats()
    if skipP1:
        print(f"{p1} não pode se mexer!")
        skipP1 = False
        wait()
        clear()
        return
    if rabbitActive:
        if rabbitTurn < 3:
            print(f"O coelho curou {p1} com 10 HP!")
            p1hp += 10
        if rabbitTurn == 3:
            rabbitActive = False
            rabbitTurn = 0
            print("O coelho dissipou...")
    print(f"------------------------{p1} - Ações--------------------------")
    print("[1] Atacar - Dano básico com baixa chance de crítico")
    print("[2] Habilidades - Menu de habilidades")
    print("[3] Defender - Restora SP e reduz dano tomado")
    if skipEnemy == True:
        actOption = [1, 2, 3, 4]
        print(f"[4] Trocar - Passa seu turno extra para {p2}")
    else:
        actOption = [1, 2, 3]
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
        p1dmg = random.randint(6, 24)
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
        crit = random.randint(1, 6)
        if crit == 6:
            p1dmg = int(p1dmg * 1.5)
            print(f"Crítico! {p1} atacou e deu {p1dmg} de dano! Derrubou o inimigo!")
            print("-------------------------------------------------------------")  
            skipEnemy = True
            enemyhp -= p1dmg
            wait()
            clear()
            print("-------------------------TURNO EXTRA!------------------------")
            p1menu()
        else:
            print(f"{p1} atacou e deu {p1dmg} de dano!")
            print("-------------------------------------------------------------")
            enemyhp -= p1dmg
            wait()
            clear()
    elif p1action == 2:
        clear()
        p1abilities()
    elif p1action == 3:
        p1sp += 10
        print(f"{p1} defendeu e recuperou 10 SP!")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p1action == 4:
        print(f"Passou para {p2}!")
        time.sleep(2)
        clear()
        p2menu()

def p1abilities():
    global p1hp, p1sp, p1atk, p2hp, p2sp, enemyhp, skipP1, skipP2, skipEnemy, p1block, p1MotivateATK, abilityCharge, p1Ult, defDebuff, defDebuffTurns
    p1stats()
    print(f"------------------------{p1} - Habilidades--------------------------")
    print("[5] Slash - Dano físico com média chance de crítico (25 HP)")
    print("[6] Block - Absorve 50% do dano do aliado, se for atacado. (6 SP)")
    print("[7] Fire - Dano de fogo com baixa chance de Burn (8 SP)")
    abilityChoice = [5, 6, 7, 0]
    if lifeSteal == True:
        print("[8] Life Steal - Rouba 25 HP do inimigo para si mesmo. (10 SP)")
        abilityChoice.append(8)
    if charge == True:
        print("[9] Charge - Aumenta o ataque e a chance de crítico pro próximo ataque (12 SP)")
        abilityChoice.append(9)
    if ult == True:
        print(f"[10] Ult - 75 de dano ao inimigo, pula o próximo turno dele e recupera 15 HP para todos os aliados. (20 SP) ({p1Ult}%)")
        abilityChoice.append(10)
        
    print("[0] Voltar")
    try:
        p1ability = int(input("O que fazer: "))
    except ValueError:
        p1ability = 0
    while p1ability not in abilityChoice:
        try:
            p1ability = int(input("Escolha habilidade válida: "))
        except ValueError:
            p1ability = 0
    if p1ability == 5:
        slash = random.randint(10, 40) + p1atk + p1atkBonus + p1slashBonus
        if defDebuff:
            slash += 7
            defDebuffTurns += 1
            if defDebuffTurns >= 3:
                defDebuff = False
                defDebuffTurns = 0
        if p1MotivateATK == True or abilityCharge == True:
            slash *= 2
            p1MotivateATK = False
            abilityCharge = False
        enemyhp -= slash
        p1hp -= 25
        slashCrit = random.randint(1, 3)
        if slashCrit == 3:
            slash = int(slash * 1.5)
            print(f"Crítico! {p1} usou Slash e deu {slash} de dano! Derrubou o inimigo!")
            print("-------------------------------------------------------------")  
            skipEnemy = True
            wait()
            clear()
            print("-------------------------TURNO EXTRA!------------------------")
            p1menu()
        else:
            print(f"{p1} usou Slash e deu {slash} de dano!")
            print("-------------------------------------------------------------")
            wait()
            clear()
    elif p1ability == 6:
        p1sp -= 6
        p1block = True
        print(f"Protegeu {p2}! Dano será dividido entre os dois.")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p1ability == 7:
        fire = random.randint(8, 32) + p1atk
        if defDebuff:
            fire += 7
            defDebuffTurns += 1
            if defDebuffTurns >= 3:
                defDebuff = False
                defDebuffTurns = 0
        if p1MotivateATK == True:
            fire *= 2
            p1MotivateATK = False
        enemyhp -= fire
        p1sp -= 8
        print(f"{p1} usou Fire e deu {fire} de dano!")
        p1Apply = random.randint(1, 3)
        if p1Apply == 3:
            burn()
        else:
            print("-------------------------------------------------------------")
            wait()
            clear()
    elif p1ability == 8:
        print("Roubou 25 HP do inimigo!")
        enemyhp -= 25
        p1sp -= 10
        p1hp += 25
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p1ability == 9:
        isCharged()
    elif p1ability == 10:
        if p1Ult < 100:
            print("Carga insuficiente!")
            wait()
            clear()
            p1abilities()
        else:
            p1sp -= 20
            p1Ult = 0
            print("Usou o ataque supremo! Carga voltou para 0.")
            skipEnemy = True
            enemyhp -= 75
            p1hp += 15
            p2hp += 15
            wait()
            clear()
    elif p1ability == 0:
        clear()
        p1menu()

def p1cards():
    global p1atkBonus, p1defBonus, p1slashBonus, lifeSteal, ult, p1, p1sp, p1hp, p1maxHP, charge, turns
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
    try:
        p1upgrade = int(input("Escolha seu upgrade: "))
    except ValueError:
        p1upgrade = 0
    while p1upgrade not in options:
        try:
            p1upgrade = int(input("Escolha um upgrade válido: "))
        except ValueError:
            p1upgrade = 0
    if p1upgrade == 1:
        print("Aumentou ataque por 3. Restaurou 5 SP.")
        print("------------------------------------")
        wait()
        clear()
        p1atkBonus += 3
        p1sp += 5
    elif p1upgrade == 2:
        print("Aumentou defesa por 2. Restaurou 5 SP.")
        print("------------------------------------")
        wait()
        clear()
        p1defBonus += 2
        p1sp += 5
    elif p1upgrade == 3:
        print("Aumentou seu HP máximo por 10. Restaurou 5 SP.")
        print("------------------------------------")
        wait()
        clear()
        p1maxHP += 10
        p1sp += 5
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

def p2menu():
    global p1hp, p1sp, p1atk, p2hp, p2sp, enemyhp, skipP1, skipP2, skipEnemy, p2MotivateATK, p2Summon, rabbitTurn, rabbitActive, defDebuff, defDebuffTurns
    if p2hp <= 0:
        return
    if rabbitActive:
        if rabbitTurn < 3:
            print(f"O coelho curou {p2} com 10 HP!")
            p2hp += 10
    if rabbitTurn == 3:
        rabbitActive = False
        rabbitTurn = 0
        print("O coelho dissipou...")
    p2stats()
    if skipP2:
        print(f"{p2} não pode se mexer!")
        skipP2 = False
        wait()
        clear()
        return
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
        if defDebuff:
            p2dmg += 7
            defDebuffTurns += 1
            if defDebuffTurns >= 3:
                defDebuff = False
                defDebuffTurns = 0
        if p2MotivateATK == True:
            p2dmg *= 2
            p2MotivateATK = False
        enemyhp -= p2dmg
        print(f"{p2} atacou e deu {p2dmg} de dano!")
        p2Distress = random.randint(1, 6)
        if p2Distress == 6:
            distress()
        else:
            print("-------------------------------------------------------------")
            wait()
            clear()
    elif p2action == 2:
        clear()
        p2magic()
    elif p2action == 3:
        p2sp += 15
        p2Defend = True
        print(f"{p2} defendeu e recuperou 15 SP!")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2action == 4:
        p2Casts()

def p2magic():
    global p1hp, p1sp, p1atk, p2hp, p2sp, enemyhp, heal, skipP1, skipP2, p1, p2, p2MotivateATK, p2Parry, p2Ult, parryActive, p2ultCharge, defDebuff, defDebuffTurns
    p2stats()
    print(f"------------------------{p2} - Magia--------------------------")
    print("[5] Ice - Ataque de gelo com média chance de Freeze (9 SP)")
    print(f"[6] Pray - Restaura {heal + p2magBonus} HP para o jogador de escolha (10 SP)")
    print("[7] Motivate - Aumenta a defesa e dobra o dano do próximo ataque do jogador de escolha (15 SP)")
    print("[0] Voltar")
    magicOptions = [5, 6, 7, 0]
    if p2Parry == True:
        print("[8] Parry - Prepara uma barreira protetora que reflete um ataque (18 SP)")
        magicOptions.append(8)
    if p2Ult == True:
        print(f"[9] Ult - 50 de dano ao inimigo, diminui o ataque e defesa dele, e restaura SP por completo. (40 HP) ({p2ultCharge}%)")
        magicOptions.append(9)
    try:
        p2action = int(input("O que fazer: "))
    except ValueError:
        p2action = 0
    while p2action not in magicOptions:
        try:
            p2action = int(input("Escolha ação válida: "))
        except ValueError:
            p2action = 0
    if p2action == 5:
        ice = random.randint(8, 36) + p2atk + p2magBonus
        if defDebuff:
            ice += 7
            defDebuffTurns += 1
            if defDebuffTurns >= 3:
                defDebuff = False
                defDebuffTurns = 0
        if p2MotivateATK == True:
            ice *= 2
            p2MotivateATK = False
        enemyhp -= ice
        p2sp -= 9
        print(f"{p2} usou Ice e deu {ice} de dano!")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2action == 6:
        pray()
    elif p2action == 7:
        motivate()
    elif p2action == 8:
        parryActive = True
        print("Levantou uma barreira protetora!")
        print("-------------------------------------------------------------")
        p2sp -= 18
        wait()
        clear()
    elif p2action == 9:
        if p2ultCharge < 100 or p2hp < 41:
            print("Carga insuficiente!")
            wait()
            clear()
            p2magic()
        else:
            p2ultCharge -= 100
            p2hp -= 40
            print("Descarregou o ataque supremo!")
            print("-------------------------------------------------------------")
            atkDebuff = True
            defDebuff = True
            p2sp = p2MaxSP
            enemyhp -= 50
    elif p2action == 0:
        clear()
        p2menu()

def p2cards():
    global p2magBonus, p2defBonus, p2sp, p2, p2MaxSP, p2Summon, p2Parry, p2Ult, turns
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
        p2upgrade = int(input("Escolha um válido: "))
    if p2upgrade == 1:
        p2magBonus += 4
        p2sp += 5
        print("Melhorou habilidades de magia por +4! Recebeu 5 SP.")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2upgrade == 2:
        p2defBonus += 4
        p2sp += 5
        print("Aumentou a defesa por +4! Recebeu 5 SP.")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2upgrade == 3:
        p2MaxSP += 5
        p2sp += 5
        print("Aumentou SP máximo por 5!")
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

def enemyActions():
    global p1hp, p1sp, p2hp, p2sp, enemyhp, p1target, p2target, skipEnemy, skipP1, skipP2, playerChoice, p1block, wolfActive, wolfTurns, parryActive, atkDebuff, atkDebuffTurns
    global p1MotivateDEF, p2MotivateDEF, ragedEnemy
    if p1hp <= 0 and p2hp <= 0:
        return
    if skipEnemy:
        print("O inimigo não pode se mexer!")
        skipEnemy = False
        wait()
        clear()
        return
    if wolfActive:
        if wolfTurns < 3:
            enemyhp -= 15
            print("O lobo atacou e deu 15 HP de dano!")
            print("-------------------------------------------------------------")
            wolfTurns += 1
            wait()
            clear()
        if wolfTurns == 3:
            wolfActive = False
            print("O lobo dissipou...")
            print("-------------------------------------------------------------")
            wolfTurns = 0
            wait()
            clear()
    
    if p1hp > 0 and p2hp > 0:
        playerTarget = random.randint(1, 2)
    elif p1hp > 0:
        playerTarget = 1
    else:
        playerTarget = 2

    enemyChoice = random.randint(1, 2)
    if enemyChoice == 1:
        if playerTarget == 1:
            if ragedEnemy == True:
                enemyatk = random.randint(10, 35) + p1target
                enemyCrit = random.randint(1, 4)
                if enemyCrit == 4:
                    enemyatk *= 1.5
                    p1hp -= enemyatk
                    skipP1 = True
                    print(f"Crítico! O inimigo atacou {p1} e deu {enemyatk} de dano! Derrubou {p1}!")
                    print("-------------------------------------------------------------")
                    wait()
                    clear()
                    enemyActions()
                else:
                    p1hp -= enemyatk
                    print(f"O inimigo atacou {p1} e deu {enemyatk} de dano!")
                    print("-------------------------------------------------------------")
                    wait()
                    clear()
            else:
                enemyatk = random.randint(7, 28) + p1target
                if atkDebuff:
                    enemyatk -= 7
                    atkDebuffTurns += 1
                    if atkDebuffTurns >= 3:
                        atkDebuff = False
                        atkDebuffTurns = 0
                if p1MotivateDEF == True:
                    enemyatk //= 2
                    print(f"O inimigo atacou {p1} e deu {enemyatk} de dano!")
                    p1MotivateDEF = False
                    wait()
                    clear()
                else:
                    p1hp -= enemyatk
                    print(f"O inimigo atacou {p1} e deu {enemyatk} de dano!")
                    wait()
                    clear()
        elif playerTarget == 2:
            if ragedEnemy == True:
                enemyatk = random.randint(10, 35) + p2target
                enemyCrit = random.randint(1, 4)
                if enemyCrit == 4:
                    enemyatk *= 1.5
                    p2hp -= enemyatk
                    skipP2 = True
                    print(f"Crítico! O inimigo atacou {p2} e deu {enemyatk} de dano! Derrubou {p2}!")
                    print("-------------------------------------------------------------")
                    wait()
                    clear()
                    enemyActions()
                else:
                    p2hp -= enemyatk
                    print(f"O inimigo atacou {p2} e deu {enemyatk} de dano!")
                    print("-------------------------------------------------------------")
                    wait()
                    clear()
            else:
                enemyatk = random.randint(7, 28) + p2target
                if atkDebuff:
                    enemyatk -= 7
                    atkDebuffTurns += 1
                    if atkDebuffTurns >= 3:
                        atkDebuff = False
                        atkDebuffTurns = 0
            if parryActive:
                enemyhp -= enemyatk
                print(f"{p2} deu um parry no ataque do inimigo! -{enemyatk} HP")
                print("-------------------------------------------------------------")
                parryActive = False
                wait()
                clear()
            else:
                if p1block:
                    p1absorb = enemyatk // 2
                    enemyatk -= p1absorb
                    p1hp -= p1absorb
                    print(f"{p1} bloqueou e absorveu {p1absorb} do dano!")
                    p1block = False
                if p2MotivateDEF == True:
                    enemyatk //= 2
                    print(f"O inimigo atacou {p2} e deu {enemyatk} de dano!")
                    p2MotivateDEF = False
                    wait()
                    clear()
                else:
                    p2hp -= enemyatk
                    print(f"O inimigo atacou {p2} e deu {enemyatk} de dano!")
                    wait()
                    clear()
    elif enemyChoice == 2:
        enemySpell = random.randint(1, 4)
        if enemySpell == 1:
            if playerTarget == 1:
                if ragedEnemy:
                    enemyFire = random.randint(12, 40) + p1target
                else:
                    enemyFire = random.randint(10, 36) + p1target
                if atkDebuff:
                    enemyFire -= 7
                    atkDebuffTurns += 1
                    if atkDebuffTurns >= 3:
                        atkDebuff = False
                        atkDebuffTurns = 0
                if p1MotivateDEF == True:
                    enemyFire //= 2
                    p1hp -= enemyFire
                    print(f"O inimigo usou fogo contra {p1}! Tomou {enemyFire} de dano.")
                    p1MotivateDEF = False
                else:
                    p1hp -= enemyFire
                    print(f"O inimigo usou fogo contra {p1}! Tomou {enemyFire} de dano.")
            elif playerTarget == 2:
                if ragedEnemy:
                    enemyFire = random.randint(12, 40) + p2target
                else:
                    enemyFire = random.randint(10, 36) + p2target
                if atkDebuff:
                    enemyFire -= 7
                    atkDebuffTurns += 1
                    if atkDebuffTurns >= 3:
                        atkDebuff = False
                        atkDebuffTurns = 0
                if parryActive:
                    enemyhp -= enemyFire
                    print(f"{p2} deu um parry no ataque do inimigo! -{enemyFire} HP")
                    print("-------------------------------------------------------------")
                    parryActive = False
                    wait()
                    clear()
                else:
                    if p2MotivateDEF == True:
                        enemyFire //= 2
                        p2hp -= enemyFire
                        print(f"O inimigo usou fogo contra {p2}! Tomou {enemyFire} de dano.")
                        p2MotivateDEF = False
                    else:
                        p2hp -= enemyFire
                        print(f"O inimigo usou fogo contra {p2}! Tomou {enemyFire} de dano.")
                    enemyBurn = random.randint(1, 4)
                    if enemyBurn == 4:
                        p2Burn()
                        wait()
                        clear()
                    else:
                        wait()
                        clear()
        elif enemySpell == 2:
            if playerTarget == 1:
                if ragedEnemy:
                    enemyIce = random.randint(10, 35)
                else:
                    enemyIce = random.randint(8, 30) + p1target
                if atkDebuff:
                    enemyIce -= 7
                    atkDebuffTurns += 1
                    if atkDebuffTurns >= 3:
                        atkDebuff = False
                        atkDebuffTurns = 0
                if p1MotivateDEF == True:
                    enemyIce //= 2
                    p1hp -= enemyIce
                    print(f"O inimigo usou gelo contra {p1}! Tomou {enemyIce} de dano.")
                    p1MotivateDEF = False
                else:
                    p1hp -= enemyIce
                    print(f"O inimigo usou gelo contra {p1}! Tomou {enemyIce} de dano.")
                if ragedEnemy:
                    enemyFreeze = random.randint(1, 2)
                else:
                    enemyFreeze = random.randint(1, 3)
                if enemyFreeze == 3:
                    skipP1 = True
                    time.sleep(2)
                    print(f"Congelou! {p1} não pode se mexer!")
                    wait()
                    clear()
                else:
                    wait()
                    clear()
            elif playerTarget == 2:
                if ragedEnemy:
                    enemyIce = random.randint(10, 35) + p2target
                enemyIce = random.randint(8, 30) + p2target
                if atkDebuff:
                    enemyIce -= 7
                    atkDebuffTurns += 1
                    if atkDebuffTurns >= 3:
                        atkDebuff = False
                        atkDebuffTurns = 0
                if parryActive:
                    enemyhp -= enemyIce
                    print(f"{p2} deu um parry no ataque do inimigo! -{enemyIce} HP")
                    print("-------------------------------------------------------------")
                    parryActive = False
                    wait()
                    clear()
                else:
                    if p2MotivateDEF:
                        enemyIce //= 2
                        p2hp -= enemyIce
                        print(f"O inimigo usou gelo contra {p2}! Tomou {enemyIce} de dano.")
                        p2MotivateDEF = False
                    else:
                        p2hp -= enemyIce
                        print(f"O inimigo usou gelo contra {p2}! Tomou {enemyIce} de dano.")
                if ragedEnemy:
                    enemyFreeze = random.randint(1, 2)
                else:
                    enemyFreeze = random.randint(1, 3)
                if enemyFreeze == 3:
                    skipP2 = True
                    time.sleep(2)
                    print(f"Congelou! {p2} não pode se mexer!")
                    wait()
                    clear()
                else:
                    wait()
                    clear()
        elif enemySpell == 3:
            if ragedEnemy == True:
                enemyhp += 50
                print("O inimigo se curou com 50 HP.")
                wait()
                clear()
            else:
                enemyhp += 30
                print("O inimigo se curou com 30 HP.")
                wait()
                clear()
        elif enemySpell == 4:
            if ragedEnemy == True:
                p1hp -= 35
                p2hp -= 35
                print(f"O inimigo atacou loucamente! {p1} e {p2} ambos foram atingidos por 35 HP.")
                wait()
                clear()
            else:
                enemyActions()

# o jogo
clear()
print("-----------------------------------")
print("        Batalha iniciada!")
print("-----------------------------------")
wait()
clear()

while (p1hp > 0 or p2hp > 0) and enemyhp > 0:
    if p1hp > 0:
        if turns % 3 == 0:
            p1cards()
        p1menu()
    if enemyhp <= 0:
        break
    if p2hp > 0:
        if turns % 3 == 0:
            p2cards()
        p2menu()
    if enemyhp <= 0:
        break
    if enemyhp <= 125 and ragedEnemy == False:
        print("O inimigo está furioso! Ataque e magia subiram!")
        enemyhp += 150
        enemyMaxHP += 75
        ragedEnemy = True
    else:
        enemyActions()
    turns += 1
    if rabbitActive:
        rabbitTurn += 1
    if ult == True:
        p1Ult += 10
    if p2Ult == True:
        p2ultCharge += 10

if p1hp <= 0 and p2hp <= 0:
    print("Os jogadores perderam... womp womp")
    print(f"Total de turnos: {turns}")
elif enemyhp <= 0:
    print("Os jogadores venceram! yippie!")
    print(f"Total de turnos: {turns}")