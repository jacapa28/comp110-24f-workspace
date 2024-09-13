"""More conditionals practice."""


def get_weather_report() -> str:
    weather = input("What is the weather? ")
    if weather.lower() == "rainy" or weather.lower() == "cold":
        print("Bring a jacket!")
    elif weather.lower() == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
