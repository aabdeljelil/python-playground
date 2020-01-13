# by Anissa and Pratyusha 
import json
import csv

# Read vegetables.csv (see previous section) into a 
# variable called vegetables.

with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict

#print the variable vegetables

print(rows)

with open('vegetables.json', 'w') as f:
	json.dump(rows, f, indent=4)
	
