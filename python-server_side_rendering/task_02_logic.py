#!/usr/bin/env python3
"""
Flask app that renders a dynamic list from JSON using Jinja loops
and conditions.
"""

import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def items_list():
    """Render page showing items loaded from items.json."""

    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items = data.get("items", [])
    except Exception:
        items = []

    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
