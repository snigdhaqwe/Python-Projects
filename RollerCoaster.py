print("Welcome to the RollerCoaster!")
Height= int(input("Enter your height in cms."))
if Height>=120:
    print("You can ride the RollerCoaster.")
    age=int(input("Enter your age"))
    if(age)<12:
     print("Please pay $5.")
    elif(age)>=18:
     print("Please pay %7")
    else:
     print("Pay $12.")
else:
    print("Sorry, you have to grow taller to ride the RollerCoaster.")
