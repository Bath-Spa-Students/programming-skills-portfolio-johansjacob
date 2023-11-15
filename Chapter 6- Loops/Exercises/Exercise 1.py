'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.'''

#creating a prompt for the user 
x = "\nWhat topping would you like on your pizza?"
x += "\nEnter 'quit' when you are finished: "
        
#creating a loop 
while True:
    topping = input(x)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break