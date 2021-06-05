import pandas as pd
import plotly.express as px

cv = pd.read_csv("covid_data.csv")
fig = px.bar(cv, x="Date", y="Cases",color="Country")
fig.show()