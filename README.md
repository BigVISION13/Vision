# Vision

Vision is a simple AI assistant and business development web app.

This project currently contains a minimal Flask application that parses natural
language prompts into actionable workflows. The parsing logic lives in
`vision/workflow.py` and the web interface is served from `app.py`.

The web UI also includes a small "Sales AI" helper. You can ask questions about
sales tactics and receive brief suggestions based on simple heuristics defined
in `vision/sales_ai.py`.

You can also generate basic automations from plain language descriptions. The
`vision/automation.py` module converts a prompt into a simple flow of actions
similar to tools like n8n.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the development server:

```bash
python app.py
```

Then open `http://localhost:5000/` in your browser. The Flask app serves its
UI from the root path using templates in `vision/templates`, so navigating
directly to `/` avoids 404 errors.

The page now provides four forms: one to parse workflow prompts, one to ask the
Sales AI for quick tips, another to generate an automation flow from a plain
language description, and a form for generating a short response in a chosen
style.

You can also run the lightweight API server via `vision_api.py`. It exposes a
`POST /generate-response` endpoint accepting JSON with `context` and `style` and
returns the generated message.

## React component example

A small React component is provided under `frontend/SalesResponseGenerator.jsx`.
It demonstrates how to call the `/generate-response` API endpoint from a
React-based UI. You can import this component into your own React application:

```jsx
import SalesResponseGenerator from './frontend/SalesResponseGenerator';
```

Make sure the Flask server is running locally so the component can post to
`http://localhost:5000/generate-response`.
