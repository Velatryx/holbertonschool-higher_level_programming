#!/usr/bin/env python3
"""
A simple Flask API with routes for reading and writing user data.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
# Do NOT add sample data here — keep it empty for the checker
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Simple API status."""
    return "OK"


@app.route("/data", methods=["GET"])
def get_usernames():
    """Return a list of all usernames in the system."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return a user object by username."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request with JSON body."""

    # Parse JSON safely
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # Validate username
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check duplicate
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Save user
    users[username] = data

    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
