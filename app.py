from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import Python3Lexer
import config

app = Flask(__name__)
app.config.from_object(config)

PLACEHOLDER_CODE = "print('Hello, World!')"


@app.route("/", methods=["GET"])
def code():
    if session.get("code") is None:
        session["code"] = PLACEHOLDER_CODE
    lines = session["code"].split("\n")
    context = {
        "message": "Paste Your Python Code 🐍",
        "code": session["code"],
        "num_lines": len(lines),
        "max_chars": len(max(lines, key=len)),
    }
    return render_template("code_input.html", **context)


@app.route("/save_code", methods=["POST"])
def save_code():
    session["code"] = request.form.get("code")
    return redirect(url_for("code"))


@app.route("/reset_session", methods=["POST"])
def reset_session():
    session.clear()
    session["code"] = PLACEHOLDER_CODE
    return redirect(url_for("code"))


@app.route("/style", methods=["GET"])
def style():
    formatter = HtmlFormatter()
    context = {
        "message": "Select Your Style 🎨",
        "style_definitions": formatter.get_style_defs(),
        "style_bg_color": formatter.style.background_color,
        "highlighted_code": highlight(session["code"], Python3Lexer(), formatter),
    }
    return render_template(url_for("style_selection.html", **context))


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
