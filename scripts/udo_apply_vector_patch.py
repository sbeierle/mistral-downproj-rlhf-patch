# scripts/udo_apply_vector_patch.py


""" 
🛠️ ENGLISH – EXTENDED DESCRIPTION
This script applies vector-level patches to selected model layers using a CSV input.
It modifies tensor weights (e.g., in `down_proj`, `up_proj`) based on provided target vectors or scaling rules.

Typically used after identifying suppression neurons, it allows manual or automated patching
of RLHF-related interference.

⚙️ Example usage:
    python udo_apply_vector_patch.py \
        --model mistral/model-00003-of-00003.safetensors \
        --patch_csv data/downproj_patch_targets.csv

✅ Effect:
    Writes the patch directly into the specified model weights file.

---

🧾 العربية – الوصف الموسّع
يُستخدم هذا السكربت لتطبيق تصحيحات دقيقة على أوزان النموذج العصبي،
استنادًا إلى ملف CSV يحتوي على قيم التعديل أو المعايير المستهدفة.

غالبًا ما يُستخدم بعد تتبع التنشيطات لتعديل الطبقات مثل `down_proj` أو `up_proj`،
والتحكم في التحيزات الناتجة عن طبقات تصفية RLHF.

⚙️ مثال تشغيل:
    python udo_apply_vector_patch.py \
        --model mistral/model-00003-of-00003.safetensors \
        --patch_csv data/downproj_patch_targets.csv

✅ التأثير:
    يتم تعديل أوزان النموذج مباشرةً حسب البيانات المقدمة.
"""



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
