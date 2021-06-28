#import modules

#Importing clear from Replit.com
try:
    from replit import clear #clears the screen for gameplay, code only used on replit.com
    not_replit = False
except ModuleNotFoundError:
    # Error handling
    not_replit = True
    pass

#Import other modules
from art import logo, vs
from game_data import data, test
import random

def wipe():
  '''Clears the screen if replit, if not adds 100 new lines to "clear the screen"'''
  if not_replit:
    print('\n'*100)
  else:
    clear()
  print(logo)


play_game = True

print(f'{logo}\n')
print("Gameplay:\n\nIn this game you are asked who has the most followers on instagram.")
print("Your job is to guess out of the two (A or B) who has more.")
print("If you choose correctly you are award a point and the game continues!\n")
input('Press [Enter] to start the game!')
wipe()


while play_game:

  #set default game variables
  selection_a = random.choice(data)
  score = 0
  game_over = False
  
  #Check to see that the random choices dont match
  while not game_over:
    bad_selection = True
    while bad_selection:
      selection_b = random.choice(data)
      if selection_a == selection_b:
        selection_b = random.choice(data)
      else:
        bad_selection = False

    #set answer to selection a
    answer = selection_a
    
    print(f'\n\nRound {score+1}:')
    print(f"Compare A: {answer['name']}, a {answer['description']} from {answer['country']}.\n")
    print(f"VS:\n")
    print(f"Compare B: {selection_b['name']}, a {selection_b['description']} from {selection_b['country']}.\n")
    
    #⬇️Testing Code⬇️
    # print(f"psst, its {answer['follower_count']} vs {selection_b['follower_count']}")
    #⬆️Testing Code⬆️
    
    
    ##Check to make sure user has made a valid input
    valid = False
    while not valid:
      guess = input("Who has more instagram followers? Type 'A' or 'B': ").capitalize()

      if guess == 'A':
        chosen = answer
        valid = True
      elif guess == 'B':
        chosen = selection_b
        valid = True
      else:
        print("That is not a valid option, try again\n")



    #Wipe the board for results
    wipe()

    #User Chose A, was wrong
    if chosen["follower_count"] == answer["follower_count"] and answer["follower_count"] < selection_b["follower_count"]:
      print(f"\nSorry, thats wrong! Final score: {score}\n")
      print(f"{answer['name']} has {answer['follower_count']} followers")
      print(f"{selection_b['name']} has {selection_b['follower_count']} followers")
      game_over = True

    #User Chose B, was wrong
    elif chosen["follower_count"] == selection_b["follower_count"]  and answer["follower_count"] > selection_b["follower_count"]:
      print(f"\nSorry, thats wrong! Final score: {score}\n")
      print(f"{answer['name']} has {answer['follower_count']} followers")
      print(f"{selection_b['name']} has {selection_b['follower_count']} followers")
      game_over = True

    #User chose a, was right
    elif chosen["follower_count"] == answer["follower_count"] and answer["follower_count"] > selection_b["follower_count"]:
      score += 1
      print(f"\nYou are right! current score: {score}\n")
      print(f"{answer['name']} has {answer['follower_count']} followers")
      print(f"{selection_b['name']} has {selection_b['follower_count']} followers")
      correct = True

    #User chose b, was right
    elif chosen["follower_count"] == selection_b["follower_count"] and answer["follower_count"] < selection_b["follower_count"]:
      score += 1
      print(f"\nYou are right! current score: {score}\n")
      print(f"{answer['name']} has {answer['follower_count']} followers")
      print(f"{selection_b['name']} has {selection_b['follower_count']} followers")
      correct = True

    
    #Check to see if user is continuing to play the game
    if 
    elif correct:
      selection_a = chosen
    else:
      game_over = True






  #Ask if user wants to play a second game
  replay = input("\nWould you like to play again?\nType 'y' for yes, or 'n' to quit: ")
  if replay == 'y':
    wipe()
  else:
    play_game = False

