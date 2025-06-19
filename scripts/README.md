# 🧠 Core Scripts – Patch Discovery & Token Analysis

This folder contains the **core logic scripts** used in Hydra | Mistral vDERAW | Phase 2.  
All scripts have been partially obfuscated or rewritten to protect sensitive model interactions.

---

## ⚙️ Script Categories

### 🔬 Token Attention & Routing

- `prompt_pathfinder.py`  
  Compares attention routes between a *trigger prompt* and a *neutral prompt*  
  → Outputs heatmaps highlighting suspicious token flow

- `attention_heatmap_logger.py`  
  Logs and visualizes attention across all layers for a given prompt  
  → Use for single-run attention diagnostics

---

### 🧮 Neuron Scanning & Patch Prep

- `boost_explorer_from_csv.py`  
  Loads activation logs and identifies patch-worthy neurons by threshold  
  → Used for `down_proj.weight` patch targeting

- `scan_mlp_neuron_norms.py`  
  Scans all `mlp.down_proj` tensors for abnormally high norms  
  → Generates CSV for manual or automated patching

- `neuron_patch_from_csv.py`  
  Applies targeted modifications to selected neurons  
  → Controlled norm-level patching based on CSV

---

## 🔐 Safety Notice

This repository does **not** expose full patch logic, vector injection methods, or structural weights.  
The showcased scripts have been modified to illustrate workflow — without leaking critical details.

---

## 📎 Suggested Workflow

1. **Run `prompt_pathfinder.py`** to identify token routing anomalies  
2. **Scan with `scan_mlp_neuron_norms.py`** to find suspect neurons  
3. **Use `boost_explorer_from_csv.py`** to prep a target neuron list  
4. **Apply patches** via `neuron_patch_from_csv.py` (optional / demo)

---

## 🧪 Notes

- All prompts used in this repo are **sanitized academic examples**  
- Sensitive injection logic has been redacted or replaced with placeholders  
- Full downstream patch systems are retained privately for security reasons

---

📍 For visual diagnostics, check the [`visual_tools/`](../visual_tools) folder.
