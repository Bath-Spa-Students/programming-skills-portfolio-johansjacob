'''A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

their meanings as values.

* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

each word-meaning pair in your output.'''

#creating a dictionary consisting of five programming words learnerd in previous chapters
glossary = {'if': 'This condition can be any expression that evaluates to either True or False','elif': 'it is used to include multiple conditional expressions after the if condition or even in between if and else conditions. ','else': 'it is used in conditional if statements, and decides what to do if the condition is False.','print': 'it is used to display a ceratin messge or call out a variable','input':'it helps the user to input the values' }

word = 'if'
print(f"\n{word.title()}: {glossary[word]}")

word = 'elif'
print(f"\n{word.title()}: {glossary[word]}")

word = 'else'
print(f"\n{word.title()}: {glossary[word]}")

word = 'print'
print(f"\n{word.title()}: {glossary[word]}")

word = 'input'
print(f"\n{word.title()}: {glossary[word]}")