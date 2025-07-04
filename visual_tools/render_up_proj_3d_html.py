import pandas as pd
import plotly.express as px

# Lokaler Pfad zur CSV-Datei
csv_path = "./path_sweep_up_proj.csv"

# CSV einlesen
df = pd.read_csv(csv_path)

# Sicherheitsprüfung & Casting
if "activation" not in df.columns and "value" in df.columns:
    df["activation"] = pd.to_numeric(df["value"], errors="coerce")

df["layer"] = pd.to_numeric(df["layer"], errors="coerce")
df["dim"] = pd.to_numeric(df["dim"], errors="coerce")
df = df.dropna(subset=["layer", "dim", "activation"])

# 3D-Scatterplot mit Plotly
fig = px.scatter_3d(
    df,
    x="layer",
    y="dim",
    z="activation",
    color="activation",
    color_continuous_scale="Viridis",
    title="🔥 UpProj 3D Activation Map – Token-Neuronen pro Layer",
    labels={
        "layer": "Layer",
        "dim": "Neuron-Dimension (Post-Gate)",
        "activation": "Aktivierungswert"
    },
    height=850,
    width=1100
)

# Optik anpassen
fig.update_traces(marker=dict(size=3, opacity=0.7))
fig.update_layout(scene=dict(
    xaxis_title='Transformer Layer',
    yaxis_title='Neuron Dimension',
    zaxis_title='Activation'
))

# HTML-Datei lokal speichern
fig.write_html("up_proj_activation_3d.html")
print("✅ Interaktive 3D-HTML gespeichert als: up_proj_activation_3d.html")
