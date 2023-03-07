import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AmazonStocks.csv")

y_sortedOpenValues = df["Open"].sort_values()

plt.boxplot(y_sortedOpenValues, vert=False)

plt.title("Amazon Stock Opening IQR BoxPlot")
plt.xlabel("Opening Stock Value")
plt.ylabel("Spread")
plt.legend()

plt.show()