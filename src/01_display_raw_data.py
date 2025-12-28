import json

def loaddata(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def display_users(givendata):
    print("Users and their connections:")

    for user in givendata["users"]:
        print(f"{user['name']} (ID: {user['id']}) - Friends: {user['friends']} - Liked Pages: {user['liked_pages']}")
    print("\nPages:")

    for page in givendata["pages"]:
        print(f"{page['id']}: {page['name']}")
    
ourdata = loaddata("data/raw/codebook_data.json")
display_users(ourdata)

