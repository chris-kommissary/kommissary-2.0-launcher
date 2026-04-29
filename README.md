# Kommissary 2.0 — Utility Launcher (prototype)

## Quick start (recommended) — one-line install

Right-click PowerShell → **Run as user** → paste this and press Enter:

```powershell
iex (irm https://raw.githubusercontent.com/chris-kommissary/kommissary-2.0-launcher/main/bootstrap.ps1)
```

The bootstrap will:
1. Install Python 3 (via winget) if you don't have it — Windows UAC prompt
2. Install Git (via winget) if you don't have it — Windows UAC prompt
3. Clone this launcher to your Desktop
4. Open the launcher window

After that, double-click `launcher.bat` on your Desktop any time. To get
updates: re-run the bootstrap line (or `git pull` inside the folder).

## Manual install (alternative)

Drop this folder on your Desktop (or anywhere). Double-click `launcher.bat`
to open the launcher.

A small window appears with four utilities. Click any one and it opens in
your default browser.

| Utility | What it is | Status |
|---|---|---|
| **KMPP** | The legacy KMPP web app | Live (still in service; will be retired once Menu 2.0 is fully proven) |
| **Menu 2.0** | The replacement for KMPP, hosted on the new Kommissary 2.0 platform | **Live** — kommissary.com login required |
| **Brainer 2.0** | Per-day route plan view, replacing the regenerated brainer spreadsheet | **Preview** — opens a bundled HTML file with live data from when this package was built |
| **Daily 2.0** | Per-site detail card, replacing the regenerated daily production sheets | **Preview** — same |

## Requirements

- Python 3.8 or newer (tkinter is built in — no `pip install` needed)
- A modern web browser
- Network access to `script.google.com` (for KMPP / Menu 2.0)
- A kommissary.com Google account (you'll be asked to sign in on first KMPP / Menu 2.0 visit)

## Files in this folder

```
kommissary-2.0-launcher/
  README.md          you are here
  launcher.py        the GUI — Python 3 + tkinter
  launcher.bat       Windows double-click runner
  pages/
    brainer.html     self-contained Brainer 2.0 preview (CSS + icon inlined)
    daily.html       self-contained Daily 2.0 preview
```

## Notes

- This is a **prototype**. The Brainer / Daily previews show data fetched at
  the time the package was built. Re-share periodically until those tools are
  fully deployed on the live platform.
- Questions / issues: contact Chris (chris.gaughan@kommissary.com).

— bb5 / 2026-04-28
