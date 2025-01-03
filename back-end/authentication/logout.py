from flask import jsonify, make_response, request
from mongo_db.db import get_db
from bson import ObjectId


def handle_logout(request):
    """Handles user logout"""
    # Get the accountID from the request body
    data = request.get_json()
    account_id = data.get('accountID')  # Extract accountID from JSON body

    if not account_id:
        return jsonify({"message": "Account ID not provided"}), 404

    # Get the database
    db = get_db()


    # Find the user in the database
    user = db.users.find_one({"_id": ObjectId(account_id)})

    if not user:
        return jsonify({"message": "User not found","accountID":account_id}), 404

    # Create a response and delete the accountID cookie
    response = make_response(jsonify({"message": "Logout successful"}), 200)

    return response
