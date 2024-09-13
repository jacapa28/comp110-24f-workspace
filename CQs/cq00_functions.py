"""Challenge question about defining and calling functions."""

__author__ = "730767778"


def mimic(message: str) -> str:
    """Return a message back defined in the arguments"""
    return message


if __name__ == "__main__":
    print(mimic(message=input("What is your message?")))
