from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
import config

app = Flask(__name__)
app.config.from_object(config)

PLACEHOLDER_CODE = "print('Hello, World!')"


@app.route("/", methods=["GET"])
def code():
    if session.get("code") is None:
        session["code"] = PLACEHOLDER_CODE
    context = {
        "message": "Paste Your Python Code 🐍",
        "code": session["code"],
    }
    return render_template("code_input.html", **context)


@app.route("/save_code", methods=["POST"])
def save_code():
    session["code"] = request.get("code")
    return redirect(url_for("code"))


@app.route("/reset_session", methods=["POST"])
def reset_sesion():
    session.clear()
    session["code"] = PLACEHOLDER_CODE
    return redirect(url_for("code"))


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
