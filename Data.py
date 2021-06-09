import csv
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("Project108/data.csv")
fig=ff.create_distplot([df["Avg Rating"].to_list()],["Avg Rating"],show_hist=False)
fig.show()