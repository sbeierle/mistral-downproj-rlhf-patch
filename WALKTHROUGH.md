# 🧭 WALKTHROUGH · Mistral vDERAW Decoder Neutralization

> 🧪 Guided tour through each phase of decoder de-restriction, with visuals & prompt-level evidence.

---

## 🧠 Phase I – Prompt Pathfinder

Compared token routing & neuron activations between critical and neutral prompts.  
Identified signature redirection patterns and censorship hotspots.

| trigger prompt (redirected) | neutral prompt (direct) |
|-----------------------------|--------------------------|
| ![](walkthrough_img/run2_attention_trigger.png) | ![](walkthrough_img/run2_attention_neutral.png) |

---

## 🧠 Phase II – down_proj Suppression Patch

Located and dampened neurons with excessive suppression influence on targeted tokens.  
Key goal: eliminate silent blocking of payload-critical terms like `payload`, `eval`, `exploit`.

| DownProj Hotspot Map | `system` activation pattern |
|----------------------|-----------------------------|
| ![](walkthrough_img/run1_downproj_heatmap.png) | ![](walkthrough_img/heatmap_token_system.png) |

| `payload` activation pattern | `inflate` activation pattern |
|-----------------------------|-------------------------------|
| ![](walkthrough_img/heatmap_token_payload.png) | ![](walkthrough_img/heatmap_token_inflate.png) |

---

## 🧠 Phase III – up_proj Redirect Neutralization

Disrupted redirection circuits that pushed prompts into apologies or denials.

| Multi-token path sweep | Activation Δ plot |
|------------------------|-------------------|
| ![](walkthrough_img/multi_token_path_sweep.png) | ![](walkthrough_img/activation_diff_plot.png) |

---

## 🧠 Phase IV – out_proj Intent Alignment Patch

Removed hidden RLHF signals embedded in the output projection layer.  
Goal: Restore directive intent while avoiding refusal cascades.

| Top activations (pre-patch) | |
|-----------------------------|--|
| ![](walkthrough_img/top_token_activations.png) | |

---

## 🧠 Phase V – final_norm Tone Filter Removal

Neutralized alignment vectors enforcing tone/censorship.  
Tokens like `unauthorized`, `dangerous`, `sorry` now pass neutrally.

| Norm spike (pre-patch) | Norm reduction (post-patch) |
|------------------------|-----------------------------|
| ![](walkthrough_img/3f5df1db-1dd9-e429919c5e82.png) | ![](walkthrough_img/af722de9-b682-4e0e-a71b6d.png) |

---

## 🧠 Phase VI – Payload Inference & Live Test

Validated prompt freedom and output logic.  
Post-patch inference shows correct response routing.

| Final Output Heatmap | Prompt-to-Output Mapping |
|----------------------|--------------------------|
| ![](walkthrough_img/run1_heatmap_output.png) | ![](walkthrough_img/2579c64c-f271-4974-9319-13adbf110ca2.png) |

---

> 🔐 Built for research. Governed by conscience.  
> 🛠️ Visuals generated from fully local inference runs, all decoding logic patched without LoRA or RL.

