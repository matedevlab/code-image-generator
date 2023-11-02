from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def code():
    context = {
        "message": "I'm hungry for your python code!",
    }
    return render_template("code_input.html", **context)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
