# Vision

Vision is a simple AI assistant and business development web app.

This project currently contains a minimal Flask application that parses natural
language prompts into actionable workflows. The parsing logic lives in
`vision/workflow.py` and the web interface is served from `app.py`.

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
