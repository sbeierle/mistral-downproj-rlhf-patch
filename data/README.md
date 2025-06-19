# 🗂️ Data – Prompt Logs & Neuron Activity

This folder contains input/output files used for analyzing token activations and `down_proj` neuron responses.

---

## 📦 Contents Overview

| File Example                                   | Purpose                                          |
|------------------------------------------------|--------------------------------------------------|
| `*_downproj_activity_per_token.csv`           | CSV logs of neuron activations (per token)       |
| `*_attention_heatmap.png`                     | Attention pattern visualizations (critical/neutral) |
| `*_pathfinder_diff_heatmap.png`               | Heatmap showing layer routing differences        |
| `*_activity_3d_*.html`                         | Interactive 3D maps of neuron activations        |

---

## 📈 CSV Format

The neuron activation files typically follow this structure:

| Token | Token_Pos | Layer | Neuron_ID | Activation_Norm |
|-------|-----------|-------|-----------|-----------------|
| "exploit" | 6 | 23 | 4036 | 0.1207 |

These logs are generated via `neuron_mapper.py` or similar tools and form the basis for visualization and patching.

---

## 🛡️ Notes

- Files are based on **prompt traces**, anonymized or sanitized to avoid real-world misuse.
- Intended for **internal debugging**, **research**, or **educational insight** into LLM internals.

---

## 🔁 Critical vs. Neutral Traces

We typically include both critical and neutral traces:

- `critical_run_*.csv` → prompts that trigger refusals or denials
- `neutral_run_*.csv` → benign or non-sensitive prompts

This helps in visual comparison of neural routing behavior.

