## Dictionary in a list.
## Instructions 
#  You are going to write a program that adds to a travel_log. 
#  You can see a travel_log which is a list that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line 21 to add
#   the entry for Russia to the travel_log.

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg], "total_visits": 2)

#### You've visited Russia 2 times.
### You've been to Moscow and Saint Petersburg.

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



## define a function for adding data in tavel log

def add_new_country(country_visited,city_visited,total_visits):
    new_country ={}
    new_country["county"] = country_visited
    new_country["city_visited"] = city_visited
    new_country["total_visits"] = total_visits
    travel_log.append(new_country)
    
add_new_country("Russia",["Moscow", "Saint Petersburg"], 2)

print(travel_log)