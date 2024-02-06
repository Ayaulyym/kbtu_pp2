from random import randint
def GuessNumber():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20. Take a guess.")
    number = randint(1,20)
    counter = 0
    
    while True:
        x = int(input())
        counter += 1
        if x < number:
            print("Your guess is too low. Take a guess.")

        elif x > number:
            print("Your guess is too high. Take a guess.")

        else:
            print(f"Good job, {name}! You guessed my number in {counter} guesses!")

            break

GuessNumber()