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
import os
print(logo)
max=0
data={}
while True:
  name=input("What's your name?: ")
  bid_price=int(input("Your bid price is?: $"))
  data[name]=bid_price
  user = input("Are there any other users who want to bid?:Type 'yes' or 'no':  ")
  if user=="no":
    for price in data:
      if max<data[price]:
        max=data[price]
        highest_bid=price
    # Clearing the Screen
    os.system('cls')    
    print(f"winner is {highest_bid} with the bid of {max}")    
    break    
  else:
    # Clearing the Screen
    os.system('cls')
      
    
    
    
  