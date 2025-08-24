from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'properties.json')

def load_properties():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_properties(props):
    with open(DATA_FILE, 'w') as f:
        json.dump(props, f, indent=2)

@app.route('/')
def index():
    properties = load_properties()
    return render_template('index.html', properties=properties)

@app.route('/add', methods=['GET', 'POST'])
def add_property():
    if request.method == 'POST':
        properties = load_properties()
        prop = {
            'title': request.form['title'],
            'description': request.form['description'],
            'price': request.form['price'],
            'image_url': request.form['image_url']
        }
        properties.append(prop)
        save_properties(properties)
        return redirect(url_for('index'))
    return render_template('add_property.html')

if __name__ == '__main__':
    app.run(debug=True)
