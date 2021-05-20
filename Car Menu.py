
def menu():
    print('Main Menu:')
    print(' 1. Cost of Gas')
    print(' 2. Used Value')
    print(' 3. Stopping Distance')
    print (' 4. Quit')
    print()
    print()
    r=2
    while r>1:
        user=int(input('Choose a function from the list:\n'))
        if (user == 1) or (user==2) or (user==3) or (user==4):
            r=1
        else:
            print('Please enter a number between 1 and 4.')
            r=2
    return user

def mileage():
    i=2
    while i>1:
      car1=int(input("Enter car 1's mileage:"))
      car2=int(input("Enter car 2's mileage:"))
      gas1=float(input("Enter car 1's average gas cost per gallon:"))
      gas2=float(input("Enter car 2's average gas cost per gallon:"))
      mile=int(input('How many miles do you drive a month:'))
      if (car1 or car2 or gas1 or gas2 or mile1) < 0:
          print('Please enter a positive value')
          print()
          i=2
      else:
          i=1
    cost1=((mile*12)*gas1)/car1
    cost2=((mile*12)*gas2)/car2
    if cost1>cost2:
        save=cost1-cost2
        print('Car 1 will save','%0.2f' %(save),'in a year')
        print()
    elif cost2>cost1:
        save=cost2-cost1
        print('Car 2 will save','%0.2f' %(save),'in a year')
        print()
    elif cost2==cost1:
        print('The two cars cost the same')
        print()

def value():
    i=2
    while i>1:
        original=int(input('Enter original car price:'))
        years=int(input('Enter number of years:'))
        price=original
        if (original or years) < 0:
            print('Please enter a positive value.')
            print()
            i=2
        else:
            i=1
    for i in range(years):
        price=price*.82
        dice=('%0.2f' %(price))
        print('Year', i+1,'value: $%s' %(dice) )
    print()
def stop():
    i=2
    while i>1:
        speed=int(input('Enter initial speed:'))
        condition=int(input('Enter tire condition (1 = new, 2 = good 3 = poor) '))
        if (speed or condition) < 0:
            print('Please enter a positive value.')
            print()
            i=2
        else:
            i=1
    v=(speed*(5280/3600))**2
    if condition == 1:
        distance=((v)/(2*0.8*32.174))
        tire='new tires'
    if condition == 2:
        distance=((v)/(2*0.6*32.174))
        tire='good tires'
    if condition == 3:
        distance=((v)/(2*0.5*32.174))
        tire='poor tires'
    print('At','%0.1f'%(speed),'miles per hour','%s,' %(tire),'the car will stop in', '%0.2f' %(distance), 'feet away')
    print()
def quit():
  i=4
  while i<5:
    break
v=menu()


if v == 1:
  t=mileage()
  v=menu()
if v == 2:
  z=value()
  v=menu()
if v == 3:
  x=stop()
  v=menu()
if v == 4:
  b=quit()
    
