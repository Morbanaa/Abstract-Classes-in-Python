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
        print("(3) Shoot Firebal:l")
        choice = input("Choose: ")

        match(choice):
            case "1":
                sword.attack()
            case "2":
                bow.attack()
            case "3":
                staff.attack()
            case _:
                continue

# Program Entry Point
if __name__ == "__main__":
    main()