#importing some necessary modules for the program
import random 
import string 
print ("----PASSWORD GENERATOR----")
def main_func():
# taking desired input from the user
    length = int (input("Enter the desired length of password :"))

 # Introducing character sets for generating the password  
    uppercase_data = string.ascii_uppercase
    lowercase_data = string.ascii_uppercase
    numerical_data = string.digits
    symbols_data = string.punctuation

 # Combining all the  character sets
    combine = lowercase_data + uppercase_data + numerical_data + symbols_data
   
   #generating a random password according to the derired length
    random_password = random.sample(combine, length)
    password = "".join(random_password)

    print ("Generated password",password) #print the generated paasword to the console
    main_func()#for calling the function recursively

#  call the main function to start the program  
main_func()    
 