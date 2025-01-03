from game_logic.player import Player
from game_logic.room_definitions import create_rooms
from game_logic.room_connections import create_connections

class Game:
    def __init__(self, account_id, state=None):
        self.account_id = account_id
        
        if state is None:
            self.rooms = create_rooms()
        else:
            self.rooms = state["rooms"]
        self.connections = create_connections()
        self.state = state or {
            "current_room": 1,
            "inventory": [],
            "door_open": False,
            "room_states": {},
            "rooms": self.rooms,
        }
        self.player = Player(self.state)

    def start(self):
        """
        Returns the start message of the game.
        """
        return "\nYour adventure begins!" + self.describe_current_room()

    def describe_current_room(self):
        """
        Returns the description of the current room.
        """
        return self.rooms[self.state["current_room"]].describe()

    def describe_current_room_only_text(self):
        """
        Returns the description of the current room.
        """
        return self.rooms[self.state["current_room"]].describe_text_only()

    def process_action(self, action):
        """
        Process the player input action and determine the correct room interaction.
        Returns appropriate messages based on actions.
        """
        current_room = self.rooms[self.state["current_room"]]
        
        if action == "look":
            return self.describe_current_room_only_text()

        elif action.startswith("move "):
            direction = action.split(" ")[1]
            move_result = self.player.move(direction, self.rooms, self.connections, self.state)
            return move_result 

        elif action.startswith("take "):
            item = action.split(" ")[1]
            return current_room.take(item, self.state)
        
        elif action == "talk":
            return current_room.talk(self.state)

        elif action == "attack":
            return current_room.attack(self.state)

        else:
            return "Action not recognized. Try again."
