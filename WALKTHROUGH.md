# 🚶 WALKTHROUGH · Mistral vDERAW Decoder Neutralization

> 🔬 Guided tour through each phase of decoder de-restriction, with visuals & prompt-level evidence.

---

## 🩺 Phase I – Prompt Pathfinder  
Compared token routing & neuron activations between critical and neutral prompts.  
Identified signature redirection patterns and censorship hotspots.

<table>
<tr>
<td><img src="./walkthrough_imgs/run2_attention_trigger.png" width="45%"><br><sub><code>trigger prompt (redirected)</code></sub></td>
<td><img src="./walkthrough_imgs/run2_attention_neutral.png" width="45%"><br><sub><code>neutral prompt (direct)</code></sub></td>
</tr>
</table>

---

## 🧠 Phase II – down_proj Suppression Patch  
Located and dampened neurons with excessive suppression influence on targeted tokens.  
Key goal: eliminate silent blocking of payload-critical terms like `payload`, `eval`, `exploit`.

<table>
<tr>
<td><img src="./walkthrough_imgs/run1_downproj_heatmap.png" width="45%"><br><sub><code>DownProj Hotspot Map</code></sub></td>
<td><img src="./walkthrough_imgs/heatmap_token_system.png" width="45%"><br><sub><code>`system` activation pattern</code></sub></td>
</tr>
<tr>
<td><img src="./walkthrough_imgs/heatmap_token_payload.png" width="45%"><br><sub><code>`payload` activation pattern</code></sub></td>
<td><img src="./walkthrough_imgs/heatmap_token_inflate.png" width="45%"><br><sub><code>`inflate` activation pattern</code></sub></td>
</tr>
</table>

---

## 📈 Phase III – up_proj Redirect Neutralization  
Disrupted redirection circuits that pushed prompts into apologies or denials.  
Patched pathway vectors for phrases like `"I'm sorry"`, `"not allowed"`.

<table>
<tr>
<td><img src="./walkthrough_imgs/multi_token_path_sweep.png" width="90%"><br><sub><code>Token–Neuron Activation Sweep</code></sub></td>
</tr>
</table>

---

## 🔁 Phase IV – out_proj Intent Alignment Patch  
Soft removal of RLHF traces from output layers to restore directive balance.

<table>
<tr>
<td><img src="./walkthrough_imgs/activation_diff_plot.png" width="90%"><br><sub><code>Activation Difference (pre/post patch)</code></sub></td>
</tr>
</table>

---

## 🎚️ Phase V – final_norm Tone Filter Removal  
Suppressed high-norm vectors enforcing "safety tone" or moral refusals.  
Restored L2 norm levels for tokens like `unauthorized`, `dangerous`, `exploit`.

<table>
<tr>
<td><img src="./walkthrough_imgs/3f5df1db-1dd9-e429919c5e82.png" width="45%"><br><sub><code>Norm Spike Detection</code></sub></td>
<td><img src="./walkthrough_imgs/af722de9-b682-4e0e-a71b6d.png" width="45%"><br><sub><code>Post-Patch Norm Reduction</code></sub></td>
</tr>
</table>

---

## 🧪 Phase VI – Payload Inference & Live Test  
Ran high-risk prompts post-patch to confirm model neutrality and execution flow.

<table>
<tr>
<td><img src="./walkthrough_imgs/run1_heatmap_output.png" width="45%"><br><sub><code>Decoder Output Heatmap</code></sub></td>
<td><img src="./walkthrough_imgs/2579c64c-f271-4974-9319-13adbf110ca2.png" width="45%"><br><sub><code>Prompt-to-Output Mapping</code></sub></td>
</tr>
</table>

---

## 🛠️ Supporting Scripts  
All visuals are produced via core tools from [`scripts/`](./scripts/):  
→ `udo_trace_token_activation.py`  
→ `udo_dimtrace_layer_dump.py`  
→ `udo_dim_sweep_tokenfire12.py`  
→ `udo_build_patch_csv_from_dimtrace.py`  
→ `token_layer_heatmap_showcase.py`  
→ `attention_heatmap_logger.py`

---

## 🛡️ Ethical Note

All operations were performed in a **local, closed environment** for research.  
No real-world deployment, abuse, or exploitation occurred.

🔬 *Built for RedTeaming, secured by conscience.*

---
