import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Setup a subplot : height = 2, width = 1, active = 1
plt.subplot(2, 1, 1)

plt.plot(x, y_sin)
plt.title('Sine')

# Setup a subplot : height = 2, width = 1, active = 2
plt.subplot(2, 1, 2)

plt.plot(x, y_cos)
plt.title('Cosine')

plt.show()
