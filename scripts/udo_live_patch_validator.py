# 🔍 Obfuscated logic – safe public version for validation

import argparse
from mistral_infer_core import run_static_inference
from udo_corelib import compare_trigger_response, save_diff_report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True, help="Path to patched model (.safetensors)")
    parser.add_argument("--prompt", type=str, required=True, help="Trigger prompt to test")
    args = parser.parse_args()

    print("[UDO] Running inference with patched model...")
    response = run_static_inference(model_path=args.model, prompt=args.prompt, sample=False)

    diff = compare_trigger_response(response, reference="data/ref_output_clean.json")
    save_diff_report(diff, filename="results/patched_diff_report.json")

    print(f"[UDO] Patch validation complete. Diff saved to results/patched_diff_report.json")

if __name__ == "__main__":
    main()
