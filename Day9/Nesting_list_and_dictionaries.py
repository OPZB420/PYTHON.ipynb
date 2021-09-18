#
### Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

## Nesting a List in a Dictionary

travel_log= {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    }

## Nesting a Dictionary in a Dictionary

travel_log= {
    "France":{"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "India": {"city_visited": ["Azamgahr", "Lucknow", "Delhi"], "total_visits": 20},
}

## Nesting a dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
    {
        "country": "India",
        "city_visited": ["Azamgahr", "Lucknow", "Delhi"],
        "total_visits": 20
    },
]

