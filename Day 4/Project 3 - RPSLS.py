#This is day 4 project: Rock Paper Scissors (Added Lizard Spock for more funsies) 
#also added defined a function and ran it (before we were supposed to in our 100 days, but shhh dont tell)



import random

rock_sign = '✊  Rock ⚫️'
paper_sign = '✋  Paper 📃'
scissors_sign = '✌️  Scissors ✂️'
lizard_sign = '🤏  Lizard 🦎'
spock_sign = '🖖  Spock  🖖'

#Introduction
print('Welcome to ✊  Rock, ✋  Paper, ✌️  Scissors, 🤏  Lizard, 🖖  Spock!')
print('''
Rules:
1. Scissors cuts Paper
2. Paper covers Rock
3. Rock crushes Lizard
4. Lizard poisons Spock
5. Spock smashes Scissors
6. Scissors decapitates Lizard
7. Lizard eats Paper
8. Paper disproves Spock
9. Spock vaporizes Rock
(and as it always has) 10. Rock crushes Scissors
''')

game_started = False

def game_play():
  game_started = True
  #Players Choice
  player = input('Please type what you would like to play: ')
  player = player.lower()

  if ((player != 'rock') and (player != 'paper') and (player != 'scissors') and (player != 'lizard') and (player != 'spock')):
    print('You have made an invalid selection, please try again\n')
    game_play()

  #Computers Choice
  choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
  computer = random.choice(choices)


  if (player == 'rock'):
    print(f'\nThe player chose: {rock_sign}')
    if (computer == 'rock'):
      print(f'The computer chose: {rock_sign}')
      print('\nDraw')
    if (computer == 'paper'):
      print(f'The computer chose: {paper_sign}')
      print('\nComputer Wins - Paper Covers Rock')
    if (computer == 'scissors'):
      print(f'The computer chose: {scissors_sign}')
      print('\nPlayer Wins - Rock Crushes Scissors')
    if (computer == 'lizard'):
      print(f'The computer chose: {lizard_sign}')
      print('\nPlayer Wins - Rock Crushes Lizard')
    if (computer == 'spock'):
      print(f'The computer chose: {spock_sign}')
      print('\nComputer Wins - Spock Vaporizes Rock')


  if (player == 'paper'):
    print(f'\nThe player chose: {paper_sign}')
    if (computer == 'rock'):
      print(f'The computer chose: {rock_sign}')
      print('\nPlayer Wins - Paper Covers Rock')
    if (computer == 'paper'):
      print(f'The computer chose: {paper_sign}')
      print('\nDraw')
    if (computer == 'scissors'):
      print(f'The computer chose: {scissors_sign}')
      print('\nComputer Wins - Scissors Cut Paper')
    if (computer == 'lizard'):
      print(f'The computer chose: {lizard_sign}')
      print('\nComputer Wins - Lizard Eats Paper')
    if (computer == 'spock'):
      print(f'The computer chose: {spock_sign}')
      print('\nPlayer Wins - Paper Disproves Spock')


  if (player == 'scissors'):
    print(f'The player chose: {scissors_sign}')
    if (computer == 'rock'):
      print(f'The computer chose: {rock_sign}')
      print('\nComputer Wins - Rock crushes Scissors')
    if (computer == 'paper'):
      print(f'The computer chose: {paper_sign}')
      print('\nPlayer Wins - Scissors Cut Paper')
    if (computer == 'scissors'):
      print(f'The computer chose: {scissors_sign}')
      print('\nDraw')
    if (computer == 'lizard'):
      print(f'The computer chose: {lizard_sign}')
      print('\nScissors Decapitates Lizard')
    if (computer == 'spock'):
      print(f'The computer chose: {spock_sign}')
      print('\nComputer Wins - Spock Smashes Scissors')


  if (player == 'lizard'):
    print(f'The player chose: {lizard_sign}')
    if (computer == 'rock'):
      print(f'The computer chose: {rock_sign}')
      print('\nComputer Wins - Rock Crushes Lizard')
    if (computer == 'paper'):
      print(f'The computer chose: {paper_sign}')
      print('\nPlayer Wins - Lizard Eats Paper')
    if (computer == 'scissors'):
      print(f'The computer chose: {scissors_sign}')
      print('\nComputer Wins - Scissors Decapitates Lizard')
    if (computer == 'lizard'):
      print(f'The computer chose: {lizard_sign}')
      print('\nDraw')
    if (computer == 'spock'):
      print(f'The computer chose: {spock_sign}')
      print('\nPlayer Wins - Lizard Poisons Spock')

  if (player == 'spock'):
    print(f'The player chose: {spock_sign}')
    if (computer == 'rock'):
      print(f'The computer chose: {rock_sign}')
      print('\nPlayer Wins - Spock Vaporizes Rock')
    if (computer == 'paper'):
      print(f'The computer chose: {paper_sign}')
      print('\nComputer Wins - Paper Disproves Spock')
    if (computer == 'scissors'):
      print(f'The computer chose: {scissors_sign}')
      print('\nPlayer Wins - Spock Smashes Scissors')
    if (computer == 'lizard'):
      print(f'The computer chose: {lizard_sign}')
      print('\nComputer Wins - Lizard Poisons Spock')
    if (computer == 'spock'):
      print(f'The computer chose: {spock_sign}')
      print('\nDraw')


  #Replay The Game
  if (game_started == True):
    print('-------')
    replay = input('\n\nWould you like to play again? Yes or No: ')
    replay = replay.lower()

    if (replay == 'yes'):
      print('')
      game_play()
    elif ((replay != 'yes') and (replay != 'no')):
      print('You have typed an incorrect answer, the game will now end. \nThanks for playing!')
    else:
      print('Thanks for playing!')



#Start The Game
game_play()



#Link to Day 4 project
#https://replit.com/@Lludu/rpsls#main.py
#https://replit.com/@Lludu/rpsls?v=1 spotlight
