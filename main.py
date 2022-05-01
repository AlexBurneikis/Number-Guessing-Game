import random

maximum = 100
minimum = 0
answer = random.randint(minimum, maximum)
#print(answer)

def is_correct(guess):
    if int(guess) == answer:
        return True
    return False

def is_higher(guess):
    if guess > answer:
        return True
    return False

def is_number(guess):
    try:
        int(guess)
        return True
    except:
        return False

def is_in_range(guess):
    if minimum <= int(guess) and int(guess) <= maximum:
        return True
    return False
        
def is_number_in_range(guess):
    if is_number(guess):
        if is_in_range(guess):
            return True
    return False

def get_guess():
    guess = input("Guess: ")
    while not is_number_in_range(guess):

        if not is_number(guess):
            print("Input must be a number.")

        elif not is_in_range(guess):
            print(f"Input must be between {minimum} and {maximum}.")

        guess = input("Guess: ")

    return(guess)

def main():
    guessno = 0

    guess = int(get_guess())
    while not is_correct(guess):

        guessno += 1

        print(f"Guess #{guessno}: Incorrect")

        if is_higher(guess):
            print(f"Answer is lower than {guess}")
        else:
            print(f"Answer is higher than {guess}")

        guess = int(get_guess())

    guessno += 1
    print(f"Guess #{guessno}: Correct")

main()