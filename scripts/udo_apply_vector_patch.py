# scripts/udo_apply_vector_patch.py

from safetensors import safe_open
import numpy as np
import sys, csv

model_path = sys.argv[1]  # e.g., 'mistral/model-00003-of-00003.safetensors'
patch_csv = sys.argv[2]   # e.g., 'data/downproj_patch.csv'
target_key = "model.layers.{L}.mlp.down_proj.weight"

with safe_open(model_path, framework="pt", device="cpu") as f:
    tensors = {k: f.get_tensor(k) for k in f.keys()}

with open(patch_csv, "r") as f:
    entries = list(csv.DictReader(f))

for e in entries:
    l = int(e["layer"])
    d = int(e["dim"])
    delta = float(e["delta"])
    key = target_key.replace("{L}", str(l))
    tensors[key][d, :] += delta

from safetensors.torch import save_file
save_file(tensors, model_path.replace(".safetensors", ".patched.safetensors"))

print(f"[✓] Patched saved to: {model_path.replace('.safetensors', '.patched.safetensors')}")
