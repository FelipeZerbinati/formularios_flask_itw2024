from flask import Flask, render_template, request

app = Flask(__name__)
frutas = ["maçã", "banana", "laranja", "melancia", "uva", "mamão", "abacaxi"]

@app.route('/', methods = {'GET', 'POST'})
def home_page():
    
    if request.method == 'POST':
        if request.form.get('fruta'):
            frutas.append(request.form.get("fruta"))

    return render_template("index.html", frutas_do_html=frutas)


if __name__ == '__main__':
    app.run(debug=True)