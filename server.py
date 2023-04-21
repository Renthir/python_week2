from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cupcakes')
def all_cupcakes():
    return render_template('cupcakes.html')

@app.route('/indiv_cupcake')
def indiv_cupcake():
    return render_template('indiv_cupcake.html')

@app.route('/order')
def order():
    return render_template('order.html')


if __name__  == "__main__":
    app.debug = True
    app.run(debug=True, port=5000, host="localhost")