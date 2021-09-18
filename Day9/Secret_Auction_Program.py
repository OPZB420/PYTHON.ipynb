##   
##       Secret Auction Program



bids = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and Bid amount is ${bid_amount}")
    
    
    

bidding_finished = False

while not bidding_finished:
    name = input("Enter your name: ")
    price = int(input("Enter your Bid Amount: $"))
    bids[name] = price
    should_continue = input("Are there any other Bidder? type 'yes' or 'no': \n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)

