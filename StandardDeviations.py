import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AmazonStocks.csv")

x = df["Date"]
y = df["Open"]
mean = df["Open"].mean()
std = df["Open"].std()

#upper = [mean + std] * len(df["Open"])
means = [(mean) for x in range(df["Open"].count())]
lower = [(mean - std) for x in range(df["Open"].count())]
lowerSecond = [(mean - (2 * std)) for x in range(df["Open"].count())]
lowerThird = [(mean - (3 * std)) for x in range(df["Open"].count())]
upper = [(mean + std) for x in range(df["Open"].count())]
upperSecond = [(mean + (2 * std)) for x in range(df["Open"].count())]

plt.plot(x, y, ls="-", color="purple", label="Open Stock Value")
plt.plot(x, means, ls="-", color="black", label="Mean Open Stock Value")

#Plot multiple series' that are related separately (label changes)
plt.plot(x, lower, ls=":", color="yellow", label="Lower STD_1")
plt.plot(x, lowerSecond, ls=":", color="orange", label="Lower STD_2")
plt.plot(x, lowerThird, ls=":", color="red", label="Lower STD_3")

#Plot multiple series' that are related at once
plt.plot(x, upper, x, upperSecond, ls=":", color="green", label="Upper STDs")

plt.title("Amazon Stock Opening STDs")
plt.xlabel("Date")
plt.ylabel("Opening Stock Value")
plt.legend()

plt.xticks(rotation=90)
plt.tick_params(axis='x', which='major', labelsize=3)
plt.tight_layout()

plt.show()