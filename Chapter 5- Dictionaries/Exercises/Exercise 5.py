'''Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about 

each pet'''

#creating an empty list to store the pets in.
pets = []

#creating individual pets, and storing each one in the list.
pet = {'animal type': 'dog',
    'name': 'rio',
    'owner': 'John',
    'weight': 20,
    'eats': 'chicken'}
pets.append(pet)

pet = {'animal type': 'lion',
    'name': 'Simba',
    'owner': 'Johan',
    'weight': 50,
    'eats': 'meat'}
pets.append(pet)

pet = {'animal type': 'falcon',
    'name': 'hero',
    'owner': 'Noah',
    'weight': 37,
    'eats': 'fish'}
pets.append(pet)

#displaying the information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")