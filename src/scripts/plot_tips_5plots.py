import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
tips = pd.read_csv(url)

tips["tip_percentage"] = 100 * tips["tip"] / tips["total_bill"]

fig, axes = plt.subplot_mosaic(
    """
    ABC
    ADE
    """,
    figsize=(13.5, 4.5),
    sharex=False,
    sharey=False,
    gridspec_kw={
        "hspace": 0.5,
        "wspace": 0.3,
        "height_ratios": [1, 1],
        "width_ratios": [1, 0.7, 0.7],
    },
)

slope, intercept = np.polyfit(tips["total_bill"], tips["tip"], 1)

x = np.linspace(tips["total_bill"].min(), tips["total_bill"].max(), 100)
y = slope * x + intercept

axes["A"].scatter(
    tips["total_bill"],
    tips["tip"],
    label="Observations",
    alpha=0.7,
    color="tab:green",
)

axes["A"].plot(
    x,
    y,
    color="black",
    linewidth=2,
    label=rf"Linear fit: $y = {slope:.3f}x + {intercept:.3f}$",
)

axes["A"].legend(frameon=False)
axes["A"].set_xlabel("Total bill ($)")
axes["A"].set_ylabel("Tip ($)")

day_order = ["Thur", "Fri", "Sat", "Sun"]
day_tip_data = [
    tips.loc[tips["day"] == day, "tip_percentage"]
    for day in day_order
]

axes["B"].boxplot(
    day_tip_data,
    tick_labels=day_order,
    patch_artist=True,
    boxprops=dict(facecolor="orange", alpha=0.7),
    medianprops=dict(color="black", linewidth=2),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
)

axes["B"].set_xlabel("Day")
axes["B"].set_ylabel("Tip percentage")

time_order = ["Lunch", "Dinner"]
time_tip_data = [
    tips.loc[tips["time"] == meal, "tip_percentage"]
    for meal in time_order
]

axes["C"].boxplot(
    time_tip_data,
    tick_labels=time_order,
    patch_artist=True,
    boxprops=dict(facecolor="orange", alpha=0.7),
    medianprops=dict(color="black", linewidth=2),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
)

axes["C"].set_xlabel("Time")
axes["C"].set_ylabel("Tip percentage")

ymax = max(
    tips["tip_percentage"].max(),
    axes["B"].get_ylim()[1],
    axes["C"].get_ylim()[1],
)

axes["B"].set_ylim(0, ymax * 1.05)
axes["C"].set_ylim(0, ymax * 1.05)

day_bill_data = [
    tips.loc[tips["day"] == day, "total_bill"]
    for day in day_order
]

axes["D"].boxplot(
    day_bill_data,
    tick_labels=day_order,
    patch_artist=True,
    boxprops=dict(facecolor="tab:blue", alpha=0.7),
    medianprops=dict(color="black", linewidth=2),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
)

axes["D"].set_xlabel("Day")
axes["D"].set_ylabel("Total bill ($)")

time_bill_data = [
    tips.loc[tips["time"] == meal, "total_bill"]
    for meal in time_order
]

axes["E"].boxplot(
    time_bill_data,
    tick_labels=time_order,
    patch_artist=True,
    boxprops=dict(facecolor="tab:blue", alpha=0.7),
    medianprops=dict(color="black", linewidth=2),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
)

axes["E"].set_xlabel("Time")
axes["E"].set_ylabel("Total bill ($)")

ymax = max(
    tips["total_bill"].max(),
    axes["D"].get_ylim()[1],
    axes["E"].get_ylim()[1],
)

axes["D"].set_ylim(0, ymax * 1.05)
axes["E"].set_ylim(0, ymax * 1.05)

for ax in axes.values():
    sns.despine(ax=ax)

for letter, key in zip("abcde", ["A", "B", "C", "D", "E"]):
    ax = axes[key]
    bbox = ax.get_position()
    fig.text(
        bbox.x0 - 0.04,
        bbox.y1 + 0.01,
        letter,
        fontsize=16,
        fontweight="bold",
    )

plt.show()