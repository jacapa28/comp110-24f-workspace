"""Location for main functions using dictionaries"""

__author__ = "730767778"


def invert(original: dict[str, str]) -> dict[str, str]:
    """returns dictionary with inverted keys and values of inputted dictionary"""
    new: dict[str, str] = {}
    # iterates over the keys of inputted function
    for key in original:
        # for each key in input list, iterates over the new dict to see if key exists
        for idx in new:
            # raises error if key already used
            if original[key] == idx:
                raise KeyError
        # adds the new key and value to new dict
        new[original[key]] = key
    return new


def favorite_color(favs: dict[str, str]) -> str:
    """returns string of most frequent occurance"""
    # initializes dict that will keep track of values and their occurances
    record: dict[str, int] = {}
    # adds values of input dict as keys for record dict
    for key in favs:
        record[favs[key]] = 0
    # updates number of occurances in the record dict
    for key in favs:
        record[favs[key]] += 1
    # initializes variables for keeping track of highest num of occurances
    max: int = 0
    most_frequent: str = ""
    for key in record:
        if record[key] > max:
            max = record[key]
            most_frequent = key
    return most_frequent


def count(original: list[str]) -> dict[str, int]:
    """Counts the number of occurances of values in a list"""
    original_count: dict[str, int] = {}
    # fills new dict with values in the list
    for value in original:
        original_count[value] = 0
    # updates occurances of values in the list in the dict
    for value in original:
        original_count[value] += 1
    return original_count


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Creates a dictionary that alphabetizes a given list"""
    alphabetical: dict[str, list[str]] = {}
    # iterates over all of the list
    for word in words:
        exists: bool = False
        # for every element in the list, checks if a key already made
        for key in alphabetical:
            if word[0].lower() == key:
                exists = True
        # if the key does not exist yet, it creates new key with letter in the dict
        if not exists:
            alphabetical[word[0].lower()] = []
    # iterates over list elements again
    for word in words:
        # for every list element, checks which key matches the first letter and
        # appends the word to the list in the dict
        for key in alphabetical:
            if word[0].lower() == key:
                alphabetical[key].append(word)
    return alphabetical


def update_attendance(
    attendance_log: dict[str, list[str]], new_day: str, new_student: str
) -> None:
    """Appends new students to specific keys in an attendance dictionary"""
    # iterates over the keys in the given dict
    day_exists: bool = False
    for day in attendance_log:
        # if the key matches the day provided by the function, proceeds
        if new_day == day:
            student_exists: bool = False
            # iterates over given list by dictionary[new_day] and checks for student
            for student in attendance_log[day]:
                if student == new_student:
                    student_exists = True
            # if the student not already entered, appends student
            if not student_exists:
                attendance_log[day].append(new_student)
            # updates variable saying the day provided already in the dict
            day_exists = True
    # adds given day key if not already in dict and gives it a list containing student
    if not day_exists:
        attendance_log[new_day] = [new_student]
