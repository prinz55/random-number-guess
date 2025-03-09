import random
print('"Guess the correct number and win a million dollars!"')
random_number = random.randint(1,9)

while True:
    guess_number = input("Guess a number between 1 to 9 : ")
    if guess_number.isdigit():
        guess_number = int(guess_number)

        if guess_number == random_number:
            print("Congratulation ! You Win")
            break
        elif guess_number >9:
            print("You entered higher number.")
        elif guess_number <1:
            print("You entered lower number")
        else:
            print("Try again !!")
    else:
        guess_number = input("Invalid number. Enter a valid number between 1 to 9 : ")



