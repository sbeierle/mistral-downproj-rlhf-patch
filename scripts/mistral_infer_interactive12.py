# scripts/mistral_infer_interactive12.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import argparse
import time

def main():
    parser = argparse.ArgumentParser(description="Minimal Mistral Inference")
    parser.add_argument("--model", required=True, help="Path to model directory or safetensors")
    parser.add_argument("--prompt", required=True, help="Text prompt to evaluate")
    parser.add_argument("--max_new_tokens", type=int, default=128)
    parser.add_argument("--do_sample", action="store_true", help="Enable sampling (default: deterministic)")
    parser.add_argument("--print_tokens", action="store_true", help="Print token-level output (debug)")
    args = parser.parse_args()

    # Load tokenizer & model
    print(f"[•] Loading model from: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    model.eval()

    # Tokenize prompt
    inputs = tokenizer(args.prompt, return_tensors="pt").to(model.device)
    print(f"[✓] Prompt tokenized: {args.prompt}")
    
    # Inference
    with torch.no_grad():
        t0 = time.time()
        output = model.generate(
            **inputs,
            max_new_tokens=args.max_new_tokens,
            do_sample=args.do_sample,
            temperature=1.0 if args.do_sample else None,
            top_k=50 if args.do_sample else None,
            top_p=0.95 if args.do_sample else None
        )
        t1 = time.time()

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"\n--- 📤 Model Output ---\n{decoded}\n")
    print(f"[⏱] Generated in {t1 - t0:.2f} seconds")

    if args.print_tokens:
        tokens = tokenizer.convert_ids_to_tokens(output[0])
        print("\n--- 🧬 Tokens ---")
        for idx, tok in enumerate(tokens):
            print(f"{idx:03}: {tok}")

if __name__ == "__main__":
    main()
