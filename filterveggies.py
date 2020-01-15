# by Anissa and Pratyusha 
import csv
import json

#Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows] 

#Loop through vegetables and filter down 
#to only green vegtables using a whitelist.
# set the filter to color = green
green_vegetables = []
for veggie in vegetables:
    if veggie['color'] == 'green':
        green_vegetables.append(veggie)
#Print veggies to the terminal
#print(green_vegetables)
#Write the veggies to a json file called greenveggies.json
with open('green_vegetables.json', 'w') as f:
    json.dump(green_vegetables, f, indent=2)
# Bonus: Output another csv called green_vegetables.csv.