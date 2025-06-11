import matplotlib.pyplot as plt
import subprocess
import datetime
from src.food_helper import get_kcal_values

def make_pie():
    date =  datetime.date.today()
    tile_name = "% of Kcal " + str(date) + "!"
    img_name = "images/pie_chart_" + str(date) + ".png"


    # Values for the pie chart
    values = [0.7, 0.2, 0.1]
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
    # try open file
    file = "json/2025-06-11.json"
    # calulate total kcal, fat, carbs, prot.
    values = get_kcal_values(file)
    # return [list]
    # print file values
    #print(f"Total Kcal: [magenta]{totalKcal:.2f}[/],   Fat: [yellow]{totalFat:.2f}[/],   Carbs: [green]{totalCarbs:.2f}[/],   Prot: [cyan]{totalProt:.2f}[/],")
    print(values)

    return [0.5, 0.3, 0.2]