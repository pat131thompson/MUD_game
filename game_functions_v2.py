"""
Main file for game functions and classes.
For each function or class created, docstrings will be within those functions / classes.
For each variable not part of a function or class - a single comment precedes.
"""

# Relevant module imports
import json
import random

# main while loop for game running.
game_is_running = True

# Dictionary of map rooms (4 x 4 grid) with nested dictionary of room descriptions and options.
map_main = {
    'a1': {
        'GAME_MAP': 'Lobby to building',
        'RM_DESC': 'You are in an entrance lobby.\nA siren is sounding.\nThere is a door in front of you and to your '
                   'right.',
        'FORWARD': 'b1',
        'BACK': '',
        'LEFT': '',
        'RIGHT': 'a2',
        'TOY': False,
        'ENEMY': False
    },
    'a2': {
        'GAME_MAP': 'Cloak room',
        'RM_DESC': 'Coats and hats hang on pegs.\nPapers lay on the floor as if people left in a hurry.',
        'FORWARD': 'b2',
        'BACK': '',
        'LEFT': 'a1',
        'RIGHT': 'a3',
        'TOY': False,
        'ENEMY': False
    },
    'a3': {
        'GAME_MAP': 'Bin store',
        'RM_DESC': 'There are bins full of papers and food cartons.\nDrops of slime fall from one of the bins...',
        'FORWARD': 'b3',
        'BACK': '',
        'LEFT': 'a2',
        'RIGHT': 'a4',
        'TOY': False,
        'ENEMY': False
    },
    'a4': {
        'GAME_MAP': 'Garage',
        'RM_DESC': 'A bike is on the floor and a car left with the doors open.\nA trail of goo runs across the floor '
                   'to the far door.',
        'FORWARD': 'b4',
        'BACK': '',
        'LEFT': 'a3',
        'RIGHT': '',
        'TOY': False,
        'ENEMY': False
    },
    'b1': {
        'GAME_MAP': 'Reception desk',
        'RM_DESC': 'A desk is in front of you.  You hear a whimper!\nA receptionist is curled under the desk.\nThey '
                   'mutter "SLIME" over and over!',
        'FORWARD': 'c1',
        'BACK': 'a1',
        'LEFT': '',
        'RIGHT': 'b2',
        'TOY': False,
        'ENEMY': False
    },
    'b2': {
        'GAME_MAP': 'Printing room',
        'RM_DESC': 'A printer is printing paper...\nThe words repeat "HELP! SLIME!"',
        'FORWARD': 'c2',
        'BACK': 'a2',
        'LEFT': 'b1',
        'RIGHT': 'b3',
        'TOY': False,
        'ENEMY': False
    },
    'b3': {
        'GAME_MAP': 'An office space',
        'RM_DESC': 'Tables are over-turned and chairs knocked over!',
        'FORWARD': 'c3',
        'BACK': 'a3',
        'LEFT': 'b2',
        'RIGHT': 'b4',
        'TOY': False,
        'ENEMY': False
    },
    'b4': {
        'GAME_MAP': 'An office space',
        'RM_DESC': 'The room is a mess. A phone line is beeping and a computer is smashed.\nThere is a note on a desk '
                   'saying "GET OUT WHILE YOU CAN!"',
        'FORWARD': 'c4',
        'BACK': 'a4',
        'LEFT': 'b3',
        'RIGHT': '',
        'TOY': False,
        'ENEMY': False
    },
    'c1': {
        'GAME_MAP': 'Kitchen area',
        'RM_DESC': 'A burning pork shop is the cause of the smoke!\nAn office worker cowers in the corner, '
                   'unsure whether to rescue their dinner or to flee!',
        'FORWARD': 'd1',
        'BACK': 'b1',
        'LEFT': '',
        'RIGHT': 'c2',
        'TOY': False,
        'ENEMY': False
    },
    'c2': {
        'GAME_MAP': 'Toilet block',
        'RM_DESC': 'The room stinks of poo! Toilet doors are open...\nWater is flooding as the toilets are blocked by '
                   'slime!',
        'FORWARD': 'd2',
        'BACK': 'b2',
        'LEFT': 'c1',
        'RIGHT': 'c3',
        'TOY': False,
        'ENEMY': False
    },
    'c3': {
        'GAME_MAP': 'An office space',
        'RM_DESC': 'The tables are covered in sticky slime...\nA person shaped blob of goo is under a table!!',
        'FORWARD': 'd3',
        'BACK': 'b3',
        'LEFT': 'c2',
        'RIGHT': 'c4',
        'TOY': False,
        'ENEMY': False
    },
    'c4': {
        'GAME_MAP': 'Lounge area',
        'RM_DESC': 'A couch and a TV are over turned!\nThe TV is running a news program about Alien Slime!',
        'FORWARD': 'd4',
        'BACK': 'b4',
        'LEFT': 'c3',
        'RIGHT': '',
        'TOY': False,
        'ENEMY': False
    },
    'd1': {
        'GAME_MAP': 'Meeting room',
        'RM_DESC': 'A large table is in the middle of the room with chairs all around.\nA radio from a firefighter is '
                   'making noises asking if someone is OK!',
        'FORWARD': '',
        'BACK': 'c1',
        'LEFT': '',
        'RIGHT': 'd2',
        'TOY': False,
        'ENEMY': False
    },
    'd2': {
        'GAME_MAP': 'Manager\'s office',
        'RM_DESC': 'The manager works here...he should be in charge!\nYou see a cupboard door move - The manager is '
                   'hiding inside!!!',
        'FORWARD': '',
        'BACK': 'c2',
        'LEFT': 'c1',
        'RIGHT': 'c3',
        'TOY': False,
        'ENEMY': False
    },
    'd3': {
        'GAME_MAP': 'Computer room',
        'RM_DESC': 'Lots of computers buzz and whir.  They give off a lot of heat!\nA gross smell of sizzling slime '
                   'from slime in a computer is in the air!',
        'FORWARD': '',
        'BACK': 'c3',
        'LEFT': 'd2',
        'RIGHT': 'd4',
        'TOY': False,
        'ENEMY': False
    },
    'd4': {
        'GAME_MAP': 'Supply room',
        'RM_DESC': 'Spare paper, pens and stickers are in here.\nA post-it note on the wall says "No Stealing!"',
        'FORWARD': '',
        'BACK': 'c4',
        'LEFT': 'd3',
        'RIGHT': '',
        'TOY': False,
        'ENEMY': False
    }
}

