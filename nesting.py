#this is a normal dictionary
capitals={
    "gujrat":"gandhinagar",
    "goa" : "panaji"
}

#this is nested dictionary
travel_places={
    "Delhi":["kutub minnar","india gate","hawa mehel"],
    "gujrat":["ahamdabad0","kutch","somnath"]   
}
#calling list element which is in a dictionary
print(travel_places["Delhi"][1])


#here is the nested list
nested_list=["A","B",["C","D"]]
#callin the elment from a list which  is in another list
print(nested_list[2][1])

#here the advanced example
travel_log={
    "delhi":{
        "number_of_places_visits":3,
        "visited":["kutub minnar","india gate","hawa mehel"]    
    },
    "gujrat":{
        "number_of_places_visits":3,
        "visited":["ahamdabad0","kutch","somnath"] 
    }
}
print(travel_log["delhi"]["visited"][1])

