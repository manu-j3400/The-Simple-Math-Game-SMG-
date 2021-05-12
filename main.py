import time, os, mathOperations
import mathIntroAnimation

Red = "\033[0;31m"
Green = "\033[0;32m"
White = "\033[0;37m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
red_back = "\033[0;41m"
grey_back = "\033[0;40m"
off = "\003[0;0m"


def clear():
    os.system('clear')


#Intro
def introAndStart():
    option = input(red_back + "[SELECT YOUR DIFFICULT: EASY, MEDIUM, HARD, EXTREME]\n" + white)
    print(red + "_____________________________________\n")
    if option == "EASY":
        #CODE
    elif option == "MEDIUM":
        #CODE
    elif option == "HARD":
        #CODE
    elif option == "EXTREME":
        #CODE

def countdown():
    print("5...")
    time.sleep(1)
    print("4...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    print("______________________________\n")
    clear()


if __name__ == "__main__":
    mathIntroAnimation.introAnimation()
    introAndStart()
    countdown()
    mathOperations.mathFunctions()
