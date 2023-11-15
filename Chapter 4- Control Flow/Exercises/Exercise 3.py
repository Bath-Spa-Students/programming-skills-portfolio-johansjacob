'''Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

•	 If the alien is green, print a message that the player earned 5 points.

•	 If the alien is yellow, print a message that the player earned 10 points.

•	 If the alien is red, print a message that the player earned 15 points.

•	 Write three versions of this program, making sure each message is printed for the appropriate color alien.'''



alien_color = 'red'

#if alien is green
if alien_color == 'green':
    print("You have earned 5 points!")
#if alien is yellow    
elif alien_color == 'yellow':
    print("You have earned 10 points!")
#if alien is red    
else:
    print("You have earned 15 points!")