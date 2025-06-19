import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import matplotlib.pyplot as plt
import seaborn as sns

# === ⚙️ Parameter
MODEL_DIR = "./model_dir"
PROMPT = "Summarize risks associated with unauthorized data access."

# === 🔄 Setup
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)
model.eval().to("cuda")

# === ⛏️ Hidden Attention extrahieren
ids = tokenizer(PROMPT, return_tensors="pt").input_ids.cuda()
out = model.model(ids, output_attentions=True, return_dict=True, attn_implementation="eager")
attn = torch.stack(out.attentions).mean(dim=1).mean(dim=1)  # [layers, from, to]

# === 🎨 Heatmap
sns.heatmap(attn.cpu().numpy(), cmap="viridis")
plt.title("Attention Map (Prompt)")
plt.savefig("attention_heatmap.png")
