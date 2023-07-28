# %%
from google_play_scraper import Sort, reviews
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# %%
def count_reviews(reviews):
    positive = 0
    negative = 0
    neutral = 0
    analyzer = SentimentIntensityAnalyzer()
    for review in reviews:
        score = analyzer.polarity_scores(review)
        if score["compound"] > 0.05:
            positive += 1
        elif score["compound"] < -0.05:
            negative += 1
        else:
            neutral += 1
    return positive, negative, neutral

# %%

def get_reviews(id):
    project, abc = reviews(id, count=400, sort=Sort.NEWEST)
    df = pd.json_normalize(project)
    df['content'] = df['content'].astype('str')
    positive, negative, neutral = count_reviews(df['content'])
    ans = "Not Fraud"
    if (negative / (positive + negative + neutral) >= 0.5):
        ans = "Fraud"
    elif ((negative / (positive + negative) ) >= 0.4):
        ans = "Fraud"
    return ans
    
# %%

# print(get_reviews("com.gettimely.timely"))
