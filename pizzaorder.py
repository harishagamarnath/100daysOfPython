import sys

print("welcome to pizza shop\nplease help us with your order")

price = 0
i = 0

for i in range(3):
    size = input("do you want L M or S: ")
    size = size.upper()
    if size == "L":
        price = 10
        break
    elif size == "M":
        price = 8
        break
    elif size == "S":
        price = 6
        break
    else:
        if i==2:
            print("you have entered incorrect size mulitple time, exiting the program")
            sys.exit(0)
        else:
            print("please enter the correct size")

pepperoni = input("do you need pepperoni: Y/N ")
pepperoni = pepperoni.upper()
if pepperoni == "Y":
    price += 1

extra_cheese = input("do you need extra cheese: Y/N ")
extra_cheese = extra_cheese.upper()
if extra_cheese == "Y":
    price += 2

print(f"your total bill is {price}")
