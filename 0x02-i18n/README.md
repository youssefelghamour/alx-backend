# 0x02. i18n

## Overview
This project implements internationalization (i18n) features in a Flask application using Flask-Babel. It includes functionalities such as parameterizing templates, forcing locale with URL parameters, mocking user login, and inferring time zones.

## Files

| File Name             | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| 0-app.py              | Basic Flask app with a single route and index.html template.                |
| 1-app.py              | Configures Babel extension and sets up supported languages.                 |
| 2-app.py              | Implements get_locale function to determine the best-matched language.      |
| 3-app.py              | Parametrizes templates using Flask-Babel and translations.                  |
| 4-app.py              | Forces locale with URL parameter and implements related functionality.      |
| 5-app.py              | Mocks user login functionality and sets global user using before_request.   |
| 6-app.py              | Enhances get_locale to prioritize user's preferred locale.                  |
| 7-app.py              | Defines get_timezone function to select time zone based on URL or user.     |
| app.py                | Advanced task: Displays current time based on inferred time zone.           |
| templates/            | Directory containing HTML templates for the app.                            |
| translations/         | Directory containing translation files for different languages.             |
| babel.cfg             | Configuration file for Babel setup.                                         |