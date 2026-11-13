#!/usr/bin/env python3
"""Flask application whose locale can be forced with a URL parameter."""

from typing import Optional
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration of the app: supported languages, locale and timezone."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale() -> Optional[str]:
    """Pick the locale from the URL parameter, else from the browser."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index() -> str:
    """Render the home page of the application."""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
