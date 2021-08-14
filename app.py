import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('trudeau-output.tsv', sep='\t', header=0)
filtered = df[df.word.eq('climate')]

fig = go.Figure(go.Scatter(x = filtered['date'], y = filtered['value']))

fig.update_layout(title='Trudeau tweets: climate',
                   plot_bgcolor='rgb(230, 230,230)')

fig.show()

### to do: compare to overall tweet volume
### add missing month values
### lowercase for tallies, group like words
### remove august since it is incomplete data