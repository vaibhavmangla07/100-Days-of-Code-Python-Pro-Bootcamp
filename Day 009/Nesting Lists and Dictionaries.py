# Dictionary
capitals = {
    "France" : "Paris",
    "India" : "Delhi",
    "Germany" : "Berlin"
}
# List in Dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "India" : ["Delhi", "Mumbai", "Bengaluru",],
    "Germany" : ["Berlin", "Stuttgart"]
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

travel = {
    "France" : {
        "num_times_vist" : 8,
        "cities_visit" : ["Paris", "Lille", "Dijon"]
    },
    "India" : {
        "num_times_vist" : 12,
        "cities_visit" : ["Delhi", "Mumbai", "Bengaluru",]
    },
    "Germany" : {
        "num_times_vist" : 5,
        "cities_visit" : ["Berlin", "Stuttgart"]
    }
}
print(travel["France"])
print(travel["India"])
print(travel["Germany"])