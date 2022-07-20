import random
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Type a Number larger than 0 next time.')
        quit()
else:
    print('Type a Number larger than 0 next time.')
    quit()
random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a Number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("You were above the Number")
        else:
            print("You were below the Number")
print("You got it in", guesses,"guesses")
