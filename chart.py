# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data for 12 months across 3 customer segments
np.random.seed(42)
months = pd.date_range("2024-01-01", periods=12, freq="M").strftime("%b")

segments = ["Retail", "Corporate", "Online"]
data = []

for seg in segments:
    base = np.random.randint(80, 150) * 1000
    seasonal_pattern = (
        base
        + np.sin(np.linspace(0, 2 * np.pi, 12)) * np.random.randint(10000, 20000)
        + np.random.normal(0, 5000, 12)
    )
    for i, month in enumerate(months):
        data.append([month, seg, max(0, int(seasonal_pattern[i]))])

df = pd.DataFrame(data, columns=["Month", "Segment", "Revenue"])

# Ensure month order is correct for plotting
df["Month"] = pd.Categorical(df["Month"], categories=months, ordered=True)

# Create the lineplot
fig, ax = plt.subplots(figsize=(8, 8))  # Base figure
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Segment",
    marker="o",
    palette="Set2",
    linewidth=2.5,
    ax=ax
)

# Customize chart for executive presentation
plt.title("Monthly Revenue Trend Analysis by Customer Segment", fontsize=16, weight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (USD)", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Customer Segment", fontsize=10, title_fontsize=11)

# Force EXACT 512x512 pixels → dpi = pixels / inches
fig.set_size_inches(512/96, 512/96)  # 5.333x5.333 inches
plt.savefig("chart.png", dpi=96)  # 96 dpi × 5.333 in = 512 px
plt.close()
