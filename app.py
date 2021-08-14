import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('trudeau-output.tsv', sep='\t', header=0)

fig = go.Figure(go.Scatter(x = df['date'], y = df['value']))

fig.update_layout(title='Trudeau tweets',
                   plot_bgcolor='rgb(230, 230,230)')

fig.show()