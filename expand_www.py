#!/usr/bin/env python3
import gzip, base64, json, pathlib
root = pathlib.Path(__file__).resolve().parent
raw = "".join((root / f"www_data.{i}").read_text() for i in range(4))
data = json.loads(raw)
out = root / "www"
out.mkdir(parents=True, exist_ok=True)
for name, b64 in data.items():
    (out / name).write_bytes(gzip.decompress(base64.b64decode(b64)))
    print("wrote", name, len((out / name).read_bytes()))
print("Full UI ready.")
