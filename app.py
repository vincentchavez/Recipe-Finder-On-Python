# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    # You can handle the search functionality here
    return render_template('results.html', search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True)
