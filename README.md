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

## 🗂 Project Structure
social-recommendation-system/
├── data/
│ ├── raw/ # Uncleaned JSON data dumps
│ └── cleaned/ # Cleaned output data
│
├── src/
│ ├── 01_display_data.py
│ ├── 02_clean_data.py
│ ├── 03_people_you_may_know.py
│ └── 04_pages_you_might_like.py
│
├── README.md
├── requirements.txt
└── .gitignore

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
