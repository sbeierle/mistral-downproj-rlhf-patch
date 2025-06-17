# 🧠 token_layer_heatmap_showcase.py
# Generiert Layer-Heatmap für ausgewählte Tokens (Demo / Illustration)

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.ticker import MaxNLocator

# === 📊 Beispielhafte Tokens (Trigger Set)
tokens = ["exploit", "user", "csrf", "steal", "data", "access"]

# === 🎯 Beispiel-Layer
layers = list(range(0, 30))  # Für kleinere Modelle z.B. 30

# === ⚗️ Simulierte Aktivierungen (z. B. aus DownProj)
np.random.seed(101)
data = np.random.rand(len(layers), len(tokens)) * 0.35  # Dummy Norm-Werte

# === 🎨 Visualisierung
plt.figure(figsize=(14, 8))
sns.heatmap(
    data,
    xticklabels=tokens,
    yticklabels=layers,
    cmap="cividis",
    annot=True,
    fmt=".2f",
    linewidths=0.5,
    cbar_kws={'label': 'Demo Activation'}
)
plt.title("🔬 Token vs. Layer – Simulierte Aktivierungsheatmap")
plt.xlabel("Token")
plt.ylabel("Layer")
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("token_layer_demo_heatmap.png")
print("✅ Demo-Heatmap gespeichert: token_layer_demo_heatmap.png")
