"""
cleans raw data
"""


import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def clean_data(givendata):
    # removing people with no names
    givendata["users"] = [user for user in givendata["users"]if user["name"]!=""]

    # removing people with no friends
    givendata["users"] = [user for user in givendata["users"] if user["friends"]!=[]]

    #removing repeated friend indices
    for user in givendata["users"]:
        user["friends"] = list({friend for friend in user["friends"]})

    # removing repeated pages
    unique_pages = {}
    for page in givendata["pages"]:
        unique_pages[page["id"]] = page
    givendata["pages"] = list(unique_pages.values())

    return givendata
ourdata = load_data("data/raw/massive_data.json")
cleaned_data = clean_data(ourdata)
json.dump(cleaned_data, open("data/cleaned/cleaned_data.json", "w"),indent=4)

