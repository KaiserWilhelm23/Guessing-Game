import random
import sys
import time
import os
import console
from datetime import datetime



def Controls():
    print('Welcome to the guessing game version 0.9.4')
    print('--'*10)
    c2 = print('Press Enter to Start\n')
    input()
    global un
    un = input('please enter a username')
    
    time.sleep(0.4)
    print('--'*10)
    print('HELLO: ', un)
    print('--'*10)
Controls()
    
    
def difficulty():
    print('Difficuty:')
    print('Press e for easy. Press h for Hard. ' )
    c3 = input('Easy, Hard: \n')
    difficulty = 0
    e = 5
    h = 10
    global points
    points = 0
    if c3.lower() == 'e' :
        difficulty = e
        print('Setting to easy')
        time.sleep(0.3)
        clr = console.clear()
        format(clr)
        print('--'*10)
        print('loading........')
        print('--'*10)
        start_time = datetime.now()
        time.sleep(0.4)
    elif c3.lower() == 'h':
        difficulty = h
        print('Setting to hard')
        time.sleep(0.4)
        clr = console.clear()
        format(clr)
        print('--'*10)
        print('loading........')
        print('--'*10)
        start_time = datetime.now()
        time.sleep(0.8)
    
    def restart():
      
      choice = input("Want to play again y/n\n")
      if choice.lower() == "y":
        clr = console.clear()
        format(clr)
        time.sleep(0.1)
        game()
      elif choice.lower() =="n":
        clr = console.clear()
        format(clr)
        time.sleep(0.1)
        print('GOOD BYE, PLAY AGAIN SOON!!')
        print('--'*10)
        end_time = datetime.now()
        
        print('Time of game play: {}'.format(end_time - start_time))
        print('--'*10)
        print('You Finished with ',points, ' points!!')
        sys.exit()
        
    def game():
        clr2 = console.clear()
        format(clr2)
        print('username: ', un)
        global points
        print("The computer can only guess 1-{0}".format(str(difficulty)))
        time.sleep(0.05)
        print('please pick a number')
        num = int(input())
        
        
        
          
        print("your number:",num)
        print('--'*10)
        g = random.randint(1,difficulty)
        print("computers number: ",g)
        print('--'*10)
        print("Try this number next! ",random.randint(1,difficulty))
        print('--'*10)
        
        if num == g:
            print("Good job you won!! :)")
            print('☑️')
            print('--'*10)
            points = points + 1
            print('Points: ', points)
        else:
            print("You lose :(")
            print('❗')
            print('--'*10)
            print('You earned no points.', '   your current points: ', points)
            print('--'*10)
        
        
        
        
        
        
            




        restart()

        


    game()


difficulty()
