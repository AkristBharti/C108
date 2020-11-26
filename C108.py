import pandas as pnd
import csv
import statistics
import plotly.express as px
import plotly.graph_objects as gp 
import plotly.figure_factory as pf


df = pnd.read_csv('C108.csv')

fig1 = pf.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"], show_hist = True)
fig1.show()
