# DESIGN.md — Chaos Bot Design System & Product Blueprint

## 1. Brand Identity & Vision
- **Name:** Chaos Bot
- **Domain:** chaosbot.com
- **Core Positioning:** An unapologetically sharp, lightning-fast AI companion that bridges unfiltered creative intelligence (**Chaos**) with laser-focused executive reasoning (**Order**).
- **Competitor Target:** Grok by xAI / x.com.
- **Visual Soul:** Inspired by **Cal.com** — brutalist clarity, refined monochrome typography, generous whitespace, razor-sharp 1px borders, and **zero AI slop** (no tacky green gradient boxes, no neon purple halos, no cheap glowing cards).

---

## 2. Competitor Teardown: Grok (xAI) vs. Chaos Bot

| Dimension | Grok on x.com | Chaos Bot (Our Advantage) |
| :--- | :--- | :--- |
| **Aesthetics** | Cluttered with X social feed, ads, and noise | **Cal.com Minimalist Canvas**: Distraction-free, pure focus on conversation |
| **Personality** | "Fun Mode" vs "Normal Mode" | **Dual Engine Modes**: `⚡ Chaos Mode` (witty, bold, unfiltered) & `🛡️ Order Mode` (concise, structured, surgical) |
| **Reasoning** | "Think" toggle | **Visible Chain-of-Thought**: Collapsible deep reasoning drawer with token step timeline |
| **Privacy / Engine** | 100% Cloud / proprietary lock-in | **Hybrid Engine**: Toggle between **Local Ollama** (100% private, on-device offline) and **Cloud API** (instant zero-install) |
| **Terminal / CLI** | None (Web & mobile app only) | **Dual Interface**: Full web app + Native terminal CLI (`python3 app.py`) with zero conflicts |

---

## 3. Cal.com Design System Specifications

### Typography
- **Display Font:** `Cal Sans` / `Geist` / `Inter` (Font weight: 600 / 700 for headlines).
- **Body Font:** `Geist Sans` / `Inter` (Font weight: 400 / 500, leading: 1.6).
- **Monospace Font:** `Geist Mono` / `JetBrains Mono` for code snippets, shortcuts, and terminal output.

### Color Palette (Monochrome & Structural Grays)
```
Canvas Light:        #FFFFFF
Canvas Light Muted:  #F9FAFB
Surface Elevated:    #FFFFFF
Border Subtle:       #E5E7EB
Border High-Contrast:#D1D5DB
Text Primary:        #111827 (Pure deep ink)
Text Muted:          #6B7280

Canvas Dark:         #0A0A0A
Canvas Dark Muted:   #121212
Surface Dark Card:   #171717
Border Dark Subtle:  #262626
Border Dark High:    #404040
Text Dark Primary:   #EDEDED
Text Dark Muted:     #A1A1AA

Accent Functional:
- Chaos Electric:    #000000 (Dark: #FFFFFF) — Stark, high-contrast CTA
- System Status:     #10B981 (Subtle indicator dot only, no neon glow)
- System Error:      #EF4444 (Clean flat badge)
```

### Layout & Spacing
- **Container Widths:** 
  - Chat stream max-width: `768px` (Optimal reading line-length).
  - Landing / Hero max-width: `1200px`.
- **Corner Radii:**
  - Cards & Containers: `rounded-xl` (`12px` to match Cal.com).
  - Buttons & Inputs: `rounded-lg` (`8px`).
  - Badges & Pills: `rounded-full`.
- **Shadows:** Minimal or zero blur. Crisp 1px borders instead of heavy diffuse dropshadows:
  - `box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); border: 1px solid var(--border-subtle)`

---

## 4. Key Features & Interface Blueprint

### 1. The Dynamic Chat Canvas
- **Clean Message Bubbles:** No garish bubble shapes. Assistant responses render directly onto the canvas with Markdown, syntax-highlighted code blocks, and copy buttons.
- **Personality Switcher Bar:**
  - `[ ⚡ Chaos Mode ]` — Sarcastic, creative, lateral thinking, provocative brainstormer.
  - `[ 🛡️ Order Mode ]` — Concise, bulleted, strict facts, executive answers.
  - `[ 🧠 Think Mode ]` — Shows step-by-step reasoning collapsible tray.
- **Floating Input Dock:**
  - Cal.com-style floating command input centered at the bottom.
  - Quick action chips: `Summarize`, `Critique my idea`, `Debug code`, `Unfiltered advice`.
  - Keyboard shortcut hints (`↵ Enter to send`, `⇧ Shift+↵ for new line`, `⌘K for commands`).

### 2. Dual-Engine Switcher (Offline / Online)
- Top-right status pill:
  - 🟢 **Local Engine (Ollama / Gemma 2)**: For privacy and offline use.
  - 🌐 **Cloud Engine (Ultra Fast)**: For browser visitors without local setup.

### 3. Integrated Terminal Preview
- A dedicated modal or split-view showing the live terminal bot (`app.py`), highlighting that Chaos Bot is both an elite web app and a high-performance CLI assistant.

---

## 5. Technical Architecture
- **Framework:** Astro.js (Zero-JS static baseline with Islands architecture).
- **Styling:** Tailwind CSS v4.
- **State Management:** Nanostores / lightweight reactive island for chat state and streaming.
- **CLI Compatibility:** The Python CLI in `app.py` remains 100% untouched and fully operational in any terminal.
