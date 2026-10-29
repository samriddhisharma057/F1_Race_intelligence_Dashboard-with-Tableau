from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renders the main dashboard and story page
    return render_template('index.html')

if __name__ == '__main__':
    # Runs local server on localhost:5000
    app.run(debug=True, port=5000)