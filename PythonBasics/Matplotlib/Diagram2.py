import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])

plt.show()
