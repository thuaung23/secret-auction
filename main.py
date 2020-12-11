# This program uses a python function, Dictionary.
# Written by: Thu Aung
# Written on: Dec 10, 2020

from replit import clear

print("Welcome to the Blind Auction")
# Create an empty dictionary.
auction_dict = {}

game_on = True
while game_on:

  # Get the users' names.
  name = input("What is your name?\n").capitalize()
  # Get the bidding amount.
  bid = int(input("What will be your bid amount?\n$"))
  # Add names as keys and bidding amounts as values.
  auction_dict[name] = f'${bid}'

  # Check for more bidders.
  bidders = input("Are there more bidders? Yes or No\n").capitalize()

  if bidders == 'Yes':
    # Clear the screen so that the previous bid is hidden.
    clear()

  elif bidders == 'No':
    # If no more bidders, get the max bid amount.
    max_bid = max(auction_dict, key = auction_dict.get)
    print(f"The highest bidder is {max_bid} with {auction_dict[max_bid]}.")
    # Stop the loop.
    game_on = False

  # In case a user typed in anything else other than 'yes' or 'no'.
  else:
    print("Sorry. I don't understand.\nBye.")
    break

print(auction_dict)
