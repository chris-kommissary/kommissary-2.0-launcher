"""Kommissary 2.0 — Utility Launcher (prototype).

Drop this folder anywhere (Desktop is fine). Double-click launcher.bat
(Windows) or run `python launcher.py` (Mac/Linux/anywhere with Python 3).

Click a utility button -> opens that surface in your default browser.
All four utilities now live behind kommissary.com Google sign-in;
Brainer 2.0 and Daily 2.0 are additionally restricted to a small
allowlist of approved users.

No installation needed. Pure-stdlib Python (tkinter is built in).
"""
import tkinter as tk
from tkinter import messagebox
import webbrowser
from pathlib import Path

# -------- targets ------------------------------------------------------
KMPP_URL    = "https://script.google.com/a/macros/kommissary.com/s/AKfycbwblN-wbqbpxBTRWe7-9586m6T6RU4-CifKdYZVkHvTgvP3wrrF7SOlin0Ls8dDhNi6/exec"
K2_BASE     = "https://script.google.com/a/macros/kommissary.com/s/AKfycbx-Ub-gsw62KRwHkRNHDKNoSJY1mSLYOXCEVwuLVmUjp2AXDeGK9SDxBSNJGt46wXnq/exec"
MENU20_URL   = K2_BASE + "?app=menu"
BRAINER_URL  = K2_BASE + "?app=brainer"   # allowlist-gated
DAILY_URL    = K2_BASE + "?app=daily"     # allowlist-gated

BASE = Path(__file__).parent.resolve()

# -------- brand palette -----------------------------------------------
COLOR_LUNAR    = "#354535"   # Brainer 2.0
COLOR_STEEL    = "#277CA1"   # Daily 2.0
COLOR_GAMBOGE  = "#E19308"   # Menu 2.0
COLOR_GREY     = "#B0B0B0"   # KMPP (legacy / neutral)
COLOR_BG       = "#F7F7F7"
COLOR_FG_LIGHT = "#FFFFFF"
COLOR_FG_DARK  = "#1A1A1A"

def open_target(target):
    if isinstance(target, Path):
        if not target.exists():
            messagebox.showerror(
                "Page missing",
                f"Could not find:\n{target}\n\n"
                "The launcher needs the bundled `pages/` folder next to launcher.py."
            )
            return
        webbrowser.open(target.as_uri())
    else:
        webbrowser.open(target)

def make_card(parent, name, build, color, target):
    frame = tk.Frame(parent, bg=color, padx=18, pady=12, cursor="hand2")
    frame.pack(fill="x", pady=4)
    name_lbl  = tk.Label(frame, text=name,  font=("Segoe UI", 13, "bold"),
                         bg=color, fg=COLOR_FG_LIGHT, anchor="w")
    build_lbl = tk.Label(frame, text=build, font=("Segoe UI", 9, "bold"),
                         bg=color, fg=COLOR_FG_LIGHT)
    name_lbl.pack(side="left")
    build_lbl.pack(side="right")
    # Click anywhere on the card -> open
    for w in (frame, name_lbl, build_lbl):
        w.bind("<Button-1>", lambda e, t=target: open_target(t))

# -------- build window -------------------------------------------------
root = tk.Tk()
root.title("Kommissary 2.0 — Utility Launcher (prototype)")
root.geometry("520x420")
root.configure(bg=COLOR_BG)

# Window icon — bundled kommissary-icon.png alongside this script
_icon_path = BASE / "kommissary-icon.png"
if _icon_path.exists():
    try:
        _icon_img = tk.PhotoImage(file=str(_icon_path))
        root.iconphoto(True, _icon_img)
        root._icon_ref = _icon_img  # keep ref so it isn\u0027t GC\u0027d
    except Exception:
        pass

# Banner header
header = tk.Frame(root, bg=COLOR_LUNAR, height=80)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(header, text="Kommissary 2.0",
         font=("Segoe UI", 22, "bold"),
         bg=COLOR_LUNAR, fg=COLOR_FG_LIGHT, anchor="w"
        ).pack(side="left", padx=20, pady=(14, 0))

tk.Label(header, text="UTILITY LAUNCHER\nPROTOTYPE",
         font=("Segoe UI", 8, "bold"),
         bg=COLOR_LUNAR, fg=COLOR_FG_LIGHT, justify="left"
        ).pack(side="left", padx=(0, 20), pady=(20, 0))

# Cards
cards = tk.Frame(root, bg=COLOR_BG, padx=20, pady=20)
cards.pack(fill="both", expand=True)

make_card(cards, "KMPP",        "LEGACY",                 COLOR_GREY,    KMPP_URL)
make_card(cards, "MENU 2.0",    "BUILD #6 LIVE",          COLOR_GAMBOGE, MENU20_URL)
make_card(cards, "BRAINER 2.0", "BUILD #1 PREVIEW (auth)", COLOR_LUNAR,  BRAINER_URL)
make_card(cards, "DAILY 2.0",   "BUILD #1 PREVIEW (auth)", COLOR_STEEL,  DAILY_URL)

# Footer
tk.Label(root, text="Prototype · 2026-04-28 · click a utility to open",
         font=("Segoe UI", 8), bg=COLOR_BG, fg=COLOR_GREY
        ).pack(side="bottom", pady=8)

root.mainloop()
