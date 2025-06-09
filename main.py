from rich import print
from run import add_food
from menu import TestApp

run = True
while run:
    answer = input(" 'q' - quit\n 'm' - menu\n 'r' - run_foodApp: ")
    if answer == "q":
        print("Bye")
        run = False
    elif answer == "m":
        # menu
        app = TestApp()
        app.run()

    elif answer == "r":
        # Run food app
        add_food()
    else:
        print("wrong value: q - m - r")
