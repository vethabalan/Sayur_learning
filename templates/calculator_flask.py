from flask import Flask,render_template
app = Flask(__name__)
@app.route("/calculator")

def calculator():
    return render_template("html_calc.html")
@app.route("/calc")
def sqrt_calc():
    return render_template("sqrt_html.html")
app.run()

