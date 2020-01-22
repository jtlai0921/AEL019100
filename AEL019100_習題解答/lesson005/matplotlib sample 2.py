import matplotlib.pyplot as plt
import numpy as np

angle = np.array(range(360))
sin_value = np.sin(angle * np.pi / 180)

ax = plt.subplot(111)
plt.plot(angle, sin_value)

plt.xlim(0,360)
plt.ylim(-1.2,1.2)

plt.show()

