#!/usr/bin/env python3
"""Flask application configured with Babel for internationalization."""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration of the app: supported languages, locale and timezone."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index() -> str:
    """Render the home page of the application."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
