print("-----SIMPLE CALCULATOR-----")

#taking numbers as a input for calculation 
num1 = float(input("enter the first number :")) #we taking float datatype as it accepts the decimal numbers also
num2 = float(input("enter the sceond number :"))

#choices for performing arithmatic functions 
print ("Enter 'add' for Addition \nEnter 'sub' for subtraction \nEnter 'multiply' for Multiplication \nEnter 'Divide' for Divison   ")

choice =input("enter your option :")

# now we add conditional statements for this
if choice== "add":
    print ("the sum of the numbers =",num1 + num2)
elif choice == "sub":
    print ("The subraction of the numbers=",num1- num2)
elif choice == "multiply" :
    print ("The multiplication of the numbers=",num1 * num2)
elif choice == "divide":
    print ("THe Divison of the numbers =",num1 / num2)
else:
    print ("invalid choice ")
