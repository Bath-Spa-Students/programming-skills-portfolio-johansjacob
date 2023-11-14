'''You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.'''

#Exercise 4

name=['Iman','Ehsan','Ahmad']

print('I would like to invite you ',name[0],' for dinner')
print()

print('I would like to invite you ',name[1],' for dinner')
print()

print('I would like to invite you ',name[2],' for dinner')
print()

print('__________________________________________________________________________________')
print()

#Exercise 5

#print statement for the guest who cannot make it to dinner

print(name[1],'Would not be able to make it for dinner')
print()

print('__________________________________________________________________________________')
print()

#New invitation list for dinner

new_name=['Iman','Ahmad','Khalid']

#Resending invitation using new list

print('I would like to invite you ',new_name[0],' for dinner')
print()

print('I would like to invite you ',new_name[1],' for dinner')
print()

print('I would like to invite you ',new_name[2],' for dinner')
print()

print('__________________________________________________________________________________')
print()

print('Unfortunamtely, I can only accomodate 2 guests for dinner.')
print()

new_list=new_name.pop(2)

#Guest whose invitation would be cancelled and message of apology for cancellation of invite
print('I am sorry', (new_list), 'to cancel your invitation for the dinner due to accomodating issues')
print()

#New updated list
print(new_name)
print()

print('__________________________________________________________________________________')
print()

#Informing the other 2 that they are still invited for dinner
print('I would like to let you know that you ',new_name[0],'are still invited for dinner')
print()

print('I would like to let you know that you ',new_name[1],'are still invited for dinner')
print()

print('__________________________________________________________________________________')
print()

#deleting the names in my list to have an empty list
del new_name[:]
print(new_name)
print()

print('__________________________________________________________________________________')
print()