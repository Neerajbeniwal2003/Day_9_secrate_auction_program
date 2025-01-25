import art_bisding

print(art_bisding.logo)
print("welcome to auction program")


def highest_bidder(bidding_dictionary):
    highest=0
    winner=""
    for i in bidding_dictionary:
        bid_amount=bidding_dictionary[i]
        if bid_amount>highest:
            highest=bid_amount
            winner+=i
    print(f"the winner is {winner} with the highest bid of ${highest}")


logs={}
proceed=True
while proceed:
    name=input("what is your name?:\n").lower()
    bid=int(input("enter your bid amount:\n"))
    logs[name]=bid   
    anyone_left=input("are there any other bidders?type 'yes' or 'no':").lower()
    if anyone_left=="yes":
        proceed=True
        print("\n"*100)
    else:
        proceed=False
        print(f"Bidders are {logs}")
        highest_bidder(logs)
        
        




