# mini lottery
# from random import *

# lucky_number = 57
# random_pick = randint(50, 59)
# print("Your number is:", random_pick)
# if  random_pick != lucky_number:
#     print("Sorry you did not win...")
# else:
#     print("You won a free trip!")

# from random import randint

# counter1 = 0
# counter2 = 0
# answer = input("Want to book a flight??? Enter 'no' to quit: ").lower()
# while answer != 'no':
#     flight_number = randint(1, 2)
#     print("Your flight number is:",flight_number)
#     if flight_number == 1:
#         counter1 +=1
#     else:
#         counter2 +=1
#     answer = input("Want to book a flight??? Enter 'no' to quit: ").lower()   
# print("there are:", counter1, "passangers in flight one")
# print("there are:", counter2, "passangers in flight two")


import random

lucky_number = random.randint(1, 9)
guess_no = int(input("Enter your lucky number: "))
num = 0
while guess_no != lucky_number:
    if guess_no > lucky_number:
        num +=1
        print(guess_no, "Too low!, try again!")
    elif guess_no > lucky_number:
        num +=1
        print(guess_no, "Too high!, try again!")
    # else:
    #     print("Congrats! You got it!")
    # guess_no = int(input("Enter your lucky number: "))
print("Lucky number is:",lucky_number,  guess_no)
