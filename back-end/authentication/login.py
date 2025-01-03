from flask import jsonify, make_response
from mongo_db.db import get_db
from werkzeug.security import check_password_hash
from datetime import datetime

def handle_login(request):
    """Handles user login"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    db = get_db()
    user = db.users.find_one({"username": username})

    if not user or not check_password_hash(user['passwordHash'], password):
        return jsonify({"message": "Please Check your username & password"}), 401

    # Update last login time
    db.users.update_one({"username": username}, {"$set": {"lastLogin": datetime.utcnow()}})
    
    # Create a response and set the cookie with accountID
    response = make_response(jsonify({"message": "Login successful","accountID":str(user['_id'])}), 200)

    return response