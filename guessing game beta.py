#Guessing game BETA 2020
import random
import sys

def restart():
    choice = input("Want to play again y/n\n")
    if choice.lower() == "y":
        game()
    elif choice.lower() =="n":
        sys.exit()

def game():
        print("The computer can only guess 1-2000")
        print('please pick a number')

        num = input()

        print("your number:",num)
        print("____________________")

        print("computers number: ",random.randint(1,2000))
        print("____________________")
        print("Try this number next!",random.randint(1,2000))

        print("_______________________________________________")
        print('Powerd by python 3.6')
        print('Version BETA')
        restart()

game()



#copyright 2020 Will Payne all rights reserved.
