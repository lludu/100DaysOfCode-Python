#This is day 11 project: BlackJack

#import modules
from replit import clear #clears the screen for gameplay, code only used on replit.com
from art import logo
import random


#Initial Screen
play_game = True
print(logo)
game_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
clear()
print(logo)

#Create the deal card function
def deal_card():
  '''Deals 1 Card from the card deck, Ace is 11 until player is over 21.\n
     Jack, Queen, and King are converted to 10'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  #draw the random card from the deck
  card = random.choice(cards)
  #return the chosen card as the output of deal_card function
  return card


def calculate_score(cards):
  #Calculate scores
  '''Calculate the total of the cards in the players hand'''
  #Check to see if anyone has blackjack, return a zero?
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  #Check to see if the ace needs to become a 1 instead of 11
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(players_score, dealers_score):

  #Check to see if its a push
  if players_score == dealers_score:
    print(f"Your cards: {players_hand}, current score: {players_score}")
    print(f"Dealer's cards: {dealers_hand}, current score: {dealers_score}\n")
    print("😱  Push! It's a tie!  😱")

  #Check to see if play got blackjack
  elif players_score == 0:
    print(f"Your cards: {players_hand}, current score:  🤑    BLACKJACK 21  🤑")
    print(f"Dealer's cards: {dealers_hand}, current score: {dealers_score}\n")
    print("🤑    Blackjack! Instant Win!  🤑")

  #Check to see if dealer got blackjack
  elif dealers_score == 0:
    print(f"Your cards: {players_hand}, current score: {players_score}")
    print(f"Dealer's cards: {dealers_hand}, current score:  🤬    BLACKJACK 21  🤬\n")
    print('🤬    Dealer got Blackjack! Instant Loss!  🤬')

  #Check to see if player bust
  elif players_score > 21:
    print(f"Your cards: {players_hand}, current score: {players_score}")
    print(f"Dealer's cards: {dealers_hand}, current score: {dealers_score}\n")
    print('You Busted!  😭')

  #Check to see if dealer bust
  elif dealers_score > 21:
    print(f"Your cards: {players_hand}, current score: {players_score}")
    print(f"Dealer's cards: {dealers_hand}, current score: {dealers_score}\n")
    print('Dealer Busted!  🤣')

  #Check to see if player wins
  elif players_score > dealers_score:
    print(f"Your cards: {players_hand}, current score: {players_score}")
    print(f"Dealer's cards: {dealers_hand}, current score: {dealers_score}\n")
    print('You Win!  🤩')

  #Check to see if dealer wins
  elif players_score < dealers_score:
    print(f"Your cards: {players_hand}, current score: {players_score}")
    print(f"Dealer's cards: {dealers_hand}, current score: {dealers_score}\n")
    print('Dealer Wins  😰')

  else:
    print('🐞  🐞    Looks like there was an unexpected bug! Please try again! 🐞  🐞')
    print('Please report how this happened to andrew@andrewjash.com!')


while play_game:
  #Create the dealer and players hands
  players_hand = []
  dealers_hand = []

  #Define the game over flag
  is_game_over = False

  #Give two cards to each player
  for _ in range(2):
    players_hand.append(deal_card())
    dealers_hand.append(deal_card())

  #Calculate the scores of both players
  players_score = calculate_score(players_hand)
  dealers_score = calculate_score(dealers_hand)

  if players_score == 0:
    print(f"Your cards: {players_hand}, current score: 21")
  else:
    print(f"Your cards: {players_hand}, current score: {players_score}")
  print(f"Dealer's first card: {dealers_hand[0]}\n")

  #See if anyone has blackjack or if player busts, then set game over flag to true
  if players_score == 0 or dealers_score == 0 or players_score > 21:
    is_game_over = True

  while not is_game_over and players_score < 21:
    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    print("")
    if hit == 'y':
      players_hand.append(deal_card())
      players_score = calculate_score(players_hand)
      print(f"Your cards: {players_hand}, current score: {players_score}")
      print(f"Dealer's first card: {dealers_hand[0]}\n")
    else:
      while dealers_score < 17:
        dealers_hand.append(deal_card())
        dealers_score = calculate_score(dealers_hand)
      is_game_over = True

  compare(players_score, dealers_score)

  replay = input("\nWould you like to play again? Type 'y' for yes, or 'n' to quit: ")
  if replay == 'y':
    clear()
    print(logo)
  else:
    play_game = False


#Link to Day 11 project code
#https://replit.com/@Lludu/Blackjack#main.py

#Link to Day 11 project game
#https://replit.com/@Lludu/Blackjack?v=1

#Link to Day 11 Full Screen game
#https://replit.com/@Lludu/Blackjack?embed=1&output=1#main.py
