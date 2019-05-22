# Example B: Guess the number game

guessNumber = 67
attempt = 1

while(attempt<=3):
    numberFromUser = int(input("Enter the number between (1-100): "))
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