#This is day 9 project: Silent Auction

from replit import clear
from art import logo
auction_running = True

#define a blank dictionary
bids = {}

while auction_running:
  #Print Welcome Screen
  print(logo)
  print('Welcome to the Silent Auction Program.')

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

print('These are the completed bids: \n')
for person in bids:
  print(person.capitalize())
  print(f'Bid Price: ${bids[person]}\n')


print(f'\n\nThe winner is {highest_bidder.capitalize()} with a bid of ${highest_price}.')


#Link to Day 9 project
#https://replit.com/@Lludu/blind-auction#main.py
