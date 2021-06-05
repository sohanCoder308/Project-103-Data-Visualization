import pandas as pd
import plotly.express as px

cv = pd.read_csv("covid_data.csv")
fig = px.scatter(cv, x="Date", y="Cases",color="Country")
fig.show()