import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("covid19_europe.csv")

df = df.drop(["Province_State","Confirmed","Recovered","Active"], axis = 1).groupby("Country_Region")

df.head(10).plot(subplots = True)
plt.legend()
plt.show()



