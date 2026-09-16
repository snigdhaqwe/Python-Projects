# Find the greatest of 3 numbers
num1=int(input("Enter a number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if(num1 > num2 and num1 > num3):
    print("num1 is the largest number")
elif(num2 > num1 and num2 > num3):
    print("num2 is the largest number")
else:
    print("Num3 is the largest number")