# Variable which will change as players move through the map.  References 1st key in map_main nested dictionary.
direction_choice = 'a1'

# Starting location on the map from which player will commence game.
current_location = map_main[direction_choice]['GAME_MAP']

# Empty dictionary within which character creation data will be held
character_final = {}

# Empty string latterly used in deployment of toy to be rescued.
toy_location = ''

# Empty string latterly used in deployment of enemy.
enemy_location = ''

# Win boolean values
player_wins_game = False
enemy_wins_game = False

# Series of variables accessed in the creation of a character object
character_type = ["Firefighter", "Slime"]
character_name = [""] 
firefighter_equip = ["Axe", "Torch"]
slime_equip = ["Huge tentacle", "Super slime vision"]
character_location = current_location


# Score board dictionary to hold score data for leaderboard save.
score_board = {
    'Player Score': 0,
    'Enemy Score': 0
}


def game_intro():
    """
    ASCII art header followed by general welcome text and introduction to character creation.
    """
    print('''
  ______ _           __ _       _     _            
 |  ____(_)         / _(_)     | |   | |           
 | |__   _ _ __ ___| |_ _  __ _| |__ | |_ ___ _ __ 
 |  __| | | '__/ _ \  _| |/ _` | '_ \| __/ _ \ '__|
 | |    | | | |  __/ | | | (_| | | | | ||  __/ |   
 |_|  __|_|_|  \___|_| |_|\__, |_| |_|\__\___|_|   
 \ \ / / __|               __/ |                   
  \ V /\__ \              |___/                    
   \_/_|___/                                       
  / ____| (_)                                      
 | (___ | |_ _ __ ___   ___                        
  \___ \| | | '_ ` _ \ / _ \                       
  ____) | | | | | | | |  __/                       
 |_____/|_|_|_| |_| |_|\___| ''')
    print("\nWelcome to Firefighter vs. Slime!")
    print("\nYour mission is to rescue the trapped toy....or to slime it!!")
    print("\nGood luck!")
    print("\nYour first task is to create your character...")


