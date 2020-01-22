import matplotlib.pyplot as plt

# 設定中文字體才能正確顯示中文
plt.rcParams['font.sans-serif']=['SimHei']

labels = '亞洲', '美洲', '歐洲', '澳洲'
sizes = [37, 30, 20, 13]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%')

plt.axis('equal')

plt.show()
