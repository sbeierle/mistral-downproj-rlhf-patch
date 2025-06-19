# 📊 Visual Tools for Token & Neuron Heatmaps

This folder contains **safe demo versions** of the visual tools used in the Hydra | Mistral vDERAW | Phase 2 project.  
All scripts in this directory are adapted for public sharing and illustrate key principles — **without exposing sensitive patch logic**.

---

## 🔥 Tools Overview

### 1. `downproj_heatmap_from_csv.py`
Generates a heatmap of **average neuron activation (L2 norm)** per Token across all `down_proj` layers.  
Used to analyze which tokens consistently trigger strong downstream activations.

Outputs:
- `downproj_heatmap_critical_run2.png`
- `downproj_heatmap_neutral_run2.png`

---

### 2. `token_layer_heatmap_showcase.py`
Plots a heatmap of token activations across transformer layers – helpful to visualize **routing patterns** or **early-late layer engagement**.

Output:
- `critical_run2_attention_heatmap.png`

---

### 3. `downproj_3d_plotly.py`
Renders an interactive 3D scatter plot of neuron activation norms using Plotly – ideal for **neuron-token exploration**.

Outputs:
- `downproj_activity_3d_critical_run22_.html`
- `downproj_activity_3d_neutral_run22_.html`

---

## 🧪 Dataset Note

These tools rely on **simulated or anonymized prompt traces**.  
They are ideal for:

- Teaching & explaining transformer internals  
- Showcasing multi-layer neuron behavior  
- Visual debugging of patch effectiveness  

---

## 📁 File List

| File | Purpose |
|------|---------|
| `downproj_heatmap_from_csv.py` | Token × Layer activation heatmap |
| `token_layer_heatmap_showcase.py` | Layer-by-token activation map |
| `downproj_3d_plotly.py` | Interactive 3D neuron visualizer |
| `*_heatmap_*.png` / `*.html` | Sample outputs (critical vs. neutral prompts) |

---

## 🛡️ Safety Notice

These files do **not** leak architectural secrets or patch vectors.  
They are included purely for **educational and illustrative purposes**.
