#This is day 9 project: Silent Auction

from replit import clear
from art import logo

new_auction = True

while new_auction:
  auction_running = True

  #define a blank dictionary
  bids = {}

  #Ask what we are bidding on
  print(logo)
  print('Welcome to the Blind Auction Program.')
  item = input("What is the item up for bid?: ")
  show_bidders = input("\nShould we disclose all bids at the end of the auction?\nType 'yes' or 'no': ").lower()
  clear()


  while auction_running:
    #Print Welcome Screen
    print(logo)
    print('Welcome to the Blind Auction Program.')
    print(f'We are currently bidding on: {item}')
    if show_bidders == 'yes' or show_bidders == 'y':
      print('Bids will be disclosed at the end\n')
    else:
      print('Bids will NOT be disclosed at the end\n')

    #get dictionary key and value from user
    name = input("What is your name: ").lower()
    bid_amount = int(input("What is your bid: $"))

    #add to dictionary, name_of_dictionary[key] = value
    bids[name] = bid_amount

    #ask for other bidders
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    #check to end auction_running
    if other_bidders == 'yes' or other_bidders == 'y':
      clear()
    else:
      clear()
      auction_running = False


  #check highest bid
  highest_bidder = ""
  highest_price = 0
  for person in bids:
    #person = name of the bidder, the KEY, the key gets looped
    #bids[person] = bidding amount of the bidder
    if highest_price < bids[person]:
      highest_price = bids[person]
      highest_bidder = person

  print(logo)
  if show_bidders == 'yes' or show_bidders == 'y':
    print('These are the completed bids: \n')

    bidder_number = 0
    for person in bids:
      bidder_number += 1
      print(f'Bidder #{bidder_number}: {person.capitalize()}')
      print(f'Bid Price: ${bids[person]}\n')


  print(f'The winner of the {item} is {highest_bidder.capitalize()} with a bid of ${highest_price}.')

  continue_auction = input("\n\nWould you like to auction another item?\nType 'yes' or 'no': ")

  if continue_auction != 'yes' and continue_auction != 'y':
    new_auction = False
    clear()
    print(logo)
    print('Thanks for bidding!')
  else:
    clear()


#Link to Day 9 project
#https://replit.com/@Lludu/blind-auction#main.py
