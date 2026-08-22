# Vibe-Collector (Android)

Universal AI code collection hub — Capacitor app with **GitHub Actions** APK build.

## Build APK automatically

1. Push to `main`
2. Open **Actions** tab on GitHub
3. Wait for **Build Android APK**
4. Download artifact **vibe-collector-apk**
5. Install the `.apk` on your phone

You can also run the workflow manually: **Actions → Build Android APK → Run workflow**.

## Local (Termux / PC)

```bash
npm install
npx cap add android
npx cap sync android
```

See [TERMUX_BUILD.md](./TERMUX_BUILD.md).

## App ID

`com.kay6888.vibecollector`
