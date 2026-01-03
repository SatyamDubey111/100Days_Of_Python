print("Welcome to the rollercoaster!")
height = int(input('What is your height in cm?  '))


if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What isyour age? "))

    if age <= 12:
        print("please pay %$")
    elif age <= 18:
        print("please pay 7$")
    elif age <= 22:
        print("please pay 9$")
  
    else:
        print("Please pay $12")

else:
    print("sorry you have to grew taller brfore you can ride.")
