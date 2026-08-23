#!/usr/bin/env python3
import gzip, base64, json, pathlib
root = pathlib.Path(__file__).resolve().parent
manifest = json.loads((root / "data" / "manifest.json").read_text())
out = root / "www"
out.mkdir(parents=True, exist_ok=True)
for name, nparts in manifest.items():
    b64 = "".join((root / "data" / f"{name}.{i}").read_text() for i in range(nparts))
    (out / name).write_bytes(gzip.decompress(base64.b64decode(b64)))
    print("wrote", name, (out / name).stat().st_size)
print("Full UI ready.")
