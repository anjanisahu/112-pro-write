
import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
df=pd.read_csv("data_story.csv")
fig=px.scatter(df, y="quant_saved",color="female")
fig.show()

