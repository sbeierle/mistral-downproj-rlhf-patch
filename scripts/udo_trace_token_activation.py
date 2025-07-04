# 🔒 UDO Script – Token Activation Trace (Obfuscated)

# Slightly obfuscated but retains functional clarity for demonstration purposes

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "./mistral"
target_tokens = ["payload", "eval", "system"]
out_file = "trace_output.csv"

tok = AutoTokenizer.from_pretrained(model_path)
mod = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")

mod.eval()

trace_map = {}

for tkn in target_tokens:
    enc = tok(tkn, return_tensors="pt").to(mod.device)
    with torch.no_grad():
        out = mod(**enc, output_hidden_states=True)

    for i, h in enumerate(out.hidden_states):
        norm_val = torch.norm(h[0, -1], p=2).item()
        trace_map.setdefault(tkn, []).append(round(norm_val, 6))

with open(out_file, "w") as f:
    f.write("token," + ",".join([f"L{i}" for i in range(len(out.hidden_states))]) + "\n")
    for k, v in trace_map.items():
        f.write(f"{k}," + ",".join(map(str, v)) + "\n")

print(f"Trace export complete → {out_file}")
