import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 4, 1000)
y_1 = np.sin(x)
y_2 = np.cos(x)
idx = np.argwhere(np.diff(np.sign(y_1 - y_2))).flatten()

fig, ax = plt.subplots()
ax.plot(x, y_1, label=r"$sin(x)$", color="r")
ax.plot(x, y_2, label=r"$cos(x)$", color="g")
ax.plot(x[idx], y_1[idx], 'ro')

ax.set_xlabel("x", loc="right")
ax.set_ylabel("y", loc="top", rotation=0)
ax.set_title("Learning to plot")
plt.legend()

plt.grid()
plt.show()

for val in idx:
    print(x[val])
