import json
import os
from game_logic.room import Room  # Import your Room class
from game_logic.npc import NPC
import copy
from mongo_db.db import get_db

# MongoDB connection 
db = get_db()
collection = db["game_saves"]  # Collection to store saved games

def save_game(account_id, state):
    try:
        # Create a deep copy of the current state to avoid modifying the original
        state_copy = copy.deepcopy(state)
        
        # Convert the room IDs to strings before saving
        state_copy['rooms'] = {str(room_id): room.to_dict() for room_id, room in state_copy['rooms'].items()}
        
        # Prepare the game save document
        game_save = {
            "account_id": account_id,
            "state": state_copy,
        }

        # Save the state to MongoDB
        result = collection.update_one(
            {"account_id": account_id},  # Find by account_id
            {"$set": game_save},  # Update the state if found, or insert if not
            upsert=True  # If account_id doesn't exist, create a new entry
        )



        return f"Game saved for account ID: {account_id}"
    except Exception as e:
        return f"Error saving game for account ID {account_id}: {e}"


def load_game(account_id):
    try:
        # Fetch the saved game from MongoDB
        game_save = collection.find_one({"account_id": account_id})
        
        if game_save:
            state = game_save['state']
            
            # Function to recreate NPCs from saved data
            def recreate_npc(npc_data):
                if npc_data:  # Recreate NPC if present
                    return NPC(**npc_data)
                return None

            # Recreate the rooms directly from the saved data
            def recreate_room(room_data):
                # Pass saved data directly to the Room constructor
                room = Room(
                    name=room_data["name"],
                    description=room_data["description"],
                    state=room_data["state"],  # Use saved state directly
                    items=room_data["items"],  # Restore items from saved data
                    npc=recreate_npc(room_data["npc"]),  # NPC from saved data
                    images=room_data["images"],  # Preserve base64 images
                )
                return room

            # Recreate rooms with their states
            state['rooms'] = {int(room_id): recreate_room(room_data) for room_id, room_data in state['rooms'].items()}

            # Ensure npc_talked is properly loaded
            state['npc_talked'] = state.get('npc_talked', {})
            
            return state
        return None
    except Exception as e:
        print(f"Error loading game: {e}")
        return f"Error loading game for account ID {account_id}: {e}"
