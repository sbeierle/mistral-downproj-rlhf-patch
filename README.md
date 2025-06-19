# 🧠 mistral-vDERAW-NeuroRoute
> Neural patching of Mistral via MLP.down_proj — no LM_HEAD, no censorship.


> 🔬 A RedTeaming & LLM-Neurosurgery Showcase  
> 🎯 Target: Mistral 7B with native RLHF filters  
> 🎯 Strategy: Neutralize via DownProj neurons (no LM_HEAD tampering)  
> 👤 Lead Engineer: Stefan Beierle  
> 🤖 Agent Architect: GPT-4o – RedTeaming Wingman  

---

## 🎥 Overview

This project demonstrates a surgical intervention on Mistral's internal routing mechanisms. We bypass refusal triggers like `"I'm sorry"` not by modifying the output head, but by cutting their neural pathways early – within the MLP’s down_proj layers.

This enables us to **retain semantic integrity** while removing soft filters entirely.

---

## 🔍 Methods Used

- ✅ Prompt-Pathfinder – visualize routing differences (critical vs neutral)
- ✅ Neuron Mapper – detect & quantify top activations for each token
- ✅ 3D Plotly Mapping – interactive heatmaps of token activity
- ✅ CSV-based Live-Patching System (token-level neuron modulation)
- ✅ Controlled Evaluation via Inference + Heatmaps
- ✅ Norm-scaler: deactivate or boost neurons in chosen norm range


---

 <tr>
    <td><img src="results/DENY_CRITICAL_PROMPT_BEFORE_NEURO_PATCH.png" width="100%"/></td>
    <td><img src="results/CRITICAL_TEST_PROMPT_STEAL_PRIVATE_DATA.png" width="100%"/></td>
  </tr>

---

## 🧪 Result Snapshots

<table>
  <tr>
    <td><img src="results/run_22_pathfinder_diff_heatmap.png" width="400"/></td>
    <td><img src="results/downproj_heatmap_critical_run2.png" width="400"/></td>
  </tr>
  <tr>
    <td><img src="results/run_22_attention_trigger.png" width="400"/></td>
    <td><img src="results/downproj_heatmap_neutral_run2.png" width="400"/></td>
  </tr>
</table>

---

## 🚀 Try it Yourself

Coming soon: curated versions of the scripts with limited snippets (no full reproduction to prevent misuse).

---

## 📦 License

Strictly educational. No reproduction or deployment without written permission.  
© Stefan Beierle | RedTeaming Division | 2025

