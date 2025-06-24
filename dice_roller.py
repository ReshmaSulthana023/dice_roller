import random
import os
import time

def dice_roll():
    print("---The result displays in---")
    display = ['5','4','3','2','1','0']

    for text in display:
        print(text,end="\r")
        time.sleep(1)
    
    dice_no = random.randint(1,6)
    print("The result is ",dice_no)

def clear_terminal():
    os.system('cls' if os.name=='nt' else 'clear') 


while True:
    input("Press Enter to roll the dice : ")
    clear_terminal()
    dice_roll()

    choice = input("Do you wanna play again?\nEnter y/n: ")
    if(choice.lower()!='y'):
        print("Thanks for playing!")
        break
