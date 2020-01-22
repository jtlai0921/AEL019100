from matplotlib import pyplot as plt
from numpy import *   # 使用第7種方法載入全部函式
from numpy import array as arr   # 載入array()函式並指定簡稱

angle = arr(range(360))   # 使用我們指定的簡稱
sin_value = sin(angle * pi / 180)

ax = plt.subplot(111)
plt.plot(angle, sin_value)

plt.xlim(0,360)
plt.ylim(-1.2,1.2)

plt.show()
