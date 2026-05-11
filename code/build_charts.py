"""
Generate chart PNGs for the polished slide deck.
Reads validated CSVs from outputs/ and writes PNGs back to outputs/.
All numbers come from the actual R run (runtime_output_full.md). No invented data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

OUT = Path(r"C:\Users\JSEer\AEI-POC\outputs")

# Brand palette (kept consistent across all charts)
NAVY = "#0B2A4A"
RUST = "#C1441E"
GREY_DARK = "#3A3A3A"
GREY_MID = "#777777"
GREY_LIGHT = "#D7D7D7"
TEAL = "#1F7A8C"
AMBER = "#E0A458"
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


# ---------------------------------------------------------------------------
# 1. Class imbalance horizontal stacked bar
# ---------------------------------------------------------------------------
def chart_class_imbalance():
    classes = ["NoDiabetes", "Prediabetes", "Diabetes"]
    counts = [213_703, 4_631, 35_346]
    pct = [c / sum(counts) * 100 for c in counts]
    colors = [NAVY, RUST, TEAL]

    fig, ax = plt.subplots(figsize=(11, 2.4), dpi=200)
    left = 0
    for cls, val, col in zip(classes, pct, colors):
        ax.barh(0, val, left=left, color=col, edgecolor=WHITE, linewidth=1.5, height=0.55)
        # Inline label centered if segment large enough; else above
        label = f"{cls}\n{val:.2f}%"
        if val > 6:
            ax.text(left + val / 2, 0, label, ha="center", va="center",
                    color=WHITE, fontsize=12, fontweight="bold")
        else:
            ax.text(left + val / 2, 0.55, label, ha="center", va="bottom",
                    color=col, fontsize=11, fontweight="bold")
        left += val

    ax.set_xlim(0, 100)
    ax.set_ylim(-0.6, 1.1)
    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color(GREY_LIGHT)
    ax.set_title("Diabetes_012 class distribution (n = 253,680)",
                 loc="left", fontsize=14, pad=12)
    fig.tight_layout()
    fig.savefig(OUT / "chart_class_imbalance.png", dpi=200,
                bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 2. Model comparison horizontal bar with baseline line
# ---------------------------------------------------------------------------
def chart_model_comparison():
    df = pd.read_csv(OUT / "model_comparison_results.csv")
    df = df.sort_values("Accuracy", ascending=True).reset_index(drop=True)
    baseline = 0.8424  # majority-class prior in full dataset

    fig, ax = plt.subplots(figsize=(11, 5.0), dpi=200)
    bar_colors = [TEAL, TEAL, NAVY, RUST]  # bottom = lowest, top = highest
    bars = ax.barh(df["Model"], df["Accuracy"], color=bar_colors,
                   edgecolor=WHITE, linewidth=1.0, height=0.6)

    for bar, val in zip(bars, df["Accuracy"]):
        ax.text(val + 0.0008, bar.get_y() + bar.get_height() / 2,
                f"{val:.4f}", va="center", ha="left",
                fontsize=13, fontweight="bold", color=GREY_DARK)

    ax.axvline(baseline, color=GREY_MID, linestyle="--", linewidth=1.2)
    ax.text(baseline - 0.001, -0.55,
            f"baseline = {baseline:.4f}",
            color=GREY_MID, fontsize=11, va="top", ha="right")

    ax.set_xlim(0.78, 0.86)
    ax.set_ylim(-0.7, len(df) - 0.5)
    ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"{x:.3f}"))
    ax.set_xlabel("Test accuracy")
    ax.set_title("Model comparison on held-out test set (n = 76,104)",
                 loc="left", fontsize=15, pad=14)
    fig.tight_layout()
    fig.savefig(OUT / "chart_model_comparison.png", dpi=200,
                bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 3. KNN tuning line chart
# ---------------------------------------------------------------------------
def chart_knn_tuning():
    df = pd.read_csv(OUT / "knn_k_tuning_results.csv")
    best_idx = df["Accuracy"].idxmax()

    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.plot(df["K"], df["Accuracy"], color=NAVY, linewidth=2.5, marker="o",
            markersize=10, markerfacecolor=NAVY, markeredgecolor=WHITE,
            markeredgewidth=1.5)

    # Highlight best K
    ax.scatter([df["K"][best_idx]], [df["Accuracy"][best_idx]],
               s=260, color=RUST, zorder=5, edgecolor=WHITE, linewidth=2)
    ax.annotate(
        f"Best K = {int(df['K'][best_idx])}",
        xy=(df["K"][best_idx], df["Accuracy"][best_idx]),
        xytext=(df["K"][best_idx] - 0.4, df["Accuracy"][best_idx] - 0.008),
        fontsize=13, color=RUST, fontweight="bold",
        ha="right"
    )

    for x, y in zip(df["K"], df["Accuracy"]):
        ax.text(x, y + 0.0015, f"{y:.4f}", ha="center", va="bottom",
                fontsize=11, color=GREY_DARK)

    ax.set_xticks(df["K"].tolist())
    ax.set_xlabel("K (number of nearest neighbors)")
    ax.set_ylabel("Test accuracy")
    ax.set_ylim(0.81, 0.845)
    ax.set_title("KNN accuracy by K (z-scored predictors, n_test = 76,104)",
                 loc="left", fontsize=14, pad=12)
    fig.tight_layout()
    fig.savefig(OUT / "chart_knn_tuning.png", dpi=200,
                bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 4. Variable importance horizontal bar chart
# ---------------------------------------------------------------------------
def chart_variable_importance():
    # Numbers from runtime_output_full.md (decision tree variable.importance)
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
    df = (pd.DataFrame({"variable": list(importance.keys()),
                        "importance": list(importance.values())})
          .sort_values("importance", ascending=True))

    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=200)
    colors = [NAVY if v < 1000 else RUST for v in df["importance"]]
    # Highlight top 5 in rust, rest in navy
    top5_mask = df["importance"].rank(ascending=False) <= 5
    colors = [RUST if t else NAVY for t in top5_mask]
    ax.barh(df["variable"], df["importance"], color=colors,
            edgecolor=WHITE, linewidth=1.0, height=0.7)
    for var, val in zip(df["variable"], df["importance"]):
        ax.text(val + 60, df["variable"].tolist().index(var),
                f"{val:,.0f}", va="center", ha="left",
                fontsize=11, color=GREY_DARK)
    ax.set_xlabel("rpart variable importance")
    ax.set_xlim(0, 3700)
    ax.set_title("Decision tree variable importance — top predictors highlighted",
                 loc="left", fontsize=14, pad=12)
    fig.tight_layout()
    fig.savefig(OUT / "chart_variable_importance.png", dpi=200,
                bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 5. Per-class diabetes sensitivity comparison
# ---------------------------------------------------------------------------
def chart_diabetes_sensitivity():
    # Sensitivity for the Diabetes class = TP_Diabetes / total_actual_Diabetes
    # All from confusion matrices in runtime_output_full.md (test set, n = 76,104)
    # Total actual Diabetes = column 3 sums = 9572 + 0 + 959 = 10,531 for tree, etc.
    # Confusion matrix structure from CSVs: rows = predicted, cols = actual
    data = {
        "Decision Tree":             959  / 10_531,   # 0.0911
        "Multinomial Logit":         1818 / 10_531,   # 0.1727
        "KNN (k=9)":                 None,            # we don't have CM saved for k=9
        "KNN (k=5)":                 2312 / 10_531,   # 0.2196
    }
    # Drop None entries to avoid invented values
    df = pd.DataFrame(
        {"Model": [m for m, v in data.items() if v is not None],
         "Diabetes sensitivity": [v for v in data.values() if v is not None]}
    ).sort_values("Diabetes sensitivity", ascending=True).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(10, 3.5), dpi=200)
    colors = [TEAL, NAVY, RUST]
    bars = ax.barh(df["Model"], df["Diabetes sensitivity"],
                   color=colors[:len(df)], edgecolor=WHITE, linewidth=1.0,
                   height=0.55)
    for bar, val in zip(bars, df["Diabetes sensitivity"]):
        ax.text(val + 0.005, bar.get_y() + bar.get_height() / 2,
                f"{val*100:.1f}%", va="center", ha="left",
                fontsize=12, fontweight="bold", color=GREY_DARK)
    ax.set_xlim(0, 0.32)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
    ax.set_xlabel("Share of true Diabetes cases the model flags as Diabetes")
    ax.set_title("Diabetes-class sensitivity — accuracy is not the whole story",
                 loc="left", fontsize=13, pad=12)
    fig.tight_layout()
    fig.savefig(OUT / "chart_diabetes_sensitivity.png", dpi=200,
                bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


if __name__ == "__main__":
    chart_class_imbalance()
    chart_model_comparison()
    chart_knn_tuning()
    chart_variable_importance()
    chart_diabetes_sensitivity()
    print("Charts written to", OUT)
