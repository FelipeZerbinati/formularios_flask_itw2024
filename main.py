from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    frutas = ["maçã", "banana", "laranja", "melancia", "uva", "mamão", "abacaxi"]
    return render_template("index.html", frutas_do_html=frutas)


if __name__ == '__main__':
    app.run(debug=True)