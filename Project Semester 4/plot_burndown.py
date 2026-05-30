"""Generate burndown chart (planned vs actual remaining tasks) as PDF."""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib as mpl

# Data: 8-day four-sprint development process (24 task items total)
DAYS = list(range(1, 9))
PLANNED = [24, 21, 18, 15, 12, 9, 5, 0]
ACTUAL = [24, 22, 19, 15, 13, 8, 5, 0]

COLOR_PLANNED = "#0066CC"  # blue
COLOR_ACTUAL = "#CC0000"  # red

OUT_DIR = Path(__file__).resolve().parent / "out"
OUT_FILE = OUT_DIR / "burndown_chart.pdf"

# Figure: 2:1 aspect ratio (inches), white background
FIG_WIDTH = 10.0
FIG_HEIGHT = FIG_WIDTH / 2.0


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    mpl.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
            "font.size": 14,
            "axes.labelsize": 16,
            "axes.titlesize": 16,
            "legend.fontsize": 14,
            "xtick.labelsize": 14,
            "ytick.labelsize": 14,
            "axes.edgecolor": "#333333",
            "axes.labelcolor": "#333333",
            "xtick.color": "#333333",
            "ytick.color": "#333333",
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
            "savefig.edgecolor": "white",
        }
    )

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT), dpi=300)

    ax.plot(
        DAYS,
        PLANNED,
        color=COLOR_PLANNED,
        linewidth=1.8,
        marker="o",
        markersize=6,
        markerfacecolor="white",
        markeredgewidth=1.5,
        markeredgecolor=COLOR_PLANNED,
        label="Planned Remaining Tasks",
        zorder=2,
    )
    ax.plot(
        DAYS,
        ACTUAL,
        color=COLOR_ACTUAL,
        linewidth=1.8,
        marker="s",
        markersize=5.5,
        markerfacecolor="white",
        markeredgewidth=1.5,
        markeredgecolor=COLOR_ACTUAL,
        label="Actual Remaining Tasks",
        zorder=3,
    )

    ax.set_xlabel("Project Day", fontsize=16)
    ax.set_ylabel("Remaining Tasks", fontsize=16)
    ax.tick_params(axis="both", which="major", labelsize=14, width=1.2, length=5)
    ax.set_xlim(0.5, 8.5)
    ax.set_ylim(-0.5, 26)
    ax.set_xticks(DAYS)
    ax.set_yticks(range(0, 27, 3))
    ax.grid(True, linestyle="-", linewidth=0.75, color="#AAAAAA", alpha=0.95)
    ax.set_axisbelow(True)

    ax.legend(
        loc="upper right",
        frameon=True,
        framealpha=1.0,
        edgecolor="#999999",
        fontsize=14,
        markerscale=1.4,
        handlelength=2.5,
        borderpad=0.8,
        labelspacing=0.6,
    )

    for spine in ax.spines.values():
        spine.set_linewidth(1.2)

    fig.tight_layout()
    fig.savefig(
        OUT_FILE,
        format="pdf",
        bbox_inches="tight",
        pad_inches=0.05,
    )
    plt.close(fig)
    print(f"Saved: {OUT_FILE}")


if __name__ == "__main__":
    main()
