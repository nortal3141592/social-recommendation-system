# Social Recommendation System (People & Pages)

A simple Python-based recommendation system that:
- Cleans large social-network data dumps
- Suggests **People You May Know**
- Suggests **Pages You Might Like**

The project demonstrates how real-world social graph data can be processed
step-by-step using basic data structures (lists, dictionaries, sets).

---

## 📌 Features

- JSON-based data ingestion
- Data cleaning:
  - Removes users with missing names
  - Removes users with no friends
  - Deduplicates friends and pages
- Friend-of-friend recommendation system
- Page recommendation based on shared interests

---

## 📊 Sample Input Format

```json
{
  "users": [
    {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
    {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [102]}
  ],
  "pages": [
    {"id": 101, "name": "Python Developers"}
  ]
}
```

## How to Use

- Store your raw data inside the `data/raw/` directory.  
  Make sure the data is in JSON format.

- Run `src/01_display_raw_data.py` to get an overview of your raw data.

- Run `src/02_data_cleaning.py` to clean the raw data.  
  The cleaned output will be saved inside `data/cleaned/`.

- Run `src/03_people_you_may_know.py` and set the `user_id` for which you want
  to find people the given user may know.

- Run `src/04_pages_you_might_like.py` and set the `user_id` for which you want
  to find pages the given user might like.
