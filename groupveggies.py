# by Anissa and Pratyusha 
import csv
import json
from pprint import pprint
# Read vegetables.csv into a variable called vegtables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows] 

#Group vegetables by color as a variable vegetables_by_color.
vegetables_by_color = {}
for veg in vegetables:
    veg_color = veg['color']
    if veg_color in vegetables_by_color:
        vegetables_by_color[veg_color].append(veg)
    else:
        vegetables_by_color[veg_color] = [veg]

#pprint(vegetables_by_color)
#Output vegetables_by_color into a json 
#called vegetables_by_color.json.
with open('groupveggies.json', 'w') as f:
    json.dump(vegetables_by_color, f, indent=2)
