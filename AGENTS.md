# AGENTS.md

## Architecture
- **Frontend-only / Serverless.** No backend, no database, no auth. Everything runs client-side.
- **Data flow:** On first load, render from `default_tasks.json` (local, instant). A "Live Fetch" button queries `tarkov.dev/api` (GraphQL) to refresh the graph from live data, overwriting the local cache.

## Tech Stack
- React (JavaScript/TypeScript via Vite or Next.js — TBD once scaffolded)
- React Flow (`@xyflow/react`) for interactive graph rendering
- TailwindCSS for styling
- Python 3 + `requests` for `scripts/update_default_tasks.py`

## Key Commands
```bash
npm install          # install deps
npm run dev          # start dev server on localhost:3000
npm run build        # production build
npm run lint         # lint (when configured)
npm run typecheck    # type-check (when TypeScript is used)

# Update the bundled task data after a wipe/patch:
pip install requests
python scripts/update_default_tasks.py
```

## Key Files
| File | Role |
|---|---|
| `default_tasks.json` | Bundled task graph — shipped with the app, loaded instantly |
| `scripts/update_default_tasks.py` | Fetches latest tasks from `tarkov.dev` GraphQL API and overwrites `default_tasks.json` |

## Conventions
- **Data source of truth is `tarkov.dev` GraphQL API.** The local JSON is a stale-but-fast snapshot.
- **No user state.** Read-only tool. No login, no saved progress.
- **Deploy anywhere static:** Vercel or GitHub Pages. Just point it at the built output directory.
- The Python script is an admin/dev tool, not part of the frontend build pipeline.
