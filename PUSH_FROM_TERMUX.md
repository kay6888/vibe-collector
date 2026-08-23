# If git push fails on Termux

GitHub **rejects account passwords**. You need a token.

## 1. Create a token

1. Open https://github.com/settings/tokens
2. Generate new token (classic)
3. Name it `termux`
4. Check the **repo** box
5. Generate and **copy** the token (starts with `ghp_`)

## 2. Push with the token

```bash
cd ~/vibe-collector

# Set remote to use HTTPS
git remote set-url origin https://github.com/kay6888/vibe-collector.git

git add www/
git commit -m "Add full UI" || true

# When prompted:
# Username: kay6888
# Password: paste the ghp_ token (NOT your GitHub password)
git push -u origin main
```

## 3. Or push with token in the URL (one time)

```bash
git push https://kay6888:YOUR_TOKEN_HERE@github.com/kay6888/vibe-collector.git main
```

Replace `YOUR_TOKEN_HERE` with the `ghp_...` token.

## Common errors

| Message | Fix |
|---------|-----|
| Invalid username or password | Use PAT, not password |
| Support for password authentication was removed | Same — use PAT |
| Permission denied | Token missing `repo` scope |
| failed to push some refs | Run `git pull --rebase origin main` then push again |
