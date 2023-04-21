from flask import Flask, render_template, request, url_for, redirect
import csv
from controller import get_cupcakes, find_cupcakes, add_cupcake_dict

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cupcakes')
def all_cupcakes():
    cupcake_list = get_cupcakes("cupcakes.csv")
    return render_template('cupcakes.html', cupcakes=cupcake_list)

@app.route('/individual-cupcake/<cupcake>')
def indiv_cupcake():
    return render_template('indiv_cupcake.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/add-cupcake/<name>')
def add_cupcake(name):
    cupcake = find_cupcakes("cupcakes.csv", name)
    if cupcake:
        add_cupcake_dict("orders.csv", cupcake)
        return redirect(url_for("index"))
    else:
        return "Sorry, cupcake not found."




if __name__  == "__main__":
    app.debug = True
    app.run(debug=True, port=5000, host="localhost")