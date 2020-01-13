# by Anissa and Pratyusha 
import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]


with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color', 'length'])


	# Loops through each vegetable 
	for veggie in vegetables:
		veggie_name = veggie['name']
		veggie_color = veggie['color']
		length = len(veggie_name)
		writer.writerow([veggie_name, veggie_color, length])
  

# In the loop, write the name of each vegetable 
# and the color into a CSV called vegetables.csv