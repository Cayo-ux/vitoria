from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/surpresa')
def surpresa():
    return render_template('surpresa.html')

if __name__ == '__main__':
    app.run(debug=True)
