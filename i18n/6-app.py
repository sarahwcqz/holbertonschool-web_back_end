#!/usr/bin/env python3
"""Flask application whose locale also comes from the user's settings."""

from typing import Dict, Optional
from flask import Flask, g, render_template, request
from flask_babel import Babel


class Config:
    """Configuration of the app: supported languages, locale and timezone."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """Return the user matching the login_as URL parameter, if any."""
    login_as = request.args.get("login_as")
    try:
        return users.get(int(login_as))
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """Store the current user, if any, on flask.g before each request."""
    g.user = get_user()


def get_locale() -> Optional[str]:
    """Pick the locale from the URL, the user settings, then the browser."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    user = g.get("user")
    if user and user["locale"] in app.config["LANGUAGES"]:
        return user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index() -> str:
    """Render the home page of the application."""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()
