import os
import platform
import time
from classes import Weapons, Sword, Bow, Staff

def main():
    # Creates objects for later use
    sword = Sword("Deathbane")
    bow = Bow("Cupid")
    staff = Staff("Groot")

    # Prints user options
    while True:
        print("Choose:")
        print("(1) Swing Sword:")
        print("(2) Shoot Bow:")
        print("(3) Shoot Firebal:")
        print("(4) End Program:")
        choice = input("Choose: ")

        match(choice):
            case "1":
                sword.attack()
            case "2":
                bow.attack()
            case "3":
                staff.attack()
            case "4":
                clear_screen()
                break
            case _:
                clear_screen()
                continue

        time.sleep(2) # Creates deley for more natrual feel
        clear_screen()


# Resets console after each update
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# Program Entry Point
if __name__ == "__main__":
    main()

    # Final Message
    print("Thanks for playing!\n")