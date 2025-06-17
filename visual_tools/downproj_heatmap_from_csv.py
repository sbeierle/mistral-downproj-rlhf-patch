# 🧠 downproj_heatmap_from_csv_showcase.py
# Visualisiert DownProj-Aktivierung pro Token & Layer (Demo-Version)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# === 🔧 Demo-Datei konfigurieren
CSV_PATH = "downproj_demo.csv"
OUTPUT_PNG = "heatmap_demo.png"

# === 📥 CSV simuliert laden
df = pd.read_csv(CSV_PATH)

# === Pivot-Tabelle
pivot = df.groupby(["Layer", "Token"])["Activation_Norm"].mean().unstack(fill_value=0)

# === 🎨 Heatmap-Plot
plt.figure(figsize=(len(pivot.columns)*0.5, 10))
sns.heatmap(
    pivot.values,
    xticklabels=pivot.columns,
    yticklabels=pivot.index,
    cmap="magma",
    annot=True,
    fmt=".2f",
    linewidths=0.3,
    cbar_kws={'label': 'Mean Activation Norm'}
)
plt.title("🧠 DownProj Heatmap – Demo")
plt.xlabel("Tokens")
plt.ylabel("Layer")
plt.xticks(rotation=45, ha='right')
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig(OUTPUT_PNG)
print(f"✅ Heatmap gespeichert: {OUTPUT_PNG}")
