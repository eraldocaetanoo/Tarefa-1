from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    return 'O resultado é: '+ str(int(request.form["n1"])+int(request.form["n2"]))

@app.route("/autor")
def autor():
    return render_template("autor.html")

if __name__ == '__main__':
    app.run(debug=True)
