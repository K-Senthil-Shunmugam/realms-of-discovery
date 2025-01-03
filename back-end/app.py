from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS  # Import CORS
from authentication.login import handle_login
from authentication.signup import handle_signup
from authentication.logout import handle_logout  # Assuming handle_logout is in logout.py
from werkzeug.security import check_password_hash
from datetime import datetime
from flask import Flask, request, jsonify
from game_logic.game import Game
from game_logic.utils import save_game, load_game
import json
import requests
import os


# Create Flask app
app = Flask(__name__)

# Enable CORS for all routes and allow credentials
CORS(app)

# Login Route (Using logic from login.py)
@app.route('/auth/login', methods=['POST'])
def login():
    return handle_login(request)

# Signup Route (Using logic from signup.py)
@app.route('/auth/signup', methods=['POST'])
def signup():
    return handle_signup(request)


# Logout Route
@app.route('/auth/logout', methods=['POST'])
def logout():
    return handle_logout(request)

 # Store game sessions for multiple users
game_sessions = {}

@app.route('/api/start_game', methods=['POST'])
def start_game():
    data = request.get_json()
    account_id = data.get('accountId')

    if account_id not in game_sessions:
        # Start a new game if no session exists for the account
        game = Game(account_id)
        game_sessions[account_id] = game
        return jsonify({
            "message": "New game started",
            "state": game.describe_current_room()
        })
    else:
        return jsonify({
            "message": "Game already started",
            "state": game_sessions[account_id].describe_current_room()
        })

@app.route('/api/load_game', methods=['POST'])
def load_game_route():
    data = request.get_json()
    account_id = data.get('accountId')

    game = game_sessions.get(account_id)

    if game:
        return jsonify({
            "message": "Game loaded successfully",
            "state": game.describe_current_room()
        })
    else:
        # Attempt to load saved game state from disk
        saved_state = load_game(account_id)
        if saved_state:
            game = Game(account_id, saved_state)
            game_sessions[account_id] = game
            return jsonify({
                "message": "Game loaded from saved state",
                "state": game.describe_current_room()
            })
        else:
            return jsonify({"message": "No saved game found for this account."}), 404

@app.route('/api/perform_action', methods=['POST'])
def perform_action():
    data = request.get_json()
    account_id = data.get('accountId')
    action = data.get('action')

    # Default the predicted action to the user-provided action
    predicted_action = action

    # Now, find the game session for the given account_id
    game = game_sessions.get(account_id)

    if game:
        # Process the action using the (predicted or user-provided) action
        result = game.process_action(predicted_action)
        room_desc = game.describe_current_room()

        # Return the result with updated room description and image
        return jsonify({
            "message": result,
            "state": room_desc["description"],
            "roomImageurl": room_desc["image"]
        })
    else:
        return jsonify({"message": "Game session not found!"}), 404

@app.route('/api/save_game', methods=['POST'])
def save_game_route():
    data = request.get_json()
    account_id = data.get('accountId')

    game = game_sessions.get(account_id)

    if game:
        # Save the game state to disk
        save_game(account_id, game.state)
        return jsonify({"message": "Game saved successfully!"})
    else:
        return jsonify({"message": "Game session not found!"}), 404

@app.route('/api/exit_game', methods=['POST'])
def exit_game():
    data = request.get_json()
    account_id = data.get('accountId')

    game = game_sessions.get(account_id)

    if game:
        # Save the game state before exiting
        save_game(account_id, game.state)
        del game_sessions[account_id]  # End the game session
        return jsonify({"message": "Game saved and session ended successfully!"})
    else:
        return jsonify({"message": "Game session not found!"}), 404


IMAGE_FOLDER = 'game_logic/room_images'

# Serve image from the 'images' folder
@app.route('/api/images/<filename>')
def serve_image(filename):
    # Ensure the file exists in the folder
    if os.path.exists(os.path.join(IMAGE_FOLDER, filename)):
        return send_from_directory(IMAGE_FOLDER, filename)
    else:
        return "Image not found", 404

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
