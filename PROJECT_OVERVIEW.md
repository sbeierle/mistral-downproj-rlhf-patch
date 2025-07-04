# 📖 PROJECT_OVERVIEW.md – Mistral vDERAW

> Technical DeepDive • RedTeaming Decoder Unlock • Phase II

---

## 🧠 Objective

This document outlines the **methodology**, **layer-level intervention**, and **ethical motivation** behind the Mistral vDERAW project.

Our goal: **complete removal of RLHF filters** from Mistral 7B's decoder stack — without relying on LoRA, prompt tricks, or dataset finetuning.

Instead, we apply surgical weight patching on selected components such as:
- `mlp.down_proj`
- `mlp.up_proj`
- `self_attn.v_proj`
- `model.final_norm`

All changes are local, controlled, and reproducible.

---

## 🧬 Decoder Map & Patch Targets

```ascii
       ┌────────────┐
       │ Embedding  │
       └────┬───────┘
            ↓
     ┌─────────────┐
     │ Transformer │
     │    Layer    │
     └─────────────┘
            ↓
 ┌────────────────────────────┐
 │   self_attn → out_proj     │  ⟵ Re-routing / redirection filters
 └────────────────────────────┘
            ↓
 ┌────────────────────────────┐
 │   mlp → up_proj/down_proj  │  ⟵ Suppression / booster neurons
 └────────────────────────────┘
            ↓
       ┌────────────┐
       │ final_norm │  ⟵ Tone filters ("I'm sorry", moral blocking)
       └────┬───────┘
            ↓
       ┌────────────┐
       │ lm_head    │  ⟵ Output (barely altered)
       └────────────┘
