while True:
    print('1. Area of the circle')
    print('2. Exit')
    x=eval(input('Enter the choice: '))
    if x==1:
        y=eval(input('Enter the radius: '))
        area=3.14*y*y
        print('Area of circle is:',area)
        print()
    elif x==2:
        print()
        break
    else:
        print('Invalid option')
            