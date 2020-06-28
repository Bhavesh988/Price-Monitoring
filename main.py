from remove import *
import time

class product:
    name: str = None
    price: float = None
    rate:str = None
    def __init__(self,name=None, price=None,rate=None):
        self.name = name
        self.price = price
        self.rate= rate

_new = product()
sender_email = input("Sender's email address:-")
password =input("Enter password:-")
receiver_email=input("Type your email address:-")

n=int(input("Enter 1 for amazon , 2 for Flipcart:-"))
if n==2:
	urla=input('Enter url of product for Flipcart - ')
	while True:
		Flip().find_p(_new,urla,sender_email,receiver_email,password)
		print("\nPrice will be checked every 5 minutes\n")
		time.sleep(300)
elif n==1:
	urlb=input('Enter url of product for Amazon - ')
	while True:
		Amz().find_p(_new,urlb,sender_email,receiver_email,password)
		print("\nPrice will be checked every 5 minutes\n")
		time.sleep(300)

