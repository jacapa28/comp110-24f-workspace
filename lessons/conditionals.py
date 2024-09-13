"""Practicing conditionals"""


def check_first_letter(word: str, letter: str) -> str:
    if word[0].lower() == letter.lower():
        return "match!"
    else:
        return "no match!"


print(
    check_first_letter(
        input("Give me a word: "), input("What should the first letter be: ")
    )
)
