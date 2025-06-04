from flask import Flask, render_template, request
from vision.workflow import parse_workflow

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    workflow = None
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        workflow = parse_workflow(prompt)
    return render_template('index.html', workflow=workflow)


if __name__ == '__main__':
    app.run(debug=True)
