try:
    from flask import Flask, render_template, request, jsonify
except ModuleNotFoundError:  # pragma: no cover - graceful fallback
    print("Flask is not installed. Please install dependencies from requirements.txt to run the web server.")
    import sys
    sys.exit(0)
from vision.workflow import parse_workflow
from vision.sales_ai import get_sales_advice
from vision.automation import generate_automation
from vision.response_generator import generate_response

# Tell Flask to look for templates inside the vision/templates directory
app = Flask(__name__, template_folder='vision/templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    workflow = None
    sales_answer = None
    automation = None
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        sales_prompt = request.form.get('sales_prompt', '')
        automation_prompt = request.form.get('automation_prompt', '')
        if prompt:
            workflow = parse_workflow(prompt)
        if sales_prompt:
            sales_answer = get_sales_advice(sales_prompt)
        if automation_prompt:
            automation = generate_automation(automation_prompt).to_dict()
    return render_template('index.html', workflow=workflow, sales_answer=sales_answer, automation=automation)


@app.route('/generate-response', methods=['POST'])
def generate_response_route():
    data = request.get_json(silent=True) or request.form
    context = data.get('context', '')
    style = data.get('style', '')
    generated = generate_response(context, style)
    if request.is_json:
        return jsonify({'response': generated})
    # when form is submitted, show result on the main page
    return render_template('index.html', workflow=None, sales_answer=None, automation=None, generated_response=generated)


@app.route('/parse-workflow', methods=['POST'])
def parse_workflow_route():
    """Parse a workflow prompt and return structured JSON."""
    data = request.get_json(silent=True) or request.form
    prompt = data.get('prompt', '')
    parsed = parse_workflow(prompt)
    return jsonify(parsed)


@app.route('/generate-automation', methods=['POST'])
def generate_automation_route():
    """Generate an automation flow from a plain language prompt."""
    data = request.get_json(silent=True) or request.form
    prompt = data.get('prompt', '')
    flow = generate_automation(prompt).to_dict()
    return jsonify(flow)


if __name__ == '__main__':
    app.run(debug=True)
