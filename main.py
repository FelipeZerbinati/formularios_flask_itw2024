#Arquivo main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

frutas = ["maçã", "banana", "laranja", "melancia", "uva", "mamão", "abacaxi"]

@app.route('/')
def home_page():
    return render_template("index.html", frutas_do_html=frutas)


@app.route('/inserir_frutas', methods=['GET', 'POST'])
def second_page():
    if request.method == 'POST':
        nova_fruta = request.form['fruta']
        frutas.append(nova_fruta)
        return redirect(url_for('home_page'))
    return render_template("index2.html")


if __name__ == '__main__':
    app.run(debug=True)
