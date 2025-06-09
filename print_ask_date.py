import json
import sys
from food_helper import print_date_file

arg = sys.argv
if len(arg) > 1:
    print_date_file(arg[1])
else:
    anser = input("(Hit Enter to open date.json) or type in the filename to open: ")
    if anser == "":
        anser = "json/date.json"
    print_date_file(anser)
