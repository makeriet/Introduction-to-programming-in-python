#1. Sequential control flow

#2. Indentation
#3. Selection control flow
    #if, else, Else If (elif)

x = 12
y = 6
if (x == y):

    print("x is equal to y")

elif (x>y):
    print("x is greater than y")
else:
    print("x is  equal to y")

# == equals to
# != not equals to
# < less than
# > greater than
# >= less or equals to
# <= greater or equals to

#4. Iterative control flow
    #while loop

number = 0
while(number<10):
    print(number)
    number = number + 1


# Example B: Guess the number game

guessNumber = 67
attempt = 1

while(attempt<=3):
    numberFromUser = int(input("Enter the number: "))
    if (numberFromUser < guessNumber):
        print("No, it is little higher than that")

    elif(numberFromUser > guessNumber):
        print("No, it is little less than that")
    else:
        print("Congratulation, you guessed the correct number")
        break
    attempt = attempt + 1
else:
    print("Attempt exceeded")










