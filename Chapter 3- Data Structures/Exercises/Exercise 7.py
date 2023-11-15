'''Think of at least five places in the world you’d like to visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.

•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

•	 Use sorted() to print your list in alphabetical order without modifying the actual list.

•	 Show that your list is still in its original order by printing it.

•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

•	 Show that your list is still in its original order by printing it again.

•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.

•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.'''


#list of five place I want to visit
place=['Spain','United Kingdom','Netherlands','Sweden','France']
print(place)
print()

print('__________________________________________________________________________________')
print()

#sorting the list of places in alphabetical order
s_place=sorted(place)
print(s_place)
print()

print('__________________________________________________________________________________')
print()

#showing that the initial order of the list has not changed
print(place)
print()

print('__________________________________________________________________________________')
print()

#using reverse() function the reverse the elements in the list of places
place.reverse()
print(place)
print()

print('__________________________________________________________________________________')
print()

#reversing the list of places back to its original order
place.reverse()
print(place)
print()

print('__________________________________________________________________________________')
print()

#using sort() function to sort the elements in the list of places in alphabetical order
place.sort()
print(place)
print()

print('__________________________________________________________________________________')
print()

#using sort() function to sort the elements in the list of places in reverse alphabetical order
place.sort(reverse=True)
print(place)
print()

print('__________________________________________________________________________________')
print()
