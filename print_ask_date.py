import json
from food_helper import print_date_file

anser = input("(Hit Enter to open date.json) or type in Filename to open: ")
if anser == "":
    anser = "json/date.json"
print_date_file(anser)
