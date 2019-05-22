#1. Defining functions

#def functionName(parameters):
    # statement(s)

"""2. Types of functions"""

#(a)Non-value returning

def compareNumber(a, b):
    if (a>b):
        print("First number is greater than second number")
    elif(a<b):
        print("First number is less than second number")
    else:
        print("First num is equals to second number")


#(b)Value returning

def findAverage(newList):
    numberSum = 0
    for eachNumber in newList:
        numberSum = numberSum + eachNumber
        avg_number = numberSum/len(newList)

    return avg_number

#3. Calling functions

firstNum = int(input("Enter first Number: "))
secondNum = int(input("Enter second Number: "))
compareNumber(firstNum, secondNum)# calling compareNumber function and sending firstNum and secondNum as argument
#compareNumber function is non value returing function

#4. Arguments and parameters

numberList = [34, 66, 72, 88, 18]
newAverage = findAverage(numberList)# calling findAverage function and sending numberList as argument
#findAverage function is value returning function

print("The average of list is:",newAverage)

#Example C: Comparing numbers
    #Write a program to find average of numbers in list
    #===>check file named Example_C.py
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
