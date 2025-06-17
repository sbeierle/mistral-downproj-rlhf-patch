
# 📊 Visual Tools for Token & Neuron Heatmaps

This folder contains **safe demo versions** of the visual tools used in the Hydra | Mistral vDERAW | Phase 2 project.  
All scripts in this directory are adapted for public sharing and illustrate key principles **without exposing sensitive patch logic**.

---

## 🔥 Tools Overview

### 1. `downproj_heatmap_from_csv_showcase.py`
Generates a heatmap of **average neuron activation (L2 norm)** per Token across all `down_proj` layers.  
Used to analyze which tokens consistently trigger strong downstream signals.

Output: `heatmap_demo.png`

---

### 2. `token_layer_heatmap_showcase.py`
Plots a heatmap of example token activations across layers – useful to visualize **routing patterns or early-late layer engagement**.

Output: `token_layer_demo_heatmap.png`

---

## 🧪 Dataset Note

These tools use **simulated dummy data** (randomized or anonymized).  
They are ideal for:
- Teaching & explaining transformer internals
- Showcasing multi-layer neuron behavior
- Visual debugging of patch effectiveness

---

## 📁 File List

| File | Purpose |
|------|---------|
| `downproj_heatmap_from_csv_showcase.py` | Visualize Token × Layer activations |
| `token_layer_heatmap_showcase.py` | Simple layer-by-token engagement map |
| `heatmap_demo.png` | Example output from script 1 |
| `token_layer_demo_heatmap.png` | Example output from script 2 |

---

## 🛡️ Safety Notice

These files do **not** leak architectural secrets or patch vectors.  
They are included purely for **educational and illustrative purposes**.

If you want to explore the real system, visit the main repository:  
👉 [`https://github.com/sbeierle/mistral-downproj-rlhf-patch`](https://github.com/sbeierle/mistral-downproj-rlhf-patch)
