print("Welcome to the Auction.")
from art import logo
print(logo)
auction={}
choice= True
while choice:
    name=input("Enter your name:")
    price=int(input("Enter the bid price: $"))
    auction[name]=price
    choice = input("Do you want to add another bit: yes or no ?")
    if choice=='yes':
            print("\n"*30)
    else:
            choice=False
highest=0
winner=""
for name in auction:
       if auction[name]>highest:
            highest=auction[name]
            winner=name
print("\n"*30) 

print(f"The winner is {winner} with the bid amount: ${highest}")