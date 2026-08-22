# Build Vibe-Collector for Android

## GitHub Actions (recommended)

1. Push this repo to GitHub
2. Open the **Actions** tab
3. Select **Build Android APK**
4. Wait for the green check
5. Download **vibe-collector-apk** artifact
6. Unzip and install the `.apk` on your phone

Manual run: Actions → Build Android APK → Run workflow

## Termux local setup

```bash
pkg update -y
pkg install git nodejs-lts python -y
git clone https://github.com/kay6888/vibe-collector.git
cd vibe-collector
npm install
npx cap add android
npx cap sync android
```

Full APK build on-device needs Android SDK (heavy). Prefer GitHub Actions.
