class Player:
    def __init__(self, state):
        self.state = state

    def handle_connection(self, connection, direction, rooms, state):
        """
        Handle conditional movement based on the provided connection.
        """
        if isinstance(connection, dict):  # Connection with conditions
            new_room_id = connection["room"]
            conditions = connection.get("conditions")

            # Check conditions
            if conditions:
                if "npc_talked" in conditions:
                    required_npc = conditions["npc_talked"]
                    if not state.get("npc_talked", {}).get(required_npc, False):
                        return f"You need to talk to {required_npc} first."
                if "item_required" in conditions:
                    required_item = conditions["item_required"]
                    if required_item not in state.get("inventory", []):
                        return f"You need the {required_item} to proceed."
        else:
            # Support for simple connections without conditions
            new_room_id = connection

        # Move to the new room
        state["current_room"] = new_room_id
        return f"You moved {direction} to {rooms[new_room_id].name}."

    def move(self, direction, rooms, connections, state):
        """
        Handle player movement based on the direction provided.
        """
        current_room_id = state["current_room"]
        
        if direction == "north":
            if current_room_id in connections and "north" in connections[current_room_id]:
                connection = connections[current_room_id]["north"]
                return self.handle_connection(connection, direction, rooms, state)
            return "You cannot move north from here."
        
        if direction == "south":
            if current_room_id in connections and "south" in connections[current_room_id]:
                connection = connections[current_room_id]["south"]
                return self.handle_connection(connection, direction, rooms, state)
            return "You cannot move south from here."
        
        if direction == "east":
            if current_room_id in connections and "east" in connections[current_room_id]:
                connection = connections[current_room_id]["east"]
                return self.handle_connection(connection, direction, rooms, state)
            return "You cannot move east from here."
        
        if direction == "west":
            if current_room_id in connections and "west" in connections[current_room_id]:
                connection = connections[current_room_id]["west"]
                return self.handle_connection(connection, direction, rooms, state)
            return "You cannot move west from here."
        
        return "Unknown direction."
