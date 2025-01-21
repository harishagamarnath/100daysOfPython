import sys

print("*******Welcome to Carnival rides********")
height = int(input("please provide your height in centimeter"))
bill_amount=0

if height<121:
    print("you are not eligible for the ride")
    sys.exit()
else:
    print("you are eligible for the ride")
    age = int(input("please provide your age"))
    if age<12:
        bill_amount+=5
    elif 12 <= age < 18:
        bill_amount=7
    elif age>=18:
        bill_amount=12
        if 45 <= age <= 55:
            bill_amount=0
    else:
        print("entered age is incorrect, please restart the program")
        sys.exit(0)

    photos = input("do you want photos Y/N: ")

    if photos == 'Y':
        bill_amount += 3
        if 45 <= age <= 55:
            bill_amount = 0

print(f"your total bill is ${bill_amount}")
