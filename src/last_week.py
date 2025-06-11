import os
from food_helper import get_kcal_values

path = '../json'
json_files = [j for j in os.listdir(path) if j.endswith('.json') and j.startswith('2025')]
print(json_files)
json_files.sort()
print(json_files)
if len(json_files) < 1:
    print("No files this week.")
    #return

for file in json_files:
    f = "../json/" + file
    list_of_values = get_kcal_values(f)
    print(f, "have values: ", list_of_values)


