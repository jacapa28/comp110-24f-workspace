"""Examples of dictionaries in Python"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["mint"] = 3

has_pbj: bool = "pbj" in ice_cream

print(ice_cream["mint"])
print(has_pbj)