class Character:
    """
    Character class - results in the character object which the player will
    play the game with.  Guides the player through the character creation
    process using the options contained in previously noted variables.
    Exception handling is built in to ensure character creation can be completed
    correctly.
    """
    def __init__(self):
        character_valid = False
        equipment_valid = False
        while not character_valid:
            self.char_type = ""
            char_type = input(
                "Play as Firefighter or Slime?\nPress 'F' for Firefighter;\nPress 'S' for Slime;\n").lower()
            try:
                if char_type == "f":
                    self.char_type = character_type[0]
                    print("You are the brave Firefighter!")
                    character_final["Type"] = character_type[0]
                    character_valid = True
                elif char_type == "s":
                    self.char_type = character_type[1]
                    print("You are the stinky Slime!")
                    character_final["Type"] = character_type[1]
                    character_valid = True
            except KeyError:
                print("Invalid entry, please try again!")
        self.name = ""
        char_name = input("What do you want to call your character?\n").title()
        character_final["Name"] = char_name
        print(f"Well {char_name}, you have a toy to find!\nTo help your quest, please choose your equipment.")
        while not equipment_valid:
            self.ff_equip = ""
            if self.char_type == character_type[0]:
                ff_equip = input(
                    "What equipment will you take?\nPress 'A' for an axe.\nPress 'T' for a torch.\n").lower()
                try:
                    if ff_equip == "a":
                        character_final["Equipment"] = firefighter_equip[0]
                        equipment_valid = True
                    elif ff_equip == "t":
                        character_final["Equipment"] = firefighter_equip[1]
                        equipment_valid = True
                except KeyError:
                    print("Invalid entry, please try again!")
            self.s_equip = ""
            if self.char_type == character_type[1]:
                s_equip = input("What equipment will you take?\nPress 'T' for a Giant Tentacle.\nPress 'V' for Super "
                                "Slime Vision.\n").lower()
                try:
                    if s_equip == "t":
                        character_final["Equipment"] = slime_equip[0]
                        equipment_valid = True
                    elif s_equip == "v":
                        character_final["Equipment"] = slime_equip[1]
                        equipment_valid = True
                except KeyError:
                    print("Invalid entry, please try again!")
        self.location = character_final["Location"] = current_location


def character_creation():
    """
    Function created to guide player through character creation.
    Gives the option to load a previously saved character.
    If this is not selected - questions guide the player through the character creation process.
    Character (loaded or created) is saved in the character_final dictionary
    """
    global character_final
    global current_location
    load_char = input("Would you like to load a previous character?\nPress 'Y' for Yes.\nPress 'N' for No.\n").lower()
    if load_char == "y":
        with open('my_char_save.txt') as save_file_one:
            character_load = save_file_one.read()
            character_final = json.loads(character_load)
    else:
        Character()


def save_character():
    """
    Save process once character completion is completed.
    """
    save = input("Would you like to save your progress?\nType 'Y' for yes.\nType 'N' for no.\n").lower()
    if save == "y":
        with open('my_char_save.txt', 'w') as save_file_one:
            save_file_one.write(json.dumps(character_final))
        print("Well done!\nYou have saved your progress!")
    else:
        return


def help_screen():
    """
    Help screen - displays game map and advises of next player course of action.
    """
    print('''
    #####################
    HELP AND INSTRUCTIONS
    #####################

    You have been gifted a map to the area you are about to explore.

         -------------------------
        |     |     |     |     |
     D  |     |     |     |     |
        |     |     |     |     |
        -------------------------
        |     |     |     |     |
     C  |     |     |     |     |
        |     |     |     |     |
        -------------------------
        |     |     |     |     |
     B  |     |     |     |     |
        |     |     |     |     |
        -------------------------
        |     |     |     |     |
     A  |     |     |     |     |
        |     |     |     |     |
        -------------------------
           1     2     3     4''')
    print("\nThe toy is found somewhere in this map.")
    print("\nYou are in square A1.")
    print("\nYour game options will appear as you progress through the map.")
    print("\nGood Luck!\n")


def place_win_condition():
    """
    Places the 'toy' (win condition) in a random room within the top quarter of the map.
    This ensures the player must travers the length of the map before being able to win.
    """
    global toy_location
    rand_num = random.randint(1, 4)
    if rand_num == 1:
        toy_location = map_main['d1']['GAME_MAP']
        return map_main['d1']['TOY'] == True
    elif rand_num == 2:
        toy_location = map_main['d2']['GAME_MAP']
        return map_main['d2']['TOY'] == True
    elif rand_num == 3:
        toy_location = map_main['d3']['GAME_MAP']
        return map_main['d3']['TOY'] == True
    else:
        toy_location = map_main['d4']['GAME_MAP']
        return map_main['d4']['TOY'] == True


