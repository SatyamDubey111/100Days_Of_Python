# in roalercoaster adding ssome extra chagre (do you want photos with ticket)


print("Welcome to the rollercoaster!")
height = int(input('What is your height in cm?  '))

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What isyour age? "))

    if age <= 12:
        bill = 5
        print("please pay %$5")
    elif age <= 18:
        bill = 7
        print("Child ticket pay 7$")
    elif age >= 45 and age <=55:
        print("Every thing is going to be ok. Have a free ride on us!")

    else:
        bill = 12
        print("Adult ticket pay $12")


    wants_photo = input("Do you want to have photo take? type y for yes and n for No.")
    if wants_photo == "Y":
        bill = bill + 3
       #Add 3$ to their bill

    print(f"your final bill is {bill}")

else:
    print("sorry you have to grew taller before you can ride.")
