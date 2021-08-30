import pandas as pd
import plotly.graph_objects as go
import datetime

df = pd.read_csv('trudeau-output.tsv', sep='\t', header=0)
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.strftime("%Y-%m")
filtered = df[df.word.eq('climate')]
reindexed = filtered.set_index('date')

start = datetime.date(2017,1,1)
end = datetime.date(2021, 6,15)
idx = pd.period_range(start, end, freq='M')

filled_vals = reindexed.reindex(index=list(idx.astype(str)), copy=False, fill_value=0)

print(filled_vals)


fig = go.Figure(go.Scatter(x = filled_vals.index, y = filled_vals['value']))

fig.update_layout(title='Trudeau tweets: climate',
                   plot_bgcolor='rgb(230, 230,230)')

fig.show()

### to do: compare to overall tweet volume
### lowercase for tallies, group like words
### update data to include all of august