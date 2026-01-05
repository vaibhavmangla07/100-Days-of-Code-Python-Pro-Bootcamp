logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def find(bidding_dict):
    winner = ""
    highest_bid = 0
    max(bidding_dict)

    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is : {winner}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("Enter Your Name : ")
    price = int(input("Enter your bid amount ($) : "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.").lower()

    if should_continue == "no":
        continue_bidding = False
        find(bids)
    elif should_continue == "yes":
        print("\n" * 20)
