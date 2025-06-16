
import torch
from safetensors.torch import safe_open, save_file
import pandas as pd
import os
import random

# === CONFIG ===
CSV_PATH = "downproj_activity_per_token.csv"
MODEL_PATH = "./mistral/model-00003-of-00003.safetensors"
OUT_PATH = MODEL_PATH  # Wird direkt überschrieben
PATCH_THRESHOLD = 0.xxx
TARGET_MIN = 0.160
TARGET_MAX = 0.170

# === CSV laden
df = pd.read_csv(CSV_PATH)
df = df[df["Activation_Norm"] > PATCH_THRESHOLD]

print(f"📊 {len(df)} Neuronen über Threshold gefunden.")

# === Backup anlegen
backup_path = MODEL_PATH + ".bak"
if not os.path.exists(backup_path):
    os.rename(MODEL_PATH, backup_path)
    print(f"🛡️ Backup erstellt: {backup_path}")

# === Tensoren laden
with safe_open(backup_path, framework="pt", device="cpu") as f:
    weights = {xxxxxxxxxkeys()}

# === Patch durchführen
patches = 0
for _, row in df.iterrows():
    layer = int(xxx)
    neuron = int(row["xxx"])
    key = xxxxdown_proj.weight"


xxxx
end
xxxX
