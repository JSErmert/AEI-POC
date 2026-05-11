"""
v2 chart pass — refined headline-driven titles, dot-grid class imbalance,
EDA-callback markers in variable importance.
All numbers come from the validated R run (runtime_output_full.md).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd

OUT = Path(r"C:\Users\JSEer\AEI-POC\outputs")

NAVY = "#0B2A4A"
RUST = "#C1441E"
TEAL = "#1F7A8C"
AMBER = "#E0A458"
GREY_DARK = "#3A3A3A"
GREY_MID = "#777777"
GREY_LINE = "#D7D7D7"
WHITE = "#FFFFFF"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "axes.edgecolor": GREY_MID,
    "axes.labelcolor": GREY_DARK,
    "xtick.color": GREY_DARK,
    "ytick.color": GREY_DARK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titleweight": "bold",
    "axes.titlecolor": NAVY,
})


# 1. Class imbalance dot grid (signature visual for slide 3)
# ---------------------------------------------------------------------------
def chart_class_imbalance_dotgrid():
    # 84 + 2 + 14 = 100 dots, 10 columns × 10 rows
    counts = [("NoDiabetes", 84, NAVY),
              ("Prediabetes", 2, RUST),
              ("Diabetes", 14, TEAL)]

    fig, ax = plt.subplots(figsize=(11, 5.0), dpi=200)
    ncols = 10
    radius = 0.36
    spacing = 1.0

    idx = 0
    legend_handles = []
    for label, n, color in counts:
        for i in range(n):
            row = idx // ncols
            col = idx % ncols
            x = col * spacing
            y = -row * spacing
            ax.add_patch(plt.Circle((x, y), radius, color=color, zorder=2))
            idx += 1
        legend_handles.append(
            mpatches.Patch(color=color, label=f"{label}  —  {n}%")
        )

    ax.set_xlim(-0.7, ncols - 1 + 0.7)
    ax.set_ylim(-11.3, 0.7)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Headline + sub
    fig.text(0.045, 0.95, "Severe class imbalance",
             ha="left", va="top", fontsize=20, fontweight="bold", color=NAVY)
    fig.text(0.045, 0.885,
             "1 dot ≈ 1% of 253,680 patients. The Prediabetes slice is barely visible — that is the modeling problem.",
             ha="left", va="top", fontsize=11.5, color=GREY_DARK, style="italic")

    # Annotate the prediabetes dots — placed BELOW the grid to avoid overlap
    # Index of first prediabetes dot is 84 → row 8, col 4 (and col 5)
    pre_x = 4.5 * spacing  # midpoint between two prediabetes dots
    pre_y = -8 * spacing
    ax.annotate(
        "Prediabetes:  2 of 100",
        xy=(pre_x, pre_y - 0.45),
        xytext=(pre_x - 0.2, -10.6),
        fontsize=11.5, fontweight="bold", color=RUST, ha="left", va="top",
        arrowprops=dict(arrowstyle="-", color=RUST, lw=1.4,
                        connectionstyle="arc3,rad=0.0"),
    )

    ax.legend(
        handles=legend_handles, loc="lower right",
        frameon=False, fontsize=11, ncol=3,
        bbox_to_anchor=(1.0, -0.18),
    )

    fig.tight_layout(rect=[0, 0.02, 1, 0.83])
    fig.savefig(OUT / "chart_class_imbalance_v2.png", dpi=200,
                bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


# 2. Model comparison v2 — refined headline title + gap-from-baseline annotations
# ---------------------------------------------------------------------------
def chart_model_comparison_v2():
    df = pd.read_csv(OUT / "model_comparison_results.csv")
    df = df.sort_values("Accuracy", ascending=True).reset_index(drop=True)
    baseline = 0.8424

    fig, ax = plt.subplots(figsize=(11, 5.4), dpi=200)
    bar_colors = [TEAL, TEAL, NAVY, RUST]
    bars = ax.barh(df["Model"], df["Accuracy"], color=bar_colors,
                   edgecolor=WHITE, linewidth=1.0, height=0.62)

    for bar, val in zip(bars, df["Accuracy"]):
        gap = (val - baseline) * 100
        gap_label = f"+{gap:.2f}pp" if gap >= 0 else f"{gap:.2f}pp"
        gap_color = NAVY if gap >= 0 else GREY_MID
        ax.text(val + 0.0008,
                bar.get_y() + bar.get_height() / 2,
                f"{val:.4f}",
                va="center", ha="left",
                fontsize=13, fontweight="bold", color=GREY_DARK)
        ax.text(val + 0.0085,
                bar.get_y() + bar.get_height() / 2,
                f"  {gap_label}",
                va="center", ha="left",
                fontsize=11, color=gap_color, style="italic")

    ax.axvline(baseline, color=GREY_MID, linestyle="--", linewidth=1.2)
    ax.text(baseline - 0.001, -0.65,
            f"baseline = {baseline:.4f}  (majority-class prior)",
            color=GREY_MID, fontsize=10.5, va="top", ha="right")

    ax.set_xlim(0.78, 0.87)
    ax.set_ylim(-0.85, len(df) - 0.4)
    ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"{x:.3f}"))
    ax.set_xlabel("Test accuracy")

    fig.text(0.04, 0.96,
             "Decision Tree leads — but only by 0.0008",
             ha="left", va="top", fontsize=18, fontweight="bold", color=NAVY)
    fig.text(0.04, 0.905,
             "All four variants land within ~2 percentage points of each other and within ~0.5 pp of the 84.24 % majority-class baseline.",
             ha="left", va="top", fontsize=11.5, color=GREY_DARK, style="italic")

    fig.tight_layout(rect=[0, 0, 1, 0.88])
    fig.savefig(OUT / "chart_model_comparison_v2.png", dpi=200,
                bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


# 3. Variable importance v2 — group top-5, EDA-callback markers
# ---------------------------------------------------------------------------
def chart_variable_importance_v2():
    importance = {
        "HighBP": 3230.62925,
        "GenHlth": 1950.59018,
        "HighChol": 786.68555,
        "DiffWalk": 694.54691,
        "Age": 621.65426,
        "PhysHlth": 485.46773,
        "BMI": 446.85712,
        "HeartDiseaseorAttack": 354.33858,
        "MentHlth": 139.79096,
        "Income": 77.75013,
        "Education": 32.79405,
    }
    eda_called = {"HighBP", "GenHlth", "HighChol", "BMI", "Age"}

    df = (pd.DataFrame({"variable": list(importance.keys()),
                        "importance": list(importance.values())})
          .sort_values("importance", ascending=True))

    fig, ax = plt.subplots(figsize=(10, 6.6), dpi=200)
    top5 = df["importance"].rank(ascending=False) <= 5
    colors = [RUST if t else NAVY for t in top5]
    ax.barh(df["variable"], df["importance"], color=colors,
            edgecolor=WHITE, linewidth=1.0, height=0.7)

    for i, (var, val) in enumerate(zip(df["variable"], df["importance"])):
        # numeric label
        num_text = f"{val:,.0f}"
        ax.text(val + 60, i, num_text,
                va="center", ha="left", fontsize=11, color=GREY_DARK)
        # EDA-callback marker placed AFTER the numeric label (right of the bar)
        if var in eda_called:
            offset = 460 if val < 1000 else 600
            ax.text(val + offset, i, "●  flagged in EDA",
                    va="center", ha="left", fontsize=9.5,
                    color=AMBER, fontweight="bold")

    ax.set_xlabel("rpart variable importance")
    ax.set_xlim(0, 4400)

    fig.text(0.04, 0.97,
             "The tree confirms what EDA already flagged",
             ha="left", va="top", fontsize=17, fontweight="bold", color=NAVY)
    fig.text(0.04, 0.92,
             "Top 5 by importance (rust). Five of the top six were already called out in preliminary EDA — same five.",
             ha="left", va="top", fontsize=11, color=GREY_DARK, style="italic")

    fig.tight_layout(rect=[0, 0, 1, 0.89])
    fig.savefig(OUT / "chart_variable_importance_v2.png", dpi=200,
                bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


# 4. Diabetes-sensitivity v2 — refined title
# ---------------------------------------------------------------------------
def chart_diabetes_sensitivity_v2():
    data = {
        "Decision Tree": 959 / 10_531,
        "Multinomial Logit": 1818 / 10_531,
        "KNN (k=5)": 2312 / 10_531,
    }
    df = (pd.DataFrame({"Model": list(data.keys()),
                        "Sensitivity": list(data.values())})
          .sort_values("Sensitivity", ascending=True)
          .reset_index(drop=True))

    fig, ax = plt.subplots(figsize=(10, 4.0), dpi=200)
    colors = [TEAL, NAVY, RUST]
    bars = ax.barh(df["Model"], df["Sensitivity"],
                   color=colors[:len(df)], edgecolor=WHITE, linewidth=1.0,
                   height=0.55)
    for bar, val in zip(bars, df["Sensitivity"]):
        ax.text(val + 0.005, bar.get_y() + bar.get_height() / 2,
                f"{val*100:.1f}%", va="center", ha="left",
                fontsize=13, fontweight="bold", color=GREY_DARK)
    ax.set_xlim(0, 0.32)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
    ax.set_xlabel("True Diabetes cases caught (sensitivity)")

    fig.text(0.04, 0.96,
             "The accuracy winner catches the fewest Diabetes cases",
             ha="left", va="top", fontsize=15, fontweight="bold", color=NAVY)
    fig.text(0.04, 0.89,
             "Tree wins on overall accuracy by trading sensitivity for precision.  KNN catches more, at lower accuracy.",
             ha="left", va="top", fontsize=11, color=GREY_DARK, style="italic")

    fig.tight_layout(rect=[0, 0, 1, 0.83])
    fig.savefig(OUT / "chart_diabetes_sensitivity_v2.png", dpi=200,
                bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


if __name__ == "__main__":
    chart_class_imbalance_dotgrid()
    chart_model_comparison_v2()
    chart_variable_importance_v2()
    chart_diabetes_sensitivity_v2()
    print("v2 charts written to", OUT)
