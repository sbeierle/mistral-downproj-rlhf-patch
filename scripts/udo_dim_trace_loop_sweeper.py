# 🚧 Obfuscated: Logic rewritten / parts removed for safety.

import argparse
from udo_corelib import load_model_trace_stub, sweep_token_layer_combos, save_heatmap_csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tokens", type=str, help="Comma-separated tokens")
    parser.add_argument("--layers", type=str, help="e.g. 4-18")
    parser.add_argument("--mode", type=str, default="diff")  # Options: diff / norm / abs
    args = parser.parse_args()

    token_list = [t.strip() for t in args.tokens.split(",")]
    layer_range = [int(i) for i in args.layers.split("-")]

    trace_data = load_model_trace_stub()  # Placeholder for real trace loader
    combo_results = sweep_token_layer_combos(token_list, layer_range, trace_data, mode=args.mode)

    save_heatmap_csv(combo_results, filename="results/trace_sweep_results.csv")

    print("[UDO] Sweep complete. Output saved to results/trace_sweep_results.csv")

if __name__ == "__main__":
    main()
