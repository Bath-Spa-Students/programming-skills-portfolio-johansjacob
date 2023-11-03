'''A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.'''

#Number of USB sticks the girl wants
x=50

#Cost of 1 USB stick
y=6

#Number of USB sticks she can buy
z=x/y
print('Number of USB stick she can buy: ',round(z))

print()

#Amount of pounds she has left
a=x-y*round(z)
print('The amount of pounds she has left after the purchase is:',a)

