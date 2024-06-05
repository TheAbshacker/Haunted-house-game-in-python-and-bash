#Fully coded by Ahmed ABS, if you want to use code please give me credits
import sys

def haunted_house():
    def entrance_hall():
        print("You are in the entrance hall. It's dark and musty. There are doors to the left, right, and straight ahead.")
        choice = input("Do you want to go 'left', 'right', or 'straight'? ").strip().lower()
        if choice == 'left':
            library()
        elif choice == 'right':
            kitchen()
        elif choice == 'straight':
            staircase()
        else:
            print("You lost")
            sys.exit()

    def library():
        print("You enter a dusty library filled with old books. There's a flickering candle on the table.")
        choice = input("Do you want to 'examine books', 'take candle', or 'go back'? ").strip().lower()
        if choice == 'examine books':
            print("You find an old book about the history of the house. It's very interesting.")
            library()
        elif choice == 'take candle':
            print("You take the candle. It might be useful later.")
            entrance_hall()
        elif choice == 'go back':
            entrance_hall()
        else:
            print("You lost")
            sys.exit()

    def kitchen():
        print("The kitchen is dirty and smells terrible. There are broken plates everywhere and a strange noise coming from the cupboard.")
        choice = input("Do you want to 'open cupboard', 'search drawers', or 'go back'? ").strip().lower()
        if choice == 'open cupboard':
            print("A ghost jumps out of the cupboard! You run back to the entrance hall.")
            entrance_hall()
        elif choice == 'search drawers':
            print("You find an old, rusty key. It might be useful later.")
            entrance_hall()
        elif choice == 'go back':
            entrance_hall()
        else:
            print("You lost")
            sys.exit()

    def staircase():
        print("You see a grand staircase leading upstairs. The air feels colder here.")
        choice = input("Do you want to 'go upstairs' or 'go back'? ").strip().lower()
        if choice == 'go upstairs':
            hallway()
        elif choice == 'go back':
            entrance_hall()
        else:
            print("You lost")
            sys.exit()

    def hallway():
        print("The hallway is long and has several doors. At the end, there is a window.")
        choice = input("Do you want to 'enter first door', 'enter second door', 'look out window', or 'go downstairs'? ").strip().lower()
        if choice == 'enter first door':
            bedroom()
        elif choice == 'enter second door':
            study()
        elif choice == 'look out window':
            print("You see nothing but darkness outside. It's very eerie.")
            hallway()
        elif choice == 'go downstairs':
            entrance_hall()
        else:
            print("You lost")
            sys.exit()

    def bedroom():
        print("A dusty old bedroom with a large bed. There's something shiny under the bed.")
        choice = input("Do you want to 'look under bed', 'check closet', or 'go back'? ").strip().lower()
        if choice == 'look under bed':
            print("You find a hidden treasure chest! Congratulations, you found the treasure and escaped the haunted house!")
        elif choice == 'check closet':
            print("A ghost jumps out of the closet! You run back to the hallway.")
            hallway()
        elif choice == 'go back':
            hallway()
        else:
            print("You lost")
            sys.exit()

    def study():
        print("A small study room with a desk and a chair. Papers are scattered everywhere.")
        choice = input("Do you want to 'read papers', 'check desk drawer', or 'go back'? ").strip().lower()
        if choice == 'read papers':
            print("You find notes about the haunted house. They are very spooky.")
            study()
        elif choice == 'check desk drawer':
            print("You find a secret map of the house. It might be useful later.")
            hallway()
        elif choice == 'go back':
            hallway()
        else:
            print("You lost")
            sys.exit()

    print("Welcome to the Haunted House Adventure!")
    entrance_hall()

haunted_house()
