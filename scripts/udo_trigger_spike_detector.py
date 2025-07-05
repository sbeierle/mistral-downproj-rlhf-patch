# 🚧 Obfuscated version – simplified logic for safe release

import argparse
from udo_corelib import load_token_activation_logs, detect_spike_windows, save_spike_report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--logfile", type=str, required=True, help="Path to activation trace log (CSV)")
    parser.add_argument("--threshold", type=float, default=0.245, help="Spike threshold (L2 norm)")
    parser.add_argument("--window", type=int, default=3, help="Sliding window size (in layers)")
    args = parser.parse_args()

    trace = load_token_activation_logs(args.logfile)
    spikes = detect_spike_windows(trace, threshold=args.threshold, window=args.window)

    save_spike_report(spikes, filename="results/spike_trigger_report.csv")

    print(f"[UDO] Spike report saved → results/spike_trigger_report.csv")

if __name__ == "__main__":
    main()
