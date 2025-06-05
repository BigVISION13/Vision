# Vision

Vision is a simple AI assistant and business development web app.

This project currently contains a minimal Flask application that parses natural
language prompts into actionable workflows. The parsing logic lives in
`vision/workflow.py` and the web interface is served from `app.py`.

The web UI also includes a small "Sales AI" helper. You can ask questions about
sales tactics and receive brief suggestions based on simple heuristics defined
in `vision/sales_ai.py`.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the development server:

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

The page provides two forms: one to parse workflow prompts and another to ask
the Sales AI for quick tips.
