import datetime
from langdetect import detect
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('trudeau-output.tsv', sep='\t', header=0)
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.strftime("%Y-%m")

selected_word = 'jobs'
filtered = df[df.word.eq(selected_word)]
reindexed = filtered.set_index('date')

start = datetime.date(2017,7,1)
end = datetime.date(2021,8,31)
idx = pd.period_range(start, end, freq='M')

filled_vals = reindexed.reindex(index=list(idx.astype(str)), copy=False, fill_value=0)

df_total = pd.read_csv('trudeau-total-output.tsv', sep='\t', header=0)
df_total['date'] = pd.to_datetime(df_total['date'])
df_total['date'] = df_total['date'].dt.strftime("%Y-%m")
totals_reindexed = df_total.set_index('date')
filled_total_vals = totals_reindexed.reindex(index=list(idx.astype(str)))

test = pd.merge(filled_vals, filled_total_vals, left_index=True, right_index=True)
print(test)

fig = go.Figure(go.Scatter(x = test.index, y = test['value'], name='Times ' + selected_word + ' tweeted'))
fig.add_scatter(x=test.index, y=test['total'], name="Total tweets")

fig.show()
