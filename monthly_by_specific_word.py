import csv
import sys
from datetime import datetime
from langdetect import detect
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import plotly.graph_objects as go

csv.field_size_limit(sys.maxsize)

stop_words=set(stopwords.words("english"))
stop_words.update({'rt', 'https', 'i', 'we', 'amp', 'justintrudeau', 'and', 'the'})

tweet_tally = dict()

with open('trudeau_all.tsv', newline='') as csvfile:
    tweetreader = csv.reader(csvfile, delimiter="\t", quotechar='|')

    for row in tweetreader:
        tweet = row[1]
        date = row[3]

        my_date = datetime.strptime(date, "%B %d, %Y at %I:%M%p")
        month = str(my_date.month)
        year = str(my_date.year)
        date_row = year + "-" + month

        try:
            if detect(tweet) == "en":
                tokenized_word=word_tokenize(tweet)

                for word in tokenized_word:
                    lower_word = word.lower()
                    if (lower_word not in stop_words) and (lower_word.isalpha()):
                        word_date_key = date_row + '#' + lower_word

                        current_tally = tweet_tally.get(word_date_key, 0)
                        tweet_tally[word_date_key] = 1 + current_tally


        except Exception:
            pass


with open('trudeau-output.tsv', 'w') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['date', 'word', 'value'])

for key in tweet_tally:
    value = tweet_tally[key]
    date = key.split("#")[0]
    text = key.split("#")[1]

    with open('trudeau-output.tsv', 'a') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow([date, text, value])

