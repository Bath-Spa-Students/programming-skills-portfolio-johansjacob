'''Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

* Use a loop to print the name of each river included in the dictionary.

* Use a loop to print the name of each country included in the dictionary.'''


#creating dictionary named rivers containing river names and the country which they flow through
rivers = {'nile': 'egypt',
    'hudson': 'united states',
    'thames': 'united kingdom'}

#loop to print a sentence about each river, such as The Nile runs through Egypt.
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

#loop to print the name of each river included in the dictionary.
print("\nThe following rivers are included in this dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")

#loop to print the name of each country included in the dictionary.
print("\nThe following countries are included in this dictonary:")
for country in rivers.values():
    print(f"- {country.title()}")