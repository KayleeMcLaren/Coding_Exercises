
travel_log = [
    {"country": "France",
     "visits": 12,
     "cities": ["Paris", "Lille", "Dijon"]
     },

    {"country": "Germany",
     "visits": 7,
     "cities": ["Berlin", "Hamburg", "Stuttgart"]
     },
]


def add_new_country(country_visited="Russia", times_visited=2, cities_visited=[]):
    new_dict = {"country": country_visited, "visits": times_visited, "cities": cities_visited}
    travel_log.append(new_dict)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
