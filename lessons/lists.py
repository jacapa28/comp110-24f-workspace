list = [0, 0, 0, 1, 1, 1]

list.append(0)


def change(word: str) -> str:
    word += "!"
    return word


word = "wow"
print(change(word=word))
