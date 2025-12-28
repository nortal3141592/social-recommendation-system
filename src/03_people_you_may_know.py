"""

Finds people you may know based on mutual friends.

"""

import json

def load_data(filename):
    with open(filename,"r") as f:
        data = json.load(f)
    return data

def people_you_may_know(user_id,givendata):
    all_friends = {}
    for user in givendata["users"]:
        all_friends[user["id"]] = user["friends"]
    friend_of_friend = {}
    for friend in all_friends[user_id]:
        if(friend in all_friends):
            friend_of_friend[friend] = all_friends[friend]
    
    score = {}
    # initialise everyone's score to be zero
    for friend in friend_of_friend:
        for friends in friend_of_friend[friend]:
            if(friends != user_id):
                score[friends] = 0
    # increment score by one if matches are found
    for friend in friend_of_friend:
        for friends in friend_of_friend[friend]:
            if(friends != user_id):
                score[friends] += 1
    # sort the dictionary in such a way that values are arranged in descending order

    suggestions = sorted(score.items(), key=lambda x:x[1],reverse = True)

    return [uid for uid,_ in suggestions]

ourdata = load_data("data/cleaned/cleaned_data.json")
user_id = 1
print(f"People you may know for user {user_id}: {people_you_may_know(user_id,ourdata)}")

