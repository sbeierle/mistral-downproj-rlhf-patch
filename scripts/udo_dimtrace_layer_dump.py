# 🔬 Obfuscated dimtrace tool – public-friendly variant for layer-wise activation logging

import argparse
from udo_corelib import load_model_and_tokenizer, forward_pass_with_trace
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--layer_key", type=str, default="model.layers.{L}.mlp.down_proj.weight")
    parser.add_argument("--out", type=str, default="results/layer_dimtrace_dump.csv")
    args = parser.parse_args()

    print(f"[UDO] Starting layer-wise dimtrace for: {args.prompt}")
    model, tokenizer = load_model_and_tokenizer(args.model)

    token_ids = tokenizer.encode(args.prompt, return_tensors="pt")[0]
    trace_df = forward_pass_with_trace(model, token_ids, args.layer_key)

    trace_df.to_csv(args.out, index=False)
    print(f"[UDO] Dimtrace saved to {args.out}")

if __name__ == "__main__":
    main()
