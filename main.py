from rich import print
from run import add_food
from rich.console import Console
from rich.markdown import Markdown

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
    else:
        print("wrong value: q - m - r")
