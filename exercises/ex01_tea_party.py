"""Program will organize a cozy tea party by giving you the number of"""

"""teabags and treats necessary along with the price!"""

__author__: str = "730767778"


# this is the main function that sets up the output
def main_planner(guests: int) -> None:
    """Organizes outputs of other functions into readable text for user"""
    # make sure to use function calls for arguments, not hard-code values
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    return None


# calculates
def tea_bags(people: int) -> int:
    """Calculates number of tea bags needed based on number of guests"""
    return people * 2


# calculates
def treats(people: int) -> int:
    """Calculates number of treats needed based on how many drinks guests will drink"""
    return int(tea_bags(people=people) * 1.5)


# final calculation function
def cost(tea_count: int, treat_count: int) -> float:
    """Calculates cost based on number of tea bags and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


# bit of a formality, runs when program is run in terminal
if __name__ == "__main__":
    """Executes our functions when the code is run in the correct manner"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
