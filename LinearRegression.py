import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("NetflixStocks.csv")

xValues = df["Open"]
yValues = df["Close"]

#Linear regresion fitting
m, c = np.polyfit(xValues, yValues, 1)

#Plot linear regression model
plt.plot(xValues, (m*xValues + c), ls=":", color="red", label="Linear Regression")

#Plot Open Vs. Close values on top
plt.scatter(xValues, yValues, color="green", label="Open Vs. Close Stock Values")

plt.title("Open Vs. Close Stock Values")
plt.xlabel("Open Stock Values")
plt.ylabel("Close Stock Values")

plt.show()