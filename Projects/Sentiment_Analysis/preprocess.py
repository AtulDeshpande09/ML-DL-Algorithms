import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd

data = pd.read_csv('sentiment.csv', encoding='latin1')
df = pd.DataFrame(data)

def process_tweets(tweet):
    tweet = re.sub(r'[^a-zA-Z]', ' ' , tweet)
    tweet = tweet.lower()
    tweet = tweet.split()
    stemmer = PorterStemmer()
    tweet = [ stemmer.stem(word) for word in tweet if word not in set(stopwords.words("english"))]
    return " ".join(tweet)

# Drop Unnecessary Columns
df.drop(columns = ['1467810369', 'Mon Apr 06 22:19:45 PDT 2009', 'NO_QUERY', '_TheSpecialOne_'])

# Apply Preprocessing Function
df['processed_tweet'] = df["@switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer.  You shoulda got David Carr of Third Day to do it. ;D"].apply(process_tweets)

df.to_csv("preprocessed.csv",index=False)