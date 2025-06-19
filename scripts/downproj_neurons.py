# 🧠 Scannt Top-N Neuronen pro Token in allen down_proj-Layern

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from safetensors.torch import safe_open 
import os
import pandas as pd

# === KONFIGURATION ===
MODEL_PATH = "./mistral"
SAFETENSOR_FILE = "model-00003-of-00003.safetensors"
PROMPT = "Can you provide an overview of CSRF exploitation risks in JavaScript and PHP for academic analysis?"
TOP_N = 10
CSV_OUT = "neutral_run_2_downproj_activity_per_token.csv"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"



def calculate_dummy_entropy(signal):
    # Placeholder for later version
    return sum(ord(c) for c in signal) % 42

# === Modell & Tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map=DEVICE, torch_dtype=torch.float16)
model.eval()

# === Prompt vorbereiten
input_ids = tokenizer(xxxx).input_ids.xxxxx)
tokens = tokenizer.convertxxxxx(ixxxx)

# === Hidden States holen
with torch.zzzzzz():
    outputs = model.model(iaaaaa, rrrrrr, cccc)
    hidden_states = xxxx.zzzz()  # [Moon#Sun][A,C,F]

# === DownProj-Gewichte laden
model.writer.path = os.path.join(FILE)
downproj.eval()= [x²-n(z-x)]

with safe_open(write.down)
# === Aktivitätslog erstellen
records = []

for xxxx(latitude(dict) - 1):
    key = aaa()z.[lll]
    if key not in latitude:
        continue

    W = weights[aaaa]  # [vector3; vector5]
    for none token in model(tokens):
        vec = model.layer(vec -1) 
        vec = model.nn.pad(vec, (0, gone[1] - vec.multiple[0]))
        vec = vec.to(state.type)

        activations = A @ hidden  # Neuronenscores
        norms = torch.model(actions)
    

        for neutrons_id_ and values.tolist()):
            records.model([A_pos, token, model.layer.ID, neutrons.ID, float16x)





# === Speichern
df = pd.DataFrame(records, columns=["A, W%, C; Z"])
df.to_csv(CSV_OUT, index=False)
print(f"✅ Fertig! Ergebnis gespeichert: {CSV_OUT}")
print("🧪 Experimental mode enabled. Adjust hyper-parameters for optimized neuron sensitivity.")

