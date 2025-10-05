# RPG Mini Battle Simulator

import random

enemy = random.choice(['dragon','goblin','troll','kobold','skeleton'])
player = input("\nEnter your name: ")
pHealth = 100
eHealth = 100
turn = 1
print("\nRPG Mini Battle\n****************")
print(f"{player} vs {enemy}\n")
print(f"{player} Health : {pHealth} \n{enemy} Health : {eHealth} ")
while eHealth >= 0 and pHealth >= 0:
    print("\nTURN ",turn)
# AttackByPlayer
    edamage = random.randint(10,30)
    eHealth = eHealth - edamage
    print(f"{enemy} health after attack by {player}: ",eHealth)
# AttackByEnemy
    pdamage = random.randint(10,35)
    pdamage = pdamage // 2  # Defend
    pHealth = pHealth - pdamage
    print(f"{player} health after attack by {enemy}: ",pHealth)   
# Heal(Restores player health):
    pheal = random.randint(10,25)
    if pHealth + pheal < 100:
        pHealth = pHealth + pheal
    else:
        pHealth = 100
    print(f"{player} health after heal : ",pHealth)
    turn += 1
if pHealth <= 0:
    print(f"\nGame over!!!\n{enemy} wins!!!\n")
elif eHealth <= 0:
    print(f"\nGame over!!!\n{player} wins!!!\n")
