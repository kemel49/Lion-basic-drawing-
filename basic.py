import numpy as np

# Create a simple drawing of a lion
fig, ax = plt.subplots()

# Draw the body
circle = plt.Circle((0.5, 0.5), 0.2, color='orange', ec='brown', lw=3)
ax.add_patch(circle)

# Draw the head
head = plt.Circle((0.5, 0.75), 0.1, color='orange', ec='brown', lw=3)
ax.add_patch(head)

# Draw the legs
legs = [
    plt.Line2D([0.4, 0.4], [0.3, 0.5], color='brown', lw=5),
    plt.Line2D([0.6, 0.6], [0.3, 0.5], color='brown', lw=5)
]
for leg in legs:
    ax.add_line(leg)

# Draw the tail
tail = plt.Line2D([0.7, 0.9], [0.5, 0.6], color='brown', lw=3)
ax.add_line(tail)

# Draw the eyes
eyes = [
    plt.Circle((0.48, 0.78), 0.02, color='black'),
    plt.Circle((0.52, 0.78), 0.02, color='black')
]
for eye in eyes:
    ax.add_patch(eye)

# Draw the nose
nose = plt.Polygon([[0.49, 0.76], [0.51, 0.76], [0.50, 0.74]], color='black')
ax.add_patch(nose)

# Draw the mouth
mouth = plt.Line2D([0.49, 0.51], [0.73, 0.73], color='black')
ax.add_line(mouth)

# Set plot limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title("Lion Roaming")
plt.show()
