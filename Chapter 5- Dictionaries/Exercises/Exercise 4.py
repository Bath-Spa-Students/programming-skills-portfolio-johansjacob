'''Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

* Use a loop to print the name of each river included in the dictionary.

* Use a loop to print the name of each country included in the dictionary.'''

rivers = {'nile': 'egypt',
    'hudson': 'united states',
    'thames': 'united kingdom'}

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this dictonary:")
for country in rivers.values():
    print(f"- {country.title()}")