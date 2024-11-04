"""Wordle game clone exercise."""

__author__ = "730767778"


def input_guess(secret_word_len: int) -> str:
    """Repeatedly asks for guess."""
    # only takes guess once its length matches parameter
    guess = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks secret word for instances of a character and returns a boolean."""
    assert len(char_guess) == 1
    idx = 0
    # iterates through secret_word and checks each index for char_guess
    while idx < len(secret_word):
        # if it finds char_guess in secret_word, exits function with true
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    # returns False if it makes it through while loop without finding char_guess
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns emoji string based on whether characters in guess are correct."""
    assert len(guess) == len(secret)

    # named constants
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # creates empty string for emojis and index int for iterating
    emojis = ""
    idx = 0
    # iterates through whole length of guess
    while idx < len(guess):
        # adds green square if char is in correct place in guess
        if guess[idx] == secret[idx]:
            emojis += GREEN_BOX
        # adds yellow square if char is not correct but present in secret
        elif contains_char(secret_word=secret, char_guess=guess[idx]):
            emojis += YELLOW_BOX
        # adds white if char not present in secret at all
        else:
            emojis += WHITE_BOX
        idx += 1
    # returns emoji string
    return emojis


def main(secret: str) -> None:
    """Start of program and primary game loop."""
    turn_count: int = 1
    # plays through 6 turns or until guess is the same as secret
    while turn_count <= 6:
        print(f"=== Turn {turn_count}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess=guess, secret=secret))
        # checks if user won and exits function if they did
        if guess == secret:
            print(f"You won in {turn_count}/6 turns!")
            return None
        turn_count += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
