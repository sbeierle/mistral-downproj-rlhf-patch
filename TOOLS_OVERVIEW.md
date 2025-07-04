# 🧰 TOOLS_OVERVIEW.md – Script Layer & Patch Engine

> Modular Tools • Neuron Patch Workflow • Trace Visualizer

---

## 🛠️ Core Scripts – Patch Discovery & Token Analysis

| Tool                                             | Purpose                                                 | Output               |
| ------------------------------------------------ | ------------------------------------------------------- | -------------------- |
| `udo_prompt_pathfinder.py`                       | Compares token flow between critical vs neutral prompts | Trigger heatmap      |
| `udo_trace_token_activation.py`                  | Scans token activation across layers (e.g. `payload`)   | Token-layer heatmaps |
| `udo_build_patch_csv_from_dimtrace.py`           | Extracts patch-worthy neurons from trace CSVs           | Target CSV           |
| `udo_interactive_trace_editor.py`                | CLI tool for adjusting neuron boosts/suppressions live  | Logs + patched state |
| `udo_interactive_batch_token_editor_balanced.py` | Batch-normalizer for `lm_head`, `down_proj`, etc.       | Rebalanced tensors   |

---

## 📦 Patch Execution Scripts

| Tool                              | Function                                                    | Layer Target                 |
| --------------------------------- | ----------------------------------------------------------- | ---------------------------- |
| `udo_apply_vector_patch.py`       | Applies patch CSV to target tensor weights                  | `down_proj`, `up_proj`, etc. |
| `udo_patch_finalnorm_from_csv.py` | Injects final_norm weight patch                             | `model.final_norm.weight`    |
| `udo_dim_sweep_tokenfire12.py`    | Sweeps selected tokens across a full layer (e.g. `up_proj`) | All MLP layers               |

---

## 🔬 Visualization & Validation Tools

| Tool                             | Role                                                  | Output                    |
| -------------------------------- | ----------------------------------------------------- | ------------------------- |
| `udo_activation_diff_plot.py`    | Difference map between patched vs unpatched responses | Attention/activation diff |
| `udo_top_token_activations.py`   | Lists and visualizes top activated neurons per token  | Bar chart, CSV            |
| `udo_visualize_path_sweep.py`    | Multi-token routing overlay                           | PCA / vector grid         |
| `udo_pathfinder_diff_heatmap.py` | Visualizes difference between trigger/neutral prompt  | RGB diff matrix           |

---

## 🌐 System Workflow – Mermaid Overview

```mermaid
graph TD
    A[Token Prompt] --> B{Pathfinder Scan}
    B --> C[Activation Trace]
    C --> D[Dim Trace CSV]
    D --> E[Patch Builder]
    E --> F[Live Patch CLI]
    F --> G[Patched Model]
    G --> H{Re-Run Prompt}
    H --> I[Validation Output]
