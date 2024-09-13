"""CQ using conditionals."""

__author__ = "730767778"


def guess_a_number() -> None:
    """Creates a secret number and checks to see if input is equal"""
    secret: int = 7
    guess: str = input("Guess a number: ")
    print("Your guess was " + guess)
    if int(guess) == secret:
        print("You got it!")
    elif int(guess) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
