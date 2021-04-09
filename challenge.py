import csv
import pandas as pd 
import plotly.figure_factory as ff

df=pd.read_csv('newdata.csv')
fig=ff.create_distplot([df['average'].tolist()],['average'],show_hist=False)
fig.show()