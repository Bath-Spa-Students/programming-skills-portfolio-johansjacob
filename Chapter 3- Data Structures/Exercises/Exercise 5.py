'''You just heard that one of your guests can't make the
dinner, so you need to send out a new set of invitations. You'll have to think of
someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.'''

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




