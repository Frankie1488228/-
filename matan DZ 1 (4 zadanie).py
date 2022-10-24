import numpy as np
import matplotlib.pyplot as plt

k1 = 1
k2 = 3

y = lambda x, k: np.cos(k * x)

fig = plt.subplots()

x = np.linspace(-3, 3, 170)

plt.plot(x, y(x, k1))
plt.plot(x, y(x, k2))

plt.title('График функции')
plt.xlabel('значения по X')
plt.ylabel('значения по Y')
plt.plot(x, y(x, k1), label='dheh', marker='o')
plt.plot(x, y(x, k2), label='hdehej', marker='^')

plt.show()
