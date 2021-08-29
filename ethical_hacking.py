import matplotlib.pyplot as plt
import pandas as pd

# load the file containing data
data = pd.read_csv("assets/covid-report.csv")

# set the style for plot
plt.style.use("seaborn")

# plot the data
df = data.groupby("Category")["Numbers"].sum()
df.plot(kind="area", stacked=False)
plt.xlabel("Category")
plt.ylabel("Number")
plt.show()