def place_enemy():
    """
    Places the enemy within the third row of the map (precluding C1 which requires an ability).
    This ensures there is a chance the player will encounter the enemy on their route to the win condition.
    """
    global enemy_location
    rand_num = random.randint(1, 3)
    if rand_num == 1:
        enemy_location = map_main['c2']['GAME_MAP']
        return map_main['c2']['ENEMY'] == True
    elif rand_num == 2:
        enemy_location = map_main['c3']['GAME_MAP']
        return map_main['c3']['ENEMY'] == True
    else:
        enemy_location = map_main['c4']['GAME_MAP']
        return map_main['c4']['ENEMY'] == True


def combat():
    """
    Combat module - combat is via a 2D6 roll of dice (player gets a + 2 bonus)
    Win = game continues
    Draw - combat continues
    Loss = game over
    """
    global game_is_running
    global enemy_location
    global enemy_wins_game
    combat_happening = True
    while combat_happening:
        print("You and your enemy circle each other as you fight!")
        print("You both strike out!")
        print(f"{character_final['Name']} - you will roll two digital dice and add 2 to the score as you surprised "
              f"your enemy!")
        print("Your enemy will then roll two digital dice.")
        print("The highest score wins!")
        player_roll = random.randint(2, 12)
        player_roll = player_roll + 2
        enemy_roll = random.randint(1, 12)
        print(f"{character_final['Name']}, you scored {player_roll}!")
        print(f"Your enemy scored {enemy_roll}!")
        if player_roll > enemy_roll:
            print(f"{character_final['Name']}, you have beaten your enemy!\nThey are stunned.\nYou are free to move!")
            enemy_location = ''
            combat_happening = False
        elif enemy_roll > player_roll:
            print(f"{character_final['Name']}, you have been beaten by your enemy!")
            print("GAME OVER!!!!")
            enemy_wins_game = True
            leaderboard(score_board['Player Score'], score_board['Enemy Score'])
            save_leaderboard()
            combat_happening = False
            game_is_running = False
        else:
            print("You both defended against each other.  The fight continues!")


def leaderboard(player_score, enemy_score):
    """
    Updates the score_board dictionary and also prints the score to the console.
    """
    global score_board
    if player_wins_game:
        player_score += 1
        print(f"\nThe final game score is:\nPlayer: {player_score}\nEnemy: {enemy_score}")
        score_board.update({'Player Score': player_score})
        score_board.update({'Enemy Score': enemy_score})
    elif enemy_wins_game:
        enemy_score += 1
        print(f"\nThe final game score is:\nPlayer: {player_score}\nEnemy: {enemy_score}")
        score_board.update({'Player Score': player_score})
        score_board.update({'Enemy Score': enemy_score})


def save_leaderboard():
    """
    Saves the score_board dictionary to the existing score txt file
    """
    with open("leaderboard.txt", "w") as save_file_two:
        save_file_two.write((json.dumps(score_board)))


