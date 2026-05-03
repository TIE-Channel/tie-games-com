# TIE-Games Website

Static website for tie-games.com - homepage, Evolrace game, privacy policy.

## Deployment via GitHub Pages

### Step 1: Create repo

Create a new GitHub repo named `tie-games-com` (or similar) under the `tie-channel` account.

Drop all files from this folder into the repo root via GitHub web UI:
- index.html (homepage)
- evolrace.html (game)
- privacy.html (privacy policy)
- evolrace-icon.png (game icon)
- og-image.png (Open Graph preview)
- favicon.ico, favicon-32.png, favicon-64.png, apple-touch-icon.png
- CNAME (custom domain config)

### Step 2: Enable GitHub Pages

1. Repo Settings -> Pages
2. Source: Deploy from a branch
3. Branch: main, folder: / (root)
4. Save

### Step 3: Configure DNS for tie-games.com

In your domain registrar (where tie-games.com is registered), add these DNS records:

A records (point apex domain to GitHub Pages IPs):
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

CNAME record (for www subdomain):
```
www -> tie-channel.github.io
```

### Step 4: Verify in GitHub Pages settings

After DNS propagates (5min - 24h):
1. Repo Settings -> Pages
2. Custom domain: tie-games.com
3. Wait for "DNS check successful"
4. Enable "Enforce HTTPS"

Done. Site available at https://tie-games.com

## Files description

- `index.html` - Homepage with games list, about, contact
- `evolrace.html` - Full Evolrace game (also playable directly)
- `privacy.html` - Privacy policy required by Play Store
- `CNAME` - Tells GitHub Pages to use tie-games.com domain
- `og-image.png` - Image shown when sharing link on social media
- `evolrace-icon.png` - Game icon used on homepage card

## Updating

To update content - edit files via GitHub web UI, commit. Changes go live in 1-2 minutes.

## Privacy policy URL for Play Store

After deployment use this URL in Play Console:
```
https://tie-games.com/privacy.html
```

This replaces the previous github.io URL.
