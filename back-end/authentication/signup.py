from flask import jsonify
from mongo_db.db import get_db
from werkzeug.security import generate_password_hash
from datetime import datetime

def handle_signup(request):
    """Handles user signup"""
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    db = get_db()

    # Check if the username or email already exists
    if db.users.find_one({"username": username}):
        return jsonify({"message": "Username already exists"}), 400
    
    if db.users.find_one({"email": email}):
        return jsonify({"message": "Email already registered"}), 400

    # Hash the password and create the user
    password_hash = generate_password_hash(password)
    new_user = {
        "username": username,
        "email": email,
        "passwordHash": password_hash,
        "creationDate": datetime.utcnow(),
        "lastLogin": None
    }
    
    db.users.insert_one(new_user)
    return jsonify({"message": "User created successfully"}), 201
