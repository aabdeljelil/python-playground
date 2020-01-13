#by Anissa and Pratyusha 
# It's cleaner to put all the imports at the beginning of the file 

import json

# Reads superheroes.json (in this folder)

with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)
	
# prints superheroes

# print(superheroes)
# Creates an empty array called powers
powers = []

# Loop thorough the members of the squad, 
#and append the powers of each to the powers array.
members = superheroes['members']
for member in members: 
	this_members_powers = member['powers']
	powers.append(this_members_powers)

# Prints those powers to the terminal

print(powers)