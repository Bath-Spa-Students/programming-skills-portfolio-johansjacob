'''Tidy up the code to make it easier to understand

Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed. 

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().'''


#using \t function

x='   Johan\tJacob    '
print(x)

print()

#performing lstrip()
a=x.lstrip()
print(a)

print()

#performing rstrip()
b=x.rstrip()
print(b)

print()

#performing strip()
c=x.strip()
print(c)

print()
print('__________________________________________________')

#using \n function
y='   Johan\n   Jacob    '
print(y)

print()

#performing lstrip()
d=y.lstrip()
print(d)

print()

#performing rstrip()
e=y.rstrip()
print(e)

print()

#performing strip()
f=y.strip()
print(f)

print()