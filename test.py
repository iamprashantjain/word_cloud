import pandas as pd
import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pdb


df = pd.read_excel('test_word_cloud.xlsx')


def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    words = [word.lower() for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)



df['Strengths'] = df['Strengths'].apply(preprocess_text)
df['Opportunities'] = df['Opportunities'].apply(preprocess_text)


print(df['Strengths'])
