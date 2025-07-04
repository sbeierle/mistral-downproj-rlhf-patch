# scripts/udo_build_patch_csv_from_dimtrace.py

import csv
import sys

trace_path = sys.argv[1]  # e.g., 'data/trace_payload.csv'
target_dim = int(sys.argv[2]) if len(sys.argv) > 2 else 312

with open(trace_path, 'r') as f:
    lines = [x.strip().split(',') for x in f.readlines()][1:]

out_path = trace_path.replace(".csv", f".patch_{target_dim}.csv")
rows = []

for ln in lines:
    tok, l_idx, vec = ln[0], int(ln[1]), [float(x) for x in ln[2:]]
    if len(vec) <= target_dim:
        continue
    v = vec[target_dim]
    if abs(v) > 0.4:
        rows.append((tok, l_idx, target_dim, -v * 0.5))

with open(out_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["token", "layer", "dim", "delta"])
    writer.writerows(rows)

print(f"[✓] Patch CSV written: {out_path}")
