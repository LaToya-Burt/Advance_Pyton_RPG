import battle
from characters import the_hero, enemy_one, enemy_two, enemy_three

battle.display_welcome()

battle.attack_phrase(the_hero,enemy_one)
battle.loot_the_loser(the_hero, enemy_one)

battle.attack_phrase(the_hero,enemy_two)
battle.loot_the_loser(the_hero,enemy_two)

battle.attack_phrase(the_hero,enemy_three)
battle.loot_the_loser(the_hero,enemy_three)

battle.the_winner(the_hero)
