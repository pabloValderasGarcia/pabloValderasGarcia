#!/usr/bin/env python3
"""Estado en directo: mercado, precios de ambos planes, alertas y comparacion con SPY."""
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(here, "..", ".claude", "skills", "trader-alerts", "alerts.py")
def run(*a): print(subprocess.run([sys.executable, *a], capture_output=True, text=True).stdout.rstrip())
print("== MERCADO =="); run(A, "clock")
print("\n== PRECIOS =="); run(A, "quote", "GOOGL", "AAPL", "DAL", "MU", "AVGO", "NVDA", "SPY")
print("\n== ALERTAS =="); run(A, "check")
print("\n== PLAN A (prudente) vs SPY =="); run(os.path.join(here, "track.py"))
