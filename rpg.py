# RPG Mini Battle Simulator

import random

enemy = random.choice(['dragon','goblin','troll','kobold','skeleton']).upper()
player = input("\nEnter your name: ").upper()
pHealth = 100
eHealth = 100
turn = 1

print("\nRPG Mini Battle\n****************")
print(f"{player} vs {enemy}\n")
print(f"{player} Health : {pHealth} \n{enemy} Health : {eHealth} ")

while eHealth > 0 and pHealth > 0:
    print("\nTURN ",turn)
    print("\nChoose your action\n1.ATTACK\n2.DEFEND\n3.HEAL")
    choice = int(input("Enter either 1 , 2 or 3 : "))
    if choice == 1: # ATTACK
        edamage = random.randint(10,30)
        pdamage = random.randint(10,35)
        eHealth = eHealth - edamage
        pHealth = pHealth - pdamage
        print(f'\n***{player} and {enemy} attacked***\n{player} Health : {pHealth} \n{enemy} Health : {eHealth}')
    elif choice == 2: # DEFEND
        pdamage = random.randint(10,35) // 2 # Damage will be halved
        pHealth = pHealth - pdamage
        print(f'\n***{enemy} attacked, {player} defended***\n{player} Health : {pHealth} \n{enemy} Health : {eHealth}')
    elif choice == 3: # HEAL
        pdamage = random.randint(10,35)
        heal = random.randint(10,25)
        if pHealth + heal > 100:
            pHealth = 100
        else:
            pHealth = pHealth + heal
        print(f'\n***{enemy} attacked and {player} healed***\n{player} Health : {pHealth} \n{enemy} Health : {eHealth}')
    else:
        print("\n***Invalid choice... You Lost a turn***")
    
    turn += 1
    
if pHealth <= 0:
    print(f"\nGame over!!!\n{enemy} won!!!\n")
elif eHealth <= 0:
    print(f"\nGame over!!!\n{player} won!!!\n")
