import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def list_common_elements(list1, list2):
    return len(set(list1).intersection(set(list2)))

def pages_you_might_like(user_id, givendata):
    all_friends = {}

    for user in givendata["users"]:
        all_friends[user["id"]] = user["friends"]
    
    user_pages = {}
    for user in givendata["users"]:
        user_pages[user["id"]] = user["liked_pages"]

    suggestion_score = {}
    for user in user_pages:
        if(user != user_id and user in all_friends[user_id]):
            suggestion_score[user] = list_common_elements(user_pages[user_id],user_pages[user])

    page_recommendations = {}
    
    for uid,score in suggestion_score.items():
        if score!=0:
            recommended = [i for i in user_pages[uid] if i not in user_pages[user_id]]
        if score not in page_recommendations:
            page_recommendations[score] = []

        page_recommendations[score].extend(recommended)

    # final_recommendations = [(uid,key) for uid,key in page_recommendations.items() if uid>0]
    # list = page_recommendations.values()
    sorted_recommendations = sorted(page_recommendations.items(), key = lambda x:x[0], reverse = True)

    list1 = [set(pages) for score,pages in sorted_recommendations if score>0]
    list2 = []
    for i in list1:
        for j in i:
            list2.append(j)
    
    
    # return [set(pages) for score,pages in sorted_recommendations if score>0]
    return list2

    
ourdata = load_data("data/cleaned/cleaned_data.json")
user_id = 1
print(f"Pages you might like for user with id {user_id} are {pages_you_might_like(user_id, ourdata)}")

