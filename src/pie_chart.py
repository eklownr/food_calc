import matplotlib.pyplot as plt
import subprocess
import datetime
from rich import print
from src.food_helper import get_kcal_values

def make_pie():
    date =  datetime.date.today()
    tile_name = "% of Kcal " + str(date) + "!"
    img_name = "images/pie_chart_" + str(date) + ".png"


    # Values for the pie chart
    values = get_pie_values()

    # Labels for the pie chart
    labels = ['Fat', 'Protein', 'Carbs']

    # Create the pie chart
    fig, ax = plt.subplots()

    # Set the background color to black
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')

    # Create the pie chart with custom text properties
    wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

    # Set the text color and font weight to white and bold
    for text in texts:
        text.set_color('white')
        text.set_weight('bold')

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_weight('bold')

    # Title with white bold text
    plt.title(tile_name, color='white', weight='bold')

    # Save the pie chart to an image file
    plt.savefig(img_name, facecolor=fig.get_facecolor(), edgecolor='none')

    # Display the image in the kitty terminal
    subprocess.run(["/usr/bin/kitty", "icat", img_name])


def get_pie_values() -> list:
    ''' open todays json-file, return Kcal % of Fat, Carbs and protein and print it out'''

    # TODO try open file if exist, else return a fix value
    file = "json/2025-06-08.json"

    # get total Kcal, Fat, Carbs and Protein in gram
    v = get_kcal_values(file)
    # Calculate % of Kcal
    fat = v[1]*9/v[0]
    carbs =  v[2]*4/v[0]
    prot =  v[3]*4/v[0]

    print("values from file: ", file)
    print(f"Total g Kcal: [magenta]{v[0]:.2f}[/],   Fat: [yellow]{v[1]:.2f}[/]g,   Carbs: [green]{v[2]:.2f}[/]g,   Prot: [cyan]{v[3]:.2f}[/]g,")
    print(f"Total % Kcal: [magenta]{v[0]:.2f}[/],   Fat: [yellow]{fat*100:.2f}[/]%,   Carbs: [green]{carbs*100:.2f}[/]%,   Prot: [cyan]{prot*100:.2f}[/]%,")

    return [fat, carbs, prot]