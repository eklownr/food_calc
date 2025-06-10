from rich import print
from rich.console import Console
from rich.markdown import Markdown
import subprocess

from food_helper import smal_print_all_food, print_date_file, print_all_food
from run import add_food
from add_food_db import new_food


# Start the app with background image
subprocess.run(["/usr/bin/kitty", "icat", "meat.jpg"])


''' main menu '''
console = Console()
def menu():
    with open("menu.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)


run = True
while run:
    answer = input(" m - menu: ")
    if answer == "q":
        print("Bye")
        run = False
    elif answer == "m":
        menu()
    elif answer == "r":
        # run food app
        add_food()
    elif answer == "k":
        print("Kcal % FAT: FAT * 9 / total_Kcal" )
        print("TODO add matplot funktion to print pie chart")
        import matplot2
    elif answer == "s":
        smal_print_all_food()
    elif answer == "a":
        print_all_food("json/all_food.json")
    elif answer == "d":
        # open file to print to console
        file = input("file to open: ")
        if file == "":
            print_date_file("json/2025-06-09.json")
        else:
            try: 
                print_date_file(file)
            except:
                print(file, "do not exist")
    elif answer == "p":
        # TODO print last week or print all pie chart image
        print_date_file("json/2025-06-09.json")
    elif answer == "n":
        # add new item/food to DB
        new_food()
    elif answer == "j":
        subprocess.run(["/usr/bin/kitty", "icat", "meat.jpg"])
    else:
        print("wrong value: q - quit; m - menu")
