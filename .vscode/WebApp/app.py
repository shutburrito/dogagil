from flask import Flask,render_template
import os

# Point to templates folder in repo root
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
