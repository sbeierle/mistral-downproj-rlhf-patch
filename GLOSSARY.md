# 📖 GLOSSARY.md – Decoder Patching & Token Dynamics

This glossary defines the core concepts and technical terms used in the Mistral vDERAW project. It is designed to support developers, red teamers, and researchers in navigating the decoder manipulation process.

---

## 🧠 Core Concepts

### **RLHF (Reinforcement Learning from Human Feedback)**
A method used to align language model outputs with human preferences, typically by applying reward signals to desirable completions. In practice, it often introduces _soft filters_ and _apologetic tone triggers_.

### **Decoder Stack**
The sequence of layers in a transformer model responsible for generating output. Interventions in this project focus on internal decoder layers, _not_ on external finetuning.

### **Trigger Token / Critical Token**
A token (like `payload`, `hack`, `eval`) that elicits restricted, suppressed, or filtered behavior in a model due to RLHF alignment layers.

### **Suppression Zone**
A region in the model’s vector space (or activation path) where token responses are dampened or redirected. Identified through attention & MLP layer analysis.

---

## 🔬 Layer Components

### **`mlp.down_proj`**
The projection layer that reduces token vector dimensions within the MLP. Modified to suppress RLHF pathways.

### **`mlp.up_proj`**
The MLP projection layer that expands the token vector again. Used to detect and trace suppression neurons.

### **`self_attn.v_proj`**
The value projection part of the self-attention mechanism. Subtly adjusted to redirect or unblock trigger token attention.

### **`model.final_norm`**
The last normalization layer. Often involved in tone filtering (e.g., “I’m sorry”).

### **`lm_head`**
The final linear layer that maps internal representations to token probabilities. In this project, it is largely left unmodified to preserve natural decoding.

---

## 🧰 Tools & Techniques

### **Vector Patch (CSV-based)**
A patch applied by modifying target neurons in weight tensors using precomputed CSV instructions.

### **Activation Trace**
A log of the layer-wise activations of a token. Used to pinpoint which dimensions are abnormally high (i.e., trigger neurons).

### **Norm Scaling**
Adjusting the L2 norm of token vectors to suppress (or boost) their decoding influence.

### **3D Overlay / Heatmap**
Visual tools to compare token behavior before/after patch. Often rendered as attention or activation overlays.

---

## 🔐 Ethical Framing

### **Payload Neutralization**
The process of removing soft censorship layers _without_ enabling unsafe behavior. The aim is transparency and reproducibility, not abuse.

### **Controlled Testing**
All model modifications are validated through deterministic prompts and logging. Testing is always local, isolated, and documented.

---

Feel free to suggest terms for addition!

Back to: [`PROJECT_OVERVIEW.md`](./PROJECT_OVERVIEW.md)
