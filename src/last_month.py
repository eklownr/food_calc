import os
from src.food_helper import get_kcal_values
from datetime import datetime, timedelta

def get_this_month():
    # Get today's date
    today = datetime.today().date()
    print("Today:", today)
    
    # Subtract 7 days
    seven_days_ago = today - timedelta(days=7)
    print("7 days ago:", seven_days_ago)
    
    path = 'json'
    json_files = [j for j in os.listdir(path) if j.endswith('.json') and j.startswith('2025')]
    print(json_files)
    json_files.sort()
    print(json_files)
    if len(json_files) < 1:
        print("No files this week.")
        #return
    
    for file in json_files:
        f = "json/" + file
        list_of_values = get_kcal_values(f)
        print(f, "have values: ", list_of_values)


