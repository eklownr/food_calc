from rich import print
from rich.console import Console
from rich.markdown import Markdown
import subprocess

from food_helper import smal_print_all_food, print_date_file
from run import add_food
from add_food_db import new_food

subprocess.run(["/usr/bin/kitty", "icat", "meat.jpg"])

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
    elif answer == "a":
        smal_print_all_food()
    elif answer == "w":
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
