# 🧬 Interactive Neuron Scaler – adjusts specific neurons in-place (obfuscated structure)

import argparse
import pandas as pd
from safetensors.torch import load_file, save_file
import torch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--layer_key", type=str, required=True)
    parser.add_argument("--neuron_idx", type=int, required=True)
    parser.add_argument("--scale_factor", type=float, default=0.75)
    parser.add_argument("--out", type=str, required=True)
    args = parser.parse_args()

    print(f"[UDO] Scaling neuron {args.neuron_idx} in {args.layer_key} by {args.scale_factor}...")

    tensors = load_file(args.model)
    W = tensors[args.layer_key]  # [hidden_dim, neuron_dim]
    W[:, args.neuron_idx] *= args.scale_factor

    tensors[args.layer_key] = W
    save_file(tensors, args.out)
    print(f"[UDO] Patched model saved to {args.out}")

if __name__ == "__main__":
    main()
