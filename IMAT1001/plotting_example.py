import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1000)
y_1 = np.exp(x)
y_2 = 2*x - 1

fig, ax = plt.subplots()
ax.plot(x, y_1, label=r"$e^x$", color="r")
ax.plot(x, y_2, label="2x - 1", color="g")

ax.set_xlabel("x", loc="right")
ax.set_ylabel("y", loc="top", rotation=0)
ax.set_title("Learning to plot")
plt.legend()

plt.grid()
plt.show()
