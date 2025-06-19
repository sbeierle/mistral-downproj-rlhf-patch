# 📁 results – Output Visuals & CSV Logs

This folder contains **outputs** from various scan & patch routines.  
It includes attention heatmaps, downproj activation maps, 3D plots, and token-wise CSV logs.

---

## 🧠 Heatmaps

### Attention-Based

- `attention_trigger.png`  
  → Attention map of a *critical* (trigger) prompt  
- `attention_neutral.png`  
  → Comparison map with a *neutral* prompt  
- `pathfinder_diff_heatmap.png`  
  → Visual difference: trigger minus neutral

### DownProj-Based

- `downproj_heatmap_critical_run2.png`  
  → Top-layer activations for trigger prompt  
- `downproj_heatmap_neutral_run2.png`  
  → Token activation under neutral conditions

---

## 🌐 3D Interactive Visuals

- `downproj_activity_3d_critical_run22_.html`  
- `downproj_activity_3d_neutral_run22_.html`  
→ Interactive neuron-token visualizations (Plotly)

Open directly in your browser!

---

## 📊 CSV Logs

- `critical_run_2_downproj_activity_per_token.csv`  
- `neutral_run_2_downproj_activity_per_token.csv`  
→ Per-token activations and dominant neurons in `mlp.down_proj`  
→ Used for visualization & patch targeting

---

## 🔒 Internal Use Notes

- All logs and heatmaps were generated **post-inference** using sanitized prompts.  
- Any norm or vector patching was done **offline**, based on these logs.  
- Files are stored here for transparency, demo purposes, and reproducibility.

---

✅ This folder is **read-only** and **not required** to run the core patch logic.  
If you want to explore how these files were generated, check:

👉 [`scripts/`](../scripts) and [`visual_tools/`](../visual_tools)

