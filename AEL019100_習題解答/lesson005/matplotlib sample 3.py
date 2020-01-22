import matplotlib.pyplot as plt
import matplotlib.patches as patches

ax = plt.subplot(111)
ax.add_patch(
    patches.Rectangle(
        (0, 0),   # (x,y)
        5,          # width
        60,          # height
    )
)
ax.add_patch(
    patches.Rectangle(
        (10, 0),   # (x,y)
        5,          # width
        80,          # height
        facecolor = 'red'
    )
)
ax.add_patch(
    patches.Rectangle(
        (20, 0),   # (x,y)
        5,          # width
        90,          # height
        facecolor = 'gray'
    )
)

ax.set_xlim(0, 30)
ax.set_ylim(0, 100)

plt.show()
