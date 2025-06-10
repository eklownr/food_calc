from rich import print
from run import add_food
from rich.console import Console
from rich.markdown import Markdown
from food_helper import smal_print_all_food, print_date_file
import subprocess

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
        add_food()
    elif answer == "a":
        smal_print_all_food()
    elif answer == "w":
        file = input("file to open: ")
        if file == "":
            print_date_file("json/2025-06-09.json")
        else:
            try: 
                print_date_file(file)
            except:
                print(file, "do not exist")
    elif answer == "p":
        print_date_file("json/2025-06-09.json")
    elif answer == "j":
        subprocess.run(["/usr/bin/kitty", "icat", "meat.jpg"])
    else:
        print("wrong value: q - quit; m - menu")
