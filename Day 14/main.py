#import modules

#Importing clear from Replit.com
try:
    from replit import clear  #clears the screen for gameplay, code only used on replit.com
    not_replit = False
except ModuleNotFoundError:
    # Error handling
    not_replit = True
    pass

#Import other modules
from art import logo, vs
from game_data import data
import random


def wipe():
    '''Clears the screen if replit, if not adds 100 new lines to "clear the screen"'''
    if not_replit:
        print('\n' * 100)
    else:
        clear()
    print(logo)


play_game = True

print(f'{logo}\n')
print("Gameplay:\n\nIn this game you are asked who has the most followers on instagram.")
print("Your job is to guess out of the two 🅰️  or 🅱️  who has more.")
print("If you choose correctly you are award a point and the game continues!\n")
input('Press [Enter] to start the game!')
wipe()

while play_game:

    #set default game variables
    a = random.choice(data)
    score = 0
    game_over = False

    #Check to see that the random choices dont match
    while not game_over:
        bad_selection = True
        while bad_selection:
            b = random.choice(data)
            if a == b:
                b = random.choice(data)
            else:
                bad_selection = False

        print(f'\nRound {score+1}:')
        print(
            f"Compare 🅰️ : {a['name']}, a {a['description']} from {a['country']}.\n"
        )
        print(f"{vs}:\n")
        print(
            f"Compare 🅱️ : {b['name']}, a {b['description']} from {b['country']}.\n"
        )

        #⬇️Testing Code⬇️
        # print(f"psst, its 🅰️  {a['follower_count']} vs 🅱️  {b['follower_count']}")
        #⬆️Testing Code⬆️

        ##Check to make sure user has made a valid input
        valid = False
        while not valid:
            guess = input(
                "\nWho has more instagram followers? Type '🅰️ ' or '🅱️ ': "
            ).capitalize()

            if guess == 'A' or guess == '🅰️':
                chosen = a
                valid = True
            elif guess == 'B' or guess == '🅱️':
                chosen = b
                valid = True
            else:
                print("That is not a valid option, try again\n")

        #Wipe the board for results
        wipe()



        #User Chose A, was wrong
        if chosen["follower_count"] == a["follower_count"] and a["follower_count"] < b["follower_count"]:
            print(f"\n😭   Sorry, thats wrong! Final score: {score}   😭\n")
            print(f"🅰️  {a['name']} has {a['follower_count']} million followers")
            print(f"🅱️  {b['name']} has {b['follower_count']} million followers")
            game_over = True

        #User Chose B, was wrong
        elif chosen["follower_count"] == b["follower_count"] and a["follower_count"] > b["follower_count"]:
            print(f"\n😭   Sorry, thats wrong! Final score: {score}   😭\n")
            print(f"🅱️  {b['name']} has {b['follower_count']} million followers")
            print(f"🅰️  {a['name']} has {a['follower_count']} million followers")
            game_over = True

        #User chose a, was right
        elif chosen["follower_count"] == a["follower_count"] and a["follower_count"] > b["follower_count"]:
            score += 1
            print(f"\n🤩  You are right! Current score: {score} 🤩")
            correct = True

        #User chose b, was right
        elif chosen["follower_count"] == b["follower_count"] and a["follower_count"] < b["follower_count"]:
            score += 1
            print(f"\n🤩  You are right! Current score: {score} 🤩")
            correct = True



        #Check to see if user is continuing to play the game
        if correct and score > 10 and chosen['name'] == data[0]["name"]:
            print('\n🤣  😅   You have reached the max level for this game!🤣  😅')
            game_over = True
        elif correct and score > 99:
            print('\nYou won level 💯 , you should take a break now! Goodbye!')
            game_over = True
        elif correct:
            a = chosen
        else:
            game_over = True

    #Ask if user wants to play a second game
    replay = input(
        "\nWould you like to play again?\nType 'y' for yes, or 'n' to quit: ")
    if replay == 'y':
        wipe()
    else:
        play_game = False