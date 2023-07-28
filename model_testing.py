# %%
from google_play_scraper import Sort, reviews
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
import glob

# %%
def count_reviews(reviews):
    positive = 0
    negative = 0
    neutral = 0
    analyzer = SentimentIntensityAnalyzer()
    for review in reviews:
        score = analyzer.polarity_scores(review)
        if score["compound"] > 0.04:
            positive += 1
        elif score["compound"] < -0.04:
            negative += 1
        else:
            neutral += 1
    return positive, negative, neutral

# %%

def get_reviews(df):
    
    positive, negative, neutral = count_reviews(df['content'])
    ans = "Not Fraud"
    if (negative / (positive + negative + neutral) >= 0.5):
        print(negative, positive, neutral)
        ans = "Fraud"
    elif ((negative / (positive + negative) ) >= 0.4):
        print(negative, positive, neutral)

        ans = "Fraud"
    # print(positive, negative, neutral, ans)
    return ans

# %%

folder_path = "dataset\Safe"

# Get a list of all the CSV files in the folder
csv_files = glob.glob(folder_path + "/*.csv")
c = 0
t= 0

# Iterate over the list of CSV files
for csv_file in csv_files:

    df = pd.read_csv(csv_file, encoding='utf-8')
    x = get_reviews(df)
    if (x == "Fraud"):
        c+=1
    # else:
    #     print(csv_file)
    t += 1

print(c / t, c, t)

        