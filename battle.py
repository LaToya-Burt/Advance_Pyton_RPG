
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
    print(f"{hero['name']} attacks {enemy ['name']}")
    hero_attacks= random.choice (hero['attacks'][0])
    print(enemy['health'])
    #enemy['health'] -= hero_attacks(1)
    #print(f"{enemy['name']} was attacked by {hero['name']} for {hero_attacks [1]} damage leaving {enemy['name']} {enemy ['health']} health remaining.")   
    print(hero_attacks[0])
    print(hero_attacks[1])











#while hero ["health"]>0 and enemy["health"]>0: