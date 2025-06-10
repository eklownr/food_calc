import matplotlib.pyplot as plt
import subprocess

# Values for the pie chart
values = [0.7, 0.2, 0.1]

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
plt.title('% of Kcal', color='white', weight='bold')

# Save the pie chart to an image file
plt.savefig('pie_chart.png', facecolor=fig.get_facecolor(), edgecolor='none')

# Display the image in the kitty terminal
subprocess.run(["/usr/bin/kitty", "icat", "pie_chart.png"])
