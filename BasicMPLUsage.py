import numpy as np
import matplotlib.pyplot as plt

#x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
#y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

plt.plot(x, y)
plt.title("Students Vs. Stonks")
plt.xlabel("Kit Kat Count")
plt.ylabel("Ben's Heart Rate")

plt.grid()

plt.show()

