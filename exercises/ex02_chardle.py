"""EX02 - Chardle - a small part of making Wordle"""

__author__ = "730767778"


def input_word() -> str:
    """Gets input from user in from of 5 letter word"""
    word: str = input("Enter a 5-character word: ")
    # assigns input to variable so it can be returned later
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return word


# similar design and concept to input_word
def input_letter() -> str:
    """similar to input_word but only wants single length str"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()
        return letter


# hardcoded to check all five letters of word
def contains_char(word: str, letter: str) -> None:
    """Prints if letter matches each letter in word"""
    print("Searching for " + letter + " in " + word)
    # variable keeps count of matching characters
    count: int = 0
    # compares each letter in word to the letter input
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    # prints number of instances in correct format
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    """Organizes function calls for program"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
