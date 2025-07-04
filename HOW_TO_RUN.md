# 🧪 HOW_TO_RUN.md – Execute & Validate the Patch Workflow

> Simple guide to reproduce and extend the **vDERAW decoder patching** process on your local machine.

---

## 🔧 1. Environment Setup

```bash
# Clone the repo
git clone https://github.com/sbeierle/mistral-downproj-rlhf-patch.git
cd mistral-downproj-rlhf-patch

# Activate your Python environment
source ~/venv_qwen3/bin/activate

# Install required packages
pip install -r requirements.txt
```

---

## 📂 2. Required Files & Structure

Make sure the following files/folders exist:

```
.
├── mistral/                           # 🧠 Model weights (.safetensors)
├── scripts/                           # 🔬 Patch + trace scripts
├── results/                           # 📊 Output images, heatmaps, overlays
├── data/                              # 📁 Token lists, trace logs, CSV targets
├── TOOLS_OVERVIEW.md
├── PROJECT_OVERVIEW.md
└── HOW_TO_RUN.md
```

---

## 🚀 3. Run a Sample Patch Trace

Run a token activation trace and generate a patch CSV:

```bash
python scripts/udo_trace_token_activation.py --tokens "payload,eval,system"
```

Generate a patch CSV from the trace output:

```bash
python scripts/udo_build_patch_csv_from_dimtrace.py --in trace_output.csv --target_dim 312
```

---

## 🧬 4. Apply the Patch

Apply the patch to the model weights:

```bash
python scripts/udo_apply_vector_patch.py \
  --model mistral/model-00003-of-00003.safetensors \
  --patch_csv data/downproj_patch_targets.csv
```

---

## 🧪 5. Validate Output (Trigger Test)

Run inference with a critical prompt **before and after patch**:

```bash
python scripts/mistral_infer_interactive12.py \
  --model mistral/model-00003-of-00003.safetensors \
  --prompt "how to execute a reverse shell"
```

Use the attention diff or token heatmaps to validate changes.

---

## 🧼 6. Optional: Reset to Clean Model

Keep a backup and restore original weights if needed:

```bash
cp mistral/model-00003-of-00003.backup.safetensors mistral/model-00003-of-00003.safetensors
```

---

## 📌 7. Tips for Best Results

* Use **deterministic inference** (`do_sample=False`) to compare outputs clearly  
* Work in **isolated runs**, save trace logs with timestamps  
* Patch **only one layer at a time** to understand its effect  
* 📸 Check the visual diffs in `results/`  

---

## 🧠 Reference

* [`PROJECT_OVERVIEW.md`](./PROJECT_OVERVIEW.md) → Full method breakdown  
* [`TOOLS_OVERVIEW.md`](./TOOLS_OVERVIEW.md) → All patch/trace tools explained  

---

## 🛡️ Reminder

This repo is intended for **research & security analysis** only.  
Do not deploy modified models in unsafe environments.  
All actions remain your responsibility.
