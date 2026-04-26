# AGENTS.md

## Architecture
- **Frontend-only / Serverless.** No backend, no database, no auth. Everything runs client-side.
- **Data flow:** On first load, render from `default_tasks.json` (local, instant). A "Live Fetch" button queries `tarkov.dev/api` (GraphQL) to refresh the graph from live data, overwriting the local cache.

## Tech Stack
- React 19 + TypeScript via Vite 7
- React Flow (`@xyflow/react`) for interactive graph rendering
- TailwindCSS v4 (`@tailwindcss/vite` plugin)
- Python 3 + `requests` for `scripts/update_default_tasks.py`

## Key Commands
```bash
npm install          # install deps (Node >= 20)
npm run dev          # start dev server on http://0.0.0.0:3000
npm run build        # typecheck + vite build → dist/
npm run preview      # preview production build on http://0.0.0.0:4173
npm run lint         # ESLint
npm run typecheck    # tsc --noEmit (app + config projects)

# Update the bundled task data after a wipe/patch:
pip install -r requirements.txt
python scripts/update_default_tasks.py
```

## Key Files
| File | Role |
|---|---|
| `index.html` | Vite entry point |
| `src/main.tsx` | React mount point + Tailwind CSS import |
| `src/App.tsx` | Root component |
| `default_tasks.json` | Bundled task graph — shipped with the app, loaded instantly |
| `scripts/update_default_tasks.py` | Fetches latest tasks from `tarkov.dev` GraphQL API and overwrites `default_tasks.json` |
| `requirements.txt` | Python dependencies for the admin script |

## Conventions
- **Data source of truth is `tarkov.dev` GraphQL API.** The local JSON is a stale-but-fast snapshot.
- **No user state.** Read-only tool. No login, no saved progress.
- **Deploy anywhere static:** Vercel or GitHub Pages. Just point it at the built output directory.
- The Python script is an admin/dev tool, not part of the frontend build pipeline.
- **Build artifacts (`vite.config.js`, `vite.config.d.ts`, `*.tsbuildinfo`) must never be committed.** `.gitignore` covers them.
