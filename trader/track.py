#!/usr/bin/env python3
"""Compare the paper portfolio in trader/baseline.json with SPY. Read-only."""
import json, subprocess, sys, re, os
here = os.path.dirname(os.path.abspath(__file__))
b = json.load(open(os.path.join(here, "baseline.json")))
alerts = os.path.join(here, "..", ".claude", "skills", "trader-alerts", "alerts.py")
syms = list(b["positions"]) + list(b["benchmark"])
out = subprocess.run([sys.executable, alerts, "quote"] + syms, capture_output=True, text=True).stdout
px = {m.group(1): float(m.group(2)) for m in re.finditer(r"^(\S+)\s+\$([\d.]+)", out, re.M)}
tot0 = tot1 = 0.0
for s, p in b["positions"].items():
    v1 = p["usd"] * px[s] / p["price"]
    tot0 += p["usd"]; tot1 += v1
    print("%-6s %6.2f -> %6.2f  (%+.1f%%)" % (s, p["usd"], v1, (v1 / p["usd"] - 1) * 100))
spy = (px["SPY"] / b["benchmark"]["SPY"] - 1) * 100
print("Portfolio %.2f -> %.2f  (%+.1f%%)   SPY %+.1f%%" % (tot0, tot1, (tot1 / tot0 - 1) * 100, spy))
