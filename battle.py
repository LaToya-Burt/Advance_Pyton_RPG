import time
import random 

#funtions needs to be for hero to pic a random attack
# funtion for enemy to pic an attack 

def display_welcome():
    greeting=""" Welcome to the Battle Royal"""
    print(greeting )
    print ("")
    instructions= "The hero, Mom, will be fighting her three enemy children. Who will reign supreme, lets check it out."
    print(instructions)
    print("")
 

def attack_phrase(hero,enemy):
    while hero['health'] > 0 and enemy['health'] > 0:
        time.sleep(1)
        print()
        print(f"{hero['name']} attacks {enemy ['name']}")
        hero_attacks= random.choice (hero['attacks'])
        # print(enemy['health']) health value
        enemy['health'] -= hero_attacks[1]
        if enemy['health'] < 0: # any action need after the hero dies would go in the scope of this if
            # pickup_enemy_item(hero,enemy) this would be an example of a step that needs to hapen if the enemy dies
            enemy['health'] = 0
        print(f"""{enemy['name']} was attacked by {hero['name']} for {hero_attacks[1]} damage
        leaving {enemy['name']} {enemy ['health']} health remaining.""")   
        # print(hero_attacks[0]) # attack name
        # print(hero_attacks[1]) # attack damage
        if enemy['health'] > 0:
            print()
            print(f"{enemy ['name']} attacks {hero['name']}")
            enemy_attacks = random.choice(enemy['attacks'])
            hero['health'] -= enemy_attacks[1]
            if hero['health'] < 0:  # any action need after the hero dies would go in the scope of this if
                hero['health'] = 0
            print(f"""{hero['name']} was attacked by {enemy['name']} for {enemy_attacks[1]} damage
            leaving {hero['name']} {hero['health']} health remaining.""")











