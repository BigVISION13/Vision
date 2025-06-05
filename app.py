from flask import Flask, render_template, request
from vision.workflow import parse_workflow
from vision.sales_ai import get_sales_advice
from vision.automation import generate_automation

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


if __name__ == '__main__':
    app.run(debug=True)
