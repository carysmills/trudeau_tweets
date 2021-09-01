import csv
import sys
from datetime import datetime
from langdetect import detect
import pandas as pd
import plotly.graph_objects as go

csv.field_size_limit(sys.maxsize)

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
                current_tally = tweet_tally.get(date_row, 0)
                tweet_tally[date_row] = 1 + current_tally


        except Exception:
            pass


with open('trudeau-total-output.tsv', 'w') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['date', 'value'])

for key in tweet_tally:
    value = tweet_tally[key]
    date = key.split("#")[0]

    with open('trudeau-total-output.tsv', 'a') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow([date, value])

