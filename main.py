from classes import Weapons, Sword, Bow, Staff

def main():
    sword = Sword("Deathbane")
    bow = Bow("Cupid")
    staff = Staff("Groot")

    while True:
        print("Choose:")
        print("(1) Swing Sword:")
        print("(2) Shoot Bow:")
        print("(3) Shoot Firebal:l")
        choice = input("Choose: ")

# Program Entry Point
if __name__ == "__main__":
    main()