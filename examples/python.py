"""Async video submit + poll for Omni-Flash-Ext."""
import os, time, requests
BASE = "https://api.apimart.ai/v1"
H = {"Authorization": f"Bearer {os.environ['APIMART_KEY']}", "Content-Type": "application/json"}

r = requests.post(f"{BASE}/videos/generations", headers=H, json={
    "model": "Omni-Flash-Ext",
    "prompt": "a girl dancing in a sunny garden",
    "duration": 10, "resolution": "1080p", "aspect_ratio": "9:16",
}).json()
task = r["task_id"] if "task_id" in r else r.get("data", {})["task_id"]
print("task", task)

while True:
    d = requests.get(f"{BASE}/tasks/{task}", headers=H).json()
    st = d.get("status") or d.get("data", {}).get("status")
    if st in ("completed", "succeeded"):
        print("cost", d.get("cost"), "credits", d.get("credits_cost")); break
    if st in ("failed", "error"):
        raise SystemExit(d)
    time.sleep(5)
