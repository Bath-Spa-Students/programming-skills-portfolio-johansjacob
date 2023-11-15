'''Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
'''

#same glossary dictionary modified by adding five more keys and values
glossary = {'if': 'This condition can be any expression that evaluates to either True or False',
            'elif': 'it is used to include multiple conditional expressions after the if condition or even in between if and else conditions. ',
            'else': 'it is used in conditional if statements, and decides what to do if the condition is False.',
            'print': 'it is used to display a ceratin messge or call out a variable',
            'input':'it helps the user to input the values',
            'dictionary': 'A collection of key-value pairs.',
            'key': 'The first item in a dictionary.',
            'value': 'An item associated with a key in a dictionary.',
            'float': 'A numerical value with a decimal point.',
            'boolean values': 'It consists of True or False.'}

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")