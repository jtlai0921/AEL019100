# 這是使用第5種方法載入模組
from matplotlib import pyplot as plt

# 這是使用第6種方法載入需要的函式
from numpy import array, sin, pi

angle = array(range(360))
sin_value = sin(angle * pi / 180)

ax = plt.subplot(111)
plt.plot(angle, sin_value)

plt.xlim(0,360)
plt.ylim(-1.2,1.2)

plt.show()
