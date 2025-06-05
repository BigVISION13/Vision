from flask import Flask, render_template, request
from vision.workflow import parse_workflow
from vision.sales_ai import get_sales_advice

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    workflow = None
    sales_answer = None
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        sales_prompt = request.form.get('sales_prompt', '')
        if prompt:
            workflow = parse_workflow(prompt)
        if sales_prompt:
            sales_answer = get_sales_advice(sales_prompt)
    return render_template('index.html', workflow=workflow, sales_answer=sales_answer)


if __name__ == '__main__':
    app.run(debug=True)
