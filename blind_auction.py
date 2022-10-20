from replit import clear
import art

secter_auction = True
print(art.logo)
print("Welcome to the secret auction program.")

def find_highest_bidder(all_bids):
  best_price = 0
  winner = " "
  for names in all_bids:
    price = all_bids[names]
    if best_price < price:
      best_price = price
      winner = names
         
  print(f"The winner is {winner} with a bid of ${best_price}")
  
while secter_auction:
  secter_auction_dict = {}
  name = input("What is your name?: ")
  bids = int(input("What's your bid?: $"))
  secter_auction_dict[name] = bids
  yes_no = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if yes_no == "yes":
    secter_auction = True
    clear()
  else:
    secter_auction = False
    find_highest_bidder(secter_auction_dict)
  
