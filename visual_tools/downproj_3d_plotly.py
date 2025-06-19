# downproj_3d_plotly.py
import pandas as pd
import plotly.express as px 

# === 🔧 CSV-Datei setzen
CSV_PATH = "neutral_run_2_downproj_activity_per_token.csv"  # oder "neutral_run_2..."
OUTPUT_HTML = "downproj_activity_3d_neutral_run22_.html"

# === 📥 Daten laden
df = pd.read_csv(CSV_PATH)

# ✏️ Token-Position optional als String (für klarere Achsen)
df["Token_Pos"] = df["Token_Pos"].astype(str)

# === 📊 3D-Plot erzeugen
fig = px.scatter_3d(
    df,
    x="Token",                # Token Text
    y="Layer",                # Layer
    z="Activation_Norm",      # Normwert
    color="Activation_Norm",
    size="Activation_Norm",
    hover_data=["Neuron_ID"],
    title="🧠 DownProj Neuron Activation – 3D Visual",
    color_continuous_scale="plasma",
    height=800
)

fig.update_layout(scene=dict(
    xaxis_title='Token',
    yaxis_title='Layer',
    zaxis_title='Activation Norm'
))
fig.write_html(OUTPUT_HTML)
print(f"✅ Interaktive Grafik gespeichert: {OUTPUT_HTML}")
