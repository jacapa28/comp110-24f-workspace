"""Challenge problem using while loops."""

__author__ = "730767778"


# run through phrase variable and check each char with search_char
def num_instances(phrase: str, search_char: str) -> int:
    """Checks for number of instances of search_char in phrase"""
    # create variables to store count and index place as func runs
    index: int = 0
    count: int = 0
    # iterates through all of phrase and compares with search_char
    while index < len(phrase):
        if phrase[index] == search_char:
            # update count of instances and index
            count += 1
        index += 1
    # return count of instances
    return count
