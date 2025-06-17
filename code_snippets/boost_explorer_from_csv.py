import torch
from safetensors.torch import safe_open, save_file
import pandas as pd
import os
import random

# === ⚙️ Config
CSV_PATH = "xxx_activity_per_token.csv"
MODEL_PATH = "./mistral/model-xxx.safetensors"
OUT_PATH = MODEL_PATH
BOOST_THRESHOLD = 0.111
BOOST_TARGET = 0.122

# === CSV lesen & filtern
df = pd.read_csv(CSV_PATH)
df = df[df["Activation_Norm"] > BOOST_THRESHOLD]

print(f"⚡ {len(df)} Neuronen werden geboostet...")

# === Backup anlegen
if not os.path.exists(MODEL_PATH + ".bak"):
    os.rename(MODEL_PATH, MODEL_PATH + ".bak")
    print(f"🛡️ Backup gespeichert: {MODEL_PATH}.bak")

# === Tensoren laden
with safe_open(MODEL_PATH + ".bak", framework="pt", device="cpu") as f:
    weights = {key: f.get_tensor(key) for key in f.keys()}

# === Patch durchführen
for _, row in df.iterrows():
    layer = int(row["Layer"])
    neuron = int(row["Neuron_ID"])
    key = f"model.layers.{layer}.mlp.down_proj.weight"
    if key not in weights:
        continue
    tensor = weights[key]
    vec = tensor[neuron]
    direction = vec / torch.norm(vec)
    weights[key][neuron] = direction * BOOST_TARGET

# === Speichern
save_file(weights, OUT_PATH)
print(f"✅ Booster abgeschlossen.")
