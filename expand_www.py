#!/usr/bin/env python3
import gzip, base64, json, pathlib
root = pathlib.Path(__file__).resolve().parent
parts = []
for i in range(4):
    for j in range(3):
        parts.append((root / f"www_data.{i}.{j}").read_text())
raw = "".join(parts)
data = json.loads(raw)
www = root / "www"
www.mkdir(parents=True, exist_ok=True)
for name, b64 in data.items():
    (www / name).write_bytes(gzip.decompress(base64.b64decode(b64)))
    print("wrote", name, len((www / name).read_bytes()))
print("Full Vibe-Collector UI ready.")
