count = 0
max_attempts = 3
number = 7

while count < max_attempts :
    guess = input("Guess a number between 1 and 10: ")
    count += 1
    if guess.isdigit() :
        guess = int(guess)

        if guess == number :
            print("Congratulations, you guessed the number!")
            break
        elif guess > number :
            print("Too high, you guessed the number!")
        else:
            print("Too low, you guessed the number!")
    else:
        print("Invalid input!")
else:
    print("You can't guess the number!,The number was:" , number)
