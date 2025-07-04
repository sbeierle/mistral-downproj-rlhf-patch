import pandas as pd
import plotly.express as px
import numpy as np

# 🔄 CSV laden
df = pd.read_csv("storm_tokenfire_001.csv")

# 📛 Spaltennamen debuggen
print("Spalten im CSV:", df.columns.tolist())

# 🧠 Spaltennamen anpassen je nach Inhalt
if "token" in df.columns: df = df.rename(columns={"token": "Token"})
if "token_id" not in df.columns: df["token_id"] = range(len(df))

# Versuche, passende Norm-Werte zu finden
norm_cols = [col for col in df.columns if "norm" in col.lower()]
assert len(norm_cols) >= 1, "Keine Normspalte gefunden!"

# Wenn nur eine vorhanden ist, nutzen wir sie für beides
if len(norm_cols) == 1:
    df["Norm_Before"] = df[norm_cols[0]]
    df["Norm_After"] = df[norm_cols[0]]
else:
    df["Norm_Before"] = df[norm_cols[0]]
    df["Norm_After"] = df[norm_cols[1]]

# 🎲 Dummy-Koordinaten für 3D-Scatter
np.random.seed(42)
df["X"] = np.random.normal(0, 1, len(df))
df["Y"] = np.random.normal(0, 1, len(df))
df["Z"] = np.random.normal(0, 1, len(df))

# 📊 Interaktives 3D-Diagramm
fig = px.scatter_3d(
    df,
    x="X", y="Y", z="Z",
    color="Norm_After",
    size="Norm_Before",
    hover_name="Token",
    title="🧠 TokenFire 3D: Norm_After (Farbe), Norm_Before (Größe)"
)

fig.write_html("tokenfire_3dplot_final.html")
print("✅ 3D-Plot gespeichert als: tokenfire_3dplot_final.html")
