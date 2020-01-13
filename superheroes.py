#by Anissa and Pratyusha 
# It's cleaner to put all the imports at the beginning of 
#the file 

import json
import csv

# Read superheroes.json (in this folder)

with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)
	
# print(superheroes)
# Creates an empty array called powers
# powers = []

# Write a header to the CSV file
with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	headers = ['name', 'age', 'secretIdentity', 
		'powers', 'squadName', 'homeTown', 'formed', 
		'secretBase', 'active']
	writer.writerow(headers)

	# Loop thorough the members of the squad, 
	#and append the powers of each to the powers array.
	members = superheroes['members']
	for member in members: 

		# Define variables 
		name = member['name']
		age = member['age']
		secret_identity = member['secretIdentity']
		powers = member['powers']
		squad_name = superheroes['squadName']
		home_town = superheroes['homeTown']
		formed = superheroes['formed']
		secret_base = superheroes['secretBase']
		active = superheroes['active']

		# Writes all of the headers in a table in a csv file
		row = [name, age, secret_identity, powers, squad_name,home_town,formed,secret_base,active]
		writer.writerow(row)
