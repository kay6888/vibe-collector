#!/data/data/com.termux/files/usr/bin/bash
# Vibe-Collector — one-shot Termux setup
# Run:  bash INSTALL_TERMUX.sh
set -e

echo "=== Vibe-Collector Termux setup ==="

pkg update -y
pkg install -y git python wget unzip

cd ~
if [ -d vibe-collector/.git ]; then
  echo "Repo already exists — pulling latest..."
  cd vibe-collector
  git pull origin main || true
else
  echo "Cloning repo..."
  git clone https://github.com/kay6888/vibe-collector.git
  cd vibe-collector
fi

echo "Expanding full UI..."
python3 expand_www.py

if grep -q screen-welcome www/index.html && grep -q PROJECTS www/app.js; then
  echo ""
  echo "Full UI is ready in ~/vibe-collector/www/"
  ls -lh www/
else
  echo "UI expand failed — data parts may still be incomplete on GitHub."
  exit 1
fi

echo ""
echo "=== Done ==="
echo ""
echo "Get the Android APK:"
echo "  1. Open https://github.com/kay6888/vibe-collector/actions"
echo "  2. Open the latest green Build Android APK run"
echo "  3. Download artifact: vibe-collector-apk"
echo "  4. Unzip and install the .apk on your phone"
echo ""
echo "Or run the workflow:"
echo "  https://github.com/kay6888/vibe-collector/actions/workflows/android.yml"
