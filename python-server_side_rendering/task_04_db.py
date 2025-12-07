#!/usr/bin/env python3
"""
Flask app that loads product data from JSON, CSV, or SQLite database
and displays it on an HTML template.
"""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def load_from_json():
    """Load products from JSON file."""
    try:
        with open("products.json", "r") as file:
            data = json.load(file)
            return data
    except Exception:
        return None


def load_from_csv():
    """Load products from CSV file."""
    products = []
    try:
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except Exception:
        return None


def load_from_sqlite():
    """Load products from SQLite database file."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": float(row[3])
            })

        return products
    except Exception:
        return None


@app.route("/products")
def display_products():
    """
    Display product data based on ?source=json|csv|sql
    and optional ?id=<number>.
    """
    source = request.args.get("source")
    item_id = request.args.get("id")

    error = None
    products = None

    # Choose data source
    if source == "json":
        products = load_from_json()
    elif source == "csv":
        products = load_from_csv()
    elif source == "sql":
        products = load_from_sqlite()
    else:
        error = "Wrong source"

    # If loading failed
    if products is None and error is None:
        error = "Error loading data"

    # Filter by id
    selected_product = None
    if item_id and products:
        try:
            item_id = int(item_id)
            for p in products:
                if p["id"] == item_id:
                    selected_product = [p]
                    break
            if selected_product is None:
                error = "Product not found"
        except ValueError:
            error = "Product not found"

    # Select final set of products to render
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
