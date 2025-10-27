print("choose an operation ")
print("1 -  Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Modulus")


option = int(input("Enter operation: "))  #THE INT IS TO CONVERT STR TO INT AND STORED IN OPTION VARIABLE

if(option in [1,2,3,4,5]):    #CHECKING IF OPTION IS IN THE LIST 1- 5 AND TAKE TWO NUMBERS AS INPUT
    num1 = float(input("Enter first number: "))  #USER FLOAT TO TAKE DECIMAL NUMBERS AS INPUT
    num2 = float(input("Enter second number: "))   
    
    if (option == 1): 
        result = num1 + num2    #if the option is 1 it will add the two numbers
    elif(option == 2):
        result = num1 - num2   #if the option is 2 it will subtract the two numbers
    elif(option == 3):
        result = num1 * num2   #if the option is 3 it will multiply the two numbers 
    elif(option == 4):
        if num2 == 0:
            print("Error: Division by zero")
            result = None
        else:
            result = num1 / num2   #if the option is 4 it will divide the two numbers
    elif(option == 5):
        result = num1 % num2   #if the option is 5 it will find the modulus of the two numbers
else:
    print("Invalid input")  #IF OPTION IS NOT IN THE LIST 1-5 IT WILL PRINT INVALID INPUT
    result = None

if result is not None:
    print("The result of the operation is {}".format(result))  #PRINT THE RESULT ,FORMATTED TO SHOW THE RESULT