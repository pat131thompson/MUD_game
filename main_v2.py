import game_functions_v2

game_functions_v2.game_intro()
game_functions_v2.character_creation()

# Error checking character creation
if len(game_functions_v2.character_final) == 0:
    print("Oops! Something went wrong!\nPlease start again.")
    quit()
else:
    print(f"Well done!\nYou have created your character!\nYour name is {game_functions_v2.character_final['Name']}.")
    print(f"You are a {game_functions_v2.character_final['Type']}.")
    print(f"Your special ability is : {game_functions_v2.character_final['Equipment']}")


game_functions_v2.save_character()
game_functions_v2.help_screen()
game_functions_v2.place_win_condition()
game_functions_v2.place_enemy()

"""
HINTS
Currently commented out but can be uncommented for game demo purposes.
Were used during the development process.
"""

# print(f"psssst - the toy is located at:\n{game_functions.toy_location}.\n")
# print(f"psssst - the enemy is located at:\n{game_functions.enemy_location}.\n")

game_functions_v2.game_play()
