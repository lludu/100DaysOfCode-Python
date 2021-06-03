#This is day 12 project: Guess The Number


################## IMPORT MODULES #######################

from art import logo, lives
from random import randrange

#Importing clear from Replit.com
try:
    from replit import clear #clears the screen for gameplay, code only used on replit.com
    not_replit = False
except ModuleNotFoundError:
    # Error handling
    not_replit = True
    pass

################## DEFINE FUNCTIONS #######################

def wipe():
  if not_replit:
    print("")
  else:
    clear()
  print(logo)
  print("I'm thinking of a number between 1 and 100.\n")

def check_answer():

  if int(guess) > ANSWER:
    print(f"🔺   {guess} is too high. Guess Again 🔺")
    if life > 0:
      return life - 1
    else:
      return life == 0

  elif int(guess) < ANSWER:
    print(f"🔻   {guess} is too Low. Guess Again 🔻")
    if life > 0:
      return life - 1
    else:
      return life == 0

  else:
    print("error")




################## INITIAL START SCREEN #######################
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")
play_game = True


################## GAME START #######################
while play_game:

  ANSWER = randrange(1,100)
  is_game_over = False
  wrong_choice = True

  #Choose the game type
  # print(f'Psst, the correct answer is {ANSWER}')
  while wrong_choice:
    stage = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if stage == "easy" or stage == "hard":
      wrong_choice = False
    else:
      print("You have typed an invalid answer, please try again.\n")
  wipe()

  #Give lives based on stage
  #due to using a list for lives, subtract one since lists start at 0
  if stage == 'easy':
    life = (10 - 1)
  elif stage == 'hard':
    life = (5 - 1)


  #Run the game
  while not is_game_over:
    print(f"You have {lives[life]} to guess the number.")

    # Check to make sure their answer is a number (do not convert to int yet)
    guess_invalid = True
    while guess_invalid:
      guess = input("Make a guess: ")
      if not guess.isdigit():
        print("That is an invalid guess. Try again. \n")
      else:
        guess_invalid = False

    wipe()

    if int(guess) == ANSWER:
      print(f"😺  😺   You got it! The answer was {ANSWER} 😺  😺")
      print(f"You had {lives[life]} left! Nice Job!")
      is_game_over = True
    elif life == 0:
      print(f"😿  😿   You have ran out of lives, the answer was {ANSWER}, Game Over 😿  😿")
      is_game_over = True
    else:
      life = check_answer()

  replay = input("\nWould you like to play again?\nType 'y' for yes, or 'n' to quit: ")
  if replay == 'y':
    wipe()
  else:
    play_game = False



#Link to Day 10 project
#https://replit.com/@Lludu/Guess-The-Number#main.py

#Link to Day 10 Play game
#https://replit.com/@Lludu/Guess-The-Number?v=1

#Link to Day 10 Fullscreen Game (Embedable File)
#https://replit.com/@Lludu/Guess-The-Number?embed=1&output=1
