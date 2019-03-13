# This is very simple program written in Python language . 

print("Here is my First assignment in Python, a Simple calulator")

nbr1= int(input("Enter First Value="))
nbr2= int(input("Enter Second Value="))

# Funtion definitions

def addition(val1, val2):
    result=val1+val2
    return result
def subtraction(val1, val2):
    result=val1-val2
    return result
def multiplication(val1, val2):
    result=val1*val2
    return result
def division(val1, val2):
    result=val1/val2
    return result

# This  section is about  selection of Operator

print("Select operation as following")
print("Enter 1 for Add")
print("Enter 2 for Subtract")
print("Enter 3 for Multiply")
print("Enter 4 for Divide")
# Take input from the user for operation selection
 
select = input("Enter choice(1/2/3/4):")
if select == '1':
         print(nbr1,"+",nbr2,"=", addition(nbr1,nbr2))
elif select == '2':
         print(nbr1,"-",nbr2,"=", subtraction(nbr1,nbr2))
elif select == '3':
         print(nbr1,"*",nbr2,"=", multiplication(nbr1,nbr2))
elif select == '4':
         print(nbr1,"/",nbr2,"=", division(nbr1,nbr2))
else:
         print("You selected wrong option")
