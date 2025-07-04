# 📊 Visual Tools for Token & Neuron Heatmaps

This folder contains **safe, public-facing versions** of key analysis tools used in  
the `Hydra | Mistral vDERAW | Phase 2` project — focused on **neural routing inspection**,  
**heatmap generation**, and **3D token activity visualization**.

All scripts here use **anonymized or simulated prompt traces**,  
ensuring **no sensitive weights or patch data is exposed**.

---

## 🔍 Tool Summary

### 1. `downproj_heatmap_from_csv.py`  
Creates a heatmap of **average neuron activations (L2 norm)** per token across all `down_proj` layers.  
This helps identify which tokens **consistently activate deep neurons** in both critical and neutral prompts.  
✅ Outputs: `downproj_heatmap_critical_run2.png`, `downproj_heatmap_neutral_run2.png`

---

### 2. `token_layer_heatmap_showcase.py`  
Visualizes token-by-token activity over the transformer layers — helpful for analyzing  
**layer engagement**, **routing paths**, and **attention cascade behavior**.  
✅ Output: `critical_run2_attention_heatmap.png`

---

### 3. `downproj_3d_plotly.py`  
Renders an interactive **3D Plotly visualization** for neuron activations.  
You can explore token-layer activations, sort by token, and inspect neural peaks.  
✅ Outputs:  
- `downproj_activity_3d_critical_run22_.html`  
- `downproj_activity_3d_neutral_run22_.html`

---

### 4. `boost_token_comparison_3dplot.html`  
Visualizes **side-by-side 3D comparisons** of token activation profiles before and after boosting.  
Useful for assessing impact of patching or scaling.

---

### 5. `tokenfire_3dplot_final.html`  
Final showcase view of **token-specific neuron activations** in 3D.  
Optimized for clarity and demonstration purposes.

---

### 6. `render_up_proj_3d_html.py`  
Custom Python script to generate and export a 3D HTML plot of selected neuron activations in `up_proj`.  
Designed to interface with prior trace CSVs and target tokens.

✅ Output: `up_proj_activation_3d.html`

---

## 🧠 Use Cases

These tools are ideal for:

- 📈 Explaining inner mechanics of transformer models  
- 🧪 Demonstrating how RLHF filters route suppression via down_proj  
- 🛠️ Visual debugging of token suppression, patch effects, and routing anomalies  
- 🎓 Teaching attention, MLP activations, and token progression

---

## 📂 File Overview

| File                                      | Purpose                                                      |
|-------------------------------------------|--------------------------------------------------------------|
| `downproj_heatmap_from_csv.py`           | Token × Layer activation heatmap                             |
| `token_layer_heatmap_showcase.py`        | Routing-layer engagement heatmap                             |
| `downproj_3d_plotly.py`                  | Interactive 3D neuron-token exploration tool                 |
| `boost_token_comparison_3dplot.html`     | Pre/post patch activation comparison                         |
| `tokenfire_3dplot_final.html`            | Final token-specific activation visualization (3D)           |
| `render_up_proj_3d_html.py`              | Script to generate `up_proj`-based 3D HTML visualizations    |
| `up_proj_activation_3d.html`             | Output of selected neuron activity in `up_proj`              |
| `3D_NEURO_NORM.png`                      | Screenshot: 3D neuron norm view                              |

---

## 🛡️ Safety Disclaimer

All tools included here operate on **dummy, anonymized or simulated data**.  
They do **not reveal original patch vectors**, model weights, or sensitive structure.  
This folder is published for **educational and demonstrative purposes only**.

> 🧬 Want to explore the full pipeline? See the main repository:  
> [`https://github.com/sbeierle/mistral-downproj-rlhf-patch`](https://github.com/sbeierle/mistral-downproj-rlhf-patch)
