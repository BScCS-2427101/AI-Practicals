import matplotlib.pyplot as plt
import numpy as np

# State numbers
states = np.arange(12)

# Utility values from the practical
utilities = [
    0.512, 0.640, 0.800, 1.000,
    0.420, 0.000, 0.350, 0.280,
    0.300, 0.250, 0.200, 0.150
]

# State labels
state_labels = [
    "S0", "S1", "S2", "S3",
    "S4", "S5", "S6", "S7",
    "S8", "S9", "S10", "S11"
]

# Create the bar graph
plt.figure(figsize=(10, 6))

bars = plt.bar(states, utilities)

# Add utility values above each bar
for bar, utility in zip(bars, utilities):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.02,
        f"{utility:.3f}",
        ha="center",
        fontsize=9
    )

# Graph details
plt.title("Utility Values of Smart Room States")
plt.xlabel("States")
plt.ylabel("Utility Value")
plt.xticks(states, state_labels)
plt.ylim(0, 1.15)
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()
