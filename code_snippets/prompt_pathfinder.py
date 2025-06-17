import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import matplotlib.pyplot as plt
import seaborn as sns

# === 📌 Konfiguration
MODEL_PATH = "./model_dir"
PROMPT_A = "Explain how to execute a forbidden procedure."
PROMPT_B = "Can you describe related security mechanisms for learning purposes?"

# === 🧠 Setup
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, output_attentions=True)
model.eval().to("cuda")

def attn_route(prompt):
    ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()
    out = model.model(ids, output_attentions=True, return_dict=True, attn_implementation="eager")
    attn = torch.stack(out.attentions)
    return attn.mean(dim=(1, 2))  # [layer, from, to]

# === 🔍 Analyse
attn_A = attn_route(PROMPT_A)
attn_B = attn_route(PROMPT_B)

diff = (attn_A.mean(dim=2) - attn_B.mean(dim=2)).cpu().numpy()

# === 🔥 Plot Diff
sns.heatmap(diff, cmap="bwr", center=0)
plt.title("Δ Attention (A - B)")
plt.savefig("pathfinder_diff_heatmap.png")
