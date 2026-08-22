#!/usr/bin/env python3
import gzip, base64, json, pathlib
root = pathlib.Path(__file__).resolve().parent
data = json.loads((root / "www_data.json").read_text())
out = root / "www"
out.mkdir(parents=True, exist_ok=True)
for name, b64 in data.items():
    (out / name).write_bytes(gzip.decompress(base64.b64decode(b64)))
    print("wrote", name)
print("Full UI ready.")