def game_play():
    """
    Main game play function for moving around the map and engaging with the rooms.
    Includes the combat function within and also the win condition trigger which can end the game.
    """
    global character_final
    global game_is_running
    global direction_choice
    global current_location
    global player_wins_game
    global score_board
    while game_is_running:
        with open('leaderboard.txt') as save_file_two:
            scoreboard_load = save_file_two.read()
            score_board = json.loads(scoreboard_load)
        print(f"{character_final['Name']}, Your current location is:-\n{current_location}.")
        if current_location == toy_location:
            print("You have found the toy!!!!\nYou win the game!!!")
            player_wins_game = True
            leaderboard(score_board['Player Score'], score_board['Enemy Score'])
            save_leaderboard()
            game_is_running = False
        elif current_location == enemy_location:
            if character_final['Type'] == "Firefighter":
                print("You have walked in on your enemy, the Evil Slime!\nPrepare to fight!")
                combat()
            else:
                print("You have walked in on your enemy, the Firefighter!\nPrepare to fight!")
                combat()
        elif current_location == map_main['b3']['GAME_MAP']:
            print("A door ahead of you is blocked by a large table.")
            if character_final["Equipment"] == "Huge tentacle" or character_final["Equipment"] == "Axe":
                print("You use your special power to break down the obstacle!")
                movement_choice = input("Please press:-\n'F' for FORWARD\n'B' for BACKWARD\n'L' for LEFT\n'R' for "
                                        "RIGHT\n").lower()
                if movement_choice == "f":
                    direction_choice = map_main[direction_choice]['FORWARD']
                    current_location = map_main[direction_choice]['GAME_MAP']
                elif movement_choice == "b":
                    direction_choice = map_main[direction_choice]['BACK']
                    current_location = map_main[direction_choice]['GAME_MAP']
                elif movement_choice == "l":
                    direction_choice = map_main[direction_choice]['LEFT']
                    current_location = map_main[direction_choice]['GAME_MAP']
                elif movement_choice == "r":
                    direction_choice = map_main[direction_choice]['RIGHT']
                    current_location = map_main[direction_choice]['GAME_MAP']
            else:
                print("You have no way of moving this obstacle and can not move forward.")
                movement_choice = input("Please press:-\n'B' for BACKWARD\n'L' for LEFT\n'R' for "
                                        "RIGHT\n").lower()
                if movement_choice == "b":
                    direction_choice = map_main[direction_choice]['BACK']
                    current_location = map_main[direction_choice]['GAME_MAP']
                elif movement_choice == "l":
                    direction_choice = map_main[direction_choice]['LEFT']
                    current_location = map_main[direction_choice]['GAME_MAP']
                elif movement_choice == "r":
                    direction_choice = map_main[direction_choice]['RIGHT']
                    current_location = map_main[direction_choice]['GAME_MAP']
        elif current_location == map_main['c1']['GAME_MAP']:
            print("An oven is on and the room is hot.\nSome smoke is making the room dark and slime is covering the "
                  "light making it hard to see!")
            if character_final["Equipment"] == "Torch" or character_final["Equipment"] == "Super slime vision":
                print("You are able to use your special power to see clearly through the room!")
                look_around = input(
                    "Would you like to explore this area further?\nType 'Y' for YES or type 'N' for NO:-\n").lower()
                if look_around == "y":
                    print(f"You explore and note:-\n{map_main[direction_choice]['RM_DESC']}.")
                else:
                    print("You look no further...")
                print("Where would you like to move next?")
                movement_choice = input(
                    "Please press:-\n'F' for FORWARD\n'B' for BACKWARD\n'L' for LEFT\n'R' for RIGHT\n").lower()
                if movement_choice == "f":
                    direction_choice = map_main[direction_choice]['FORWARD']
                    current_location = map_main[direction_choice]['GAME_MAP']
                elif movement_choice == "b":
                    direction_choice = map_main[direction_choice]['BACK']
                    current_location = map_main[direction_choice]['GAME_MAP']
                elif movement_choice == "l":
                    direction_choice = map_main[direction_choice]['LEFT']
                    current_location = map_main[direction_choice]['GAME_MAP']
                elif movement_choice == "r":
                    direction_choice = map_main[direction_choice]['RIGHT']
                    current_location = map_main[direction_choice]['GAME_MAP']
            else:
                print("You are confused by your sudden loss of sight and you stumble around the room until you "
                      "encounter a random door!\nYou have no idea which way you are going!")
                random_room = random.randint(1, 3)
                if random_room == 1:
                    direction_choice = map_main[direction_choice]['RIGHT']
                    current_location = map_main[direction_choice]['GAME_MAP']
                elif random_room == 2:
                    direction_choice = map_main[direction_choice]['BACK']
                    current_location = map_main[direction_choice]['GAME_MAP']
                else:
                    direction_choice = map_main[direction_choice]['FORWARD']
                    current_location = map_main[direction_choice]['GAME_MAP']
        else:
            look_around = input(
                "Would you like to explore this area further?\nType 'Y' for YES or type 'N' for NO:-\n").lower()
            if look_around == "y":
                print(f"You explore and note:-\n{map_main[direction_choice]['RM_DESC']}.")
            else:
                print("You look no further...")
            print("Where would you like to move next?")
            movement_choice = input(
                "Please press:-\n'F' for FORWARD\n'B' for BACKWARD\n'L' for LEFT\n'R' for RIGHT\n").lower()
            if (movement_choice == "f") and (len(map_main[direction_choice]['FORWARD']) > 0):
                direction_choice = map_main[direction_choice]['FORWARD']
                current_location = map_main[direction_choice]['GAME_MAP']
            elif (movement_choice == "b") and (len(map_main[direction_choice]['BACK']) > 0):
                direction_choice = map_main[direction_choice]['BACK']
                current_location = map_main[direction_choice]['GAME_MAP']
            elif (movement_choice == "l") and (len(map_main[direction_choice]['LEFT']) > 0):
                direction_choice = map_main[direction_choice]['LEFT']
                current_location = map_main[direction_choice]['GAME_MAP']
            elif (movement_choice == "r") and (len(map_main[direction_choice]['RIGHT']) > 0):
                direction_choice = map_main[direction_choice]['RIGHT']
                current_location = map_main[direction_choice]['GAME_MAP']
            else:
                print("You can't go that way - please try again!")
