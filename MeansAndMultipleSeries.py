import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AmazonStocks.csv")

xpoints = df["Date"]
y1points = df["Close"]
mean = df["Close"].mean()
y3mean = [mean for x in range(df["Close"].count())]

plt.plot(xpoints, y1points, ls="-", color="blue", label="Closing")
plt.plot(xpoints, y3mean, ls=":", color="red", label="Closing Mean")

plt.xticks(rotation=90)

plt.tick_params(axis='x', which='major', labelsize=3)
plt.tight_layout()

plt.xlabel("Date")
plt.ylabel("Stock Value")
plt.title("Amazon Stock Analysis")

plt.legend(title="Key/Legend")

plt.show()