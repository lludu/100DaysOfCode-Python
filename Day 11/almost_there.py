#import modules
from replit import clear #clears the screen for gameplay, code only used on replit.com
from art import logo
import random

#Card Deck of all Cards, Ace is 11 until player is over 21, Jack, Queen, King are converted to 10
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



#Initial Screen
print(logo)
game_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
clear()


def play_again():
  #define the empy hands of each player
  players_hand = []
  dealers_hand = [] 

  #Main Run
  print(logo)
  player_hit = True
  dealer_hit = True

  dealers_hand = random.sample(card_deck, 2)

  def check_scores():
    if dealers_score > 21:
      print(f"\nYour final hand: {players_hand}, final score: {players_score}")
      print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
      print(f"\nDealer Busted! 🤣")
      play_again()

    elif players_score == dealers_score:
      print(f"\nYour final hand: {players_hand}, final score: {players_score}")
      print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
      print(f"\n😱  Its a Push, No one Wins! 😱")
      play_again()

    elif players_score < dealers_score:
      print(f"\nYour final hand: {players_hand}, final score: {players_score}")
      print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
      print(f"\nDealer Wins! 😰")
      play_again()

    elif players_score > dealers_score and players_score < 21:
      print(f"\nYour final hand: {players_hand}, final score: {players_score}")
      print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
      print(f"\nYou Win! 🤩")
      play_again()

    



  while player_hit:

    if len(players_hand) == 0:
      players_hand += random.sample(card_deck, 2)
    else:
      players_hand += random.sample(card_deck, 1)


    players_score = 0
    for card in players_hand:
      players_score += card

    dealers_score = 0
    for card in dealers_hand:
      dealers_score += card

    print(f"Your cards: {players_hand}, current score: {players_score}")
    print(f"Dealer's first card: {dealers_hand[0]}\n")

    #Check to see if player gets blackjack!
    if players_score == 21 and len(players_hand) == 2 and dealers_score < 21:
      print(f"\nYour final hand: {players_hand}, final score: {players_score}")
      print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
      print(f"\n🤑  You hit 21! Blackjack! Instant Win! 🤑\n")
      player_hit = False
      dealer_hit = False

    #Check to see if a player has blackjack but dealer also has blackjack
    elif players_score == 21 and dealers_score == 21:
      print(f"\nYour final hand: {players_hand}, final score: {players_score}")
      print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
      print(f"\n😱  Its a Push, No one Wins! 😱")
      player_hit = False
      dealer_hit = False
    
    #Check to see if a player busts
    elif players_score > 21:
      print(f"\nYour final hand: {players_hand}, final score: {players_score}")
      print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
      print(f"\nYou Busted! 😭")
      player_hit = False
      dealer_hit = False

    #If blackjack checks and bust checks fail, ask player if they want the next card 
    else:
      hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      print("")
      if hit == 'n':
        player_hit = False


  while dealer_hit:

    if dealers_score == 21 and len(dealers_hand) == 2 and players_score < 21:
      print(f"\nYour final hand: {players_hand}, final score: {players_score}")
      print(f"Dealer's final hand: {dealers_hand}, final score: {dealers_score}")
      print(f"\n🤬  Dealer Hit 21! Blackjack! Dealer Wins!🤬\n")
      dealer_hit = False

    elif dealers_score < 17 and players_score < 21:
      dealers_hand += random.sample(card_deck, 1)
      dealers_score = 0
      for card in dealers_hand:
        dealers_score += card
    

    elif dealers_score < 17 and players_score > 21:
      dealer_hit = False
      check_scores()

    elif dealers_score >= 17:
      dealer_hit = False
      check_scores()

  game_play = input("\nWould you like to play again? Type 'y' or 'n': ").lower()
  if game_play == 'y':
    clear()
    play_again()
    
play_again()