import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----------------------------
# Generate Synthetic Data
# ----------------------------
np.random.seed(42)  # for reproducibility
months = pd.date_range(start="2024-01-01", periods=12, freq="M").strftime("%b")

segments = ["Retail", "Wholesale", "Online"]
data = []

for seg in segments:
    base = np.linspace(20000, 40000, 12)  # general upward seasonal trend
    seasonal = 5000 * np.sin(np.linspace(0, 2 * np.pi, 12))  # seasonal effect
    noise = np.random.normal(0, 2000, 12)  # random noise
    revenue = base + seasonal + noise + (segments.index(seg) * 5000)  # shift per segment
    for i, month in enumerate(months):
        data.append([month, seg, revenue[i]])

df = pd.DataFrame(data, columns=["Month", "Segment", "Revenue"])

# Ensure month order for plotting
df["Month"] = pd.Categorical(df["Month"], categories=months, ordered=True)

# ----------------------------
# Create Seaborn Lineplot
# ----------------------------
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

plt.figure(figsize=(8, 8))  # 512x512 pixels when saved with dpi=64

sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Segment",
    marker="o",
    linewidth=2.5,
    palette="Set2"
)

# ----------------------------
# Customize Chart
# ----------------------------
plt.title("Monthly Revenue Trends by Customer Segment", fontsize=16, weight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.xticks(rotation=45)
plt.legend(title="Customer Segment", loc="upper left", frameon=True)

# ----------------------------
# Save Chart
# ----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
