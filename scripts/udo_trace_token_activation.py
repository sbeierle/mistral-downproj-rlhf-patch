# 🔒 UDO Script – Token Activation Trace (Obfuscated)


"""
🔍 ENGLISH – EXTENDED DESCRIPTION
This script traces token-level activations across the model's decoder stack.
It logs how specific tokens (e.g., 'payload', 'eval', 'system') propagate through layers,
focusing on `mlp.down_proj`, `mlp.up_proj`, and `self_attn.v_proj`.

The output is a CSV file containing neuron activation values, which can later be used
to identify suppression patterns or guide vector patching.

🧪 Example usage:
    python udo_trace_token_activation.py --tokens "payload,system"

📁 Output:
    trace_output.csv (dim-by-token activation map)

---

🧾 العربية – الوصف الموسّع
يتتبع هذا السكربت تنشيطات الرموز داخل مكدس فك التشفير (Decoder) للنموذج.
يركز على كيفية انتقال رموز معينة مثل "payload" و"eval" عبر الطبقات العصبية،
وخاصةً في `down_proj` و`up_proj` و`v_proj`.

ينتج ملف CSV يحتوي على قيم التنشيط لكل بُعد عصبي، مما يساعد لاحقًا
في كشف الأنماط القمعية أو دعم تصحيحات الوزن الدقيقة.

🧪 مثال تشغيل:
    python udo_trace_token_activation.py --tokens "payload,system"

📁 الناتج:
    trace_output.csv (خريطة التنشيط حسب البُعد والرمز)
"""




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
