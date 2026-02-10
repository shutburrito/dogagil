# dogagil — Run instructions

To run the Flask app from this workspace (app copy is inside `.vscode` so it appears in Explorer):

1. From the repository root:

```bash
cd /workspaces/dogagil
python3 .vscode/app.py
```

If you use a virtual environment inside `.vscode` (optional):

```bash
source .vscode/.venv/bin/activate
python3 .vscode/app.py
```

Open http://127.0.0.1:5000/ in your browser.

If you prefer the app located at the repo root, move `.vscode/app.py` back to the repo root:

```bash
mv .vscode/app.py ./app.py
```
