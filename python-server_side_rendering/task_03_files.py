#!/usr/bin/env python3
"""
Flask app that reads product data from JSON or CSV and displays it.
"""

import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def load_from_json():
    """Load product data from products.json."""
    try:
        with open("products.json", "r") as file:
            data = json.load(file)
            return data
    except Exception:
        return None


def load_from_csv():
    """Load product data from products.csv."""
    products = []
    try:
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id + price to proper types
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except Exception:
        return None


@app.route("/products")
def display_products():
    """Render products from JSON or CSV depending on ?source=."""
    source = request.args.get("source")
    item_id = request.args.get("id")

    error = None
    products = None

    # Validate source
    if source == "json":
        products = load_from_json()
    elif source == "csv":
        products = load_from_csv()
    else:
        error = "Wrong source"

    # If file-loading failed
    if products is None and error is None:
        error = "Error loading data"

    # Filter by id
    selected_product = None
    if item_id and products:
        try:
            item_id = int(item_id)
            for p in products:
                if p["id"] == item_id:
                    selected_product = [p]    # wrap in list for template loop
                    break
            if selected_product is None:
                error = "Product not found"
        except ValueError:
            error = "Product not found"

    # If ID provided AND found → only display that product
    if selected_product:
        products_to_display = selected_product
    else:
        products_to_display = products

    return render_template(
        "product_display.html",
        products=products_to_display,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
