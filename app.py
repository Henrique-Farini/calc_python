from flask import Flask, render_template, request

app = Flask(__name__)

expressao = ""

def parenteses_auto(expr):
    abertos = expr.count("(")
    fechados = expr.count(")")

    # se precisa abrir
    if abertos == fechados:
        return expr + "("

    # se ultimo char permite fechar
    if expr and expr[-1] not in "+-*/(":
        return expr + ")"

    return expr + "("


@app.route("/", methods=["GET","POST"])
def index():
    global expressao

    if request.method == "POST":
        btn = request.form.get("btn")

        if btn == "C":
            expressao = ""

        elif btn == "DEL":
            expressao = expressao[:-1]

        elif btn == "()":
            expressao = parenteses_auto(expressao)

        elif btn == "%":
            try:
                expressao = str(float(expressao) / 100)
            except:
                expressao = "Erro"

        elif btn == "=":
            try:
                expressao = str(eval(expressao))
            except:
                expressao = "Erro"

        else:
            expressao += btn

    return render_template("index.html", resultado=expressao)

if __name__ == "__main__":
    app.run(debug=True)