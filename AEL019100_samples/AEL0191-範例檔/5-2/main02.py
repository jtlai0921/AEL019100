import matplotlib.pyplot as plt
import matplotlib.patches as patches

ax = plt.subplot(111)
ax.add_patch(
    patches.Rectangle((0, 0), 5, 60, facecolor = 'blue')
)
ax.add_patch(
    patches.Rectangle(
        (10, 0), 5, 80, facecolor = 'red')
)
ax.add_patch(
    patches.Rectangle(
        (20, 0), 5, 90, facecolor = 'gray')
)

ax.set_xlim(0, 30)
ax.set_ylim(0, 100)

plt.show()
