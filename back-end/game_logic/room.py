from game_logic.npc import NPC

class Room:
    def __init__(self, name, description, state, items=None, npc=None, images=None):
        self.name = name
        self.description = description
        self.state = state  # Dictionary for room-specific states
        self.items = items or []
        self.npc = npc  # Instance of NPC
        self.images = images or {}

    def describe(self):
        description = f"\n{self.name}: {self.description}"
        if self.items:
            description += f"\nYou see: {', '.join(self.items)}"
        if self.npc:
            description += f"\nYou see {self.npc.name} here."
        return {"description":description,"image":self.display_image()}

    def describe_text_only(self):

        description = f"\n{self.name}: {self.description}"
        if self.items:
            description += f"\nYou see: {', '.join(self.items)}"
        if self.npc:
            description += f"\nYou see {self.npc.name} here."
        return description
        

    def display_image(self):
        for key, value in self.state.items():
            if value and key in self.images:
                return self.images[key]
        return self.images.get('default', '')
    
    def talk(self, state):
        if self.npc:
            dialogue = f"{self.npc.name} says: '{self.npc.dialogue}'"
            if "npc_talked" not in state:
                state["npc_talked"] = {}
            state["npc_talked"][self.npc.npc_id] = True  # Mark NPC as talked to
            return dialogue
        return "There is no one here to talk to."

    def take(self, item, state):
        if item in self.items:
            self.items.remove(item)
            state["inventory"].append(item)
            self.state[f"{item}_present"] = False
            return f"You take the {item}."
        return f"There is no {item} here to take."

    def attack(self, state):
        if self.npc and self.npc.required_item in state["inventory"]:
            reward = f"You attack {self.npc.name} with your {self.npc.required_item} and defeat them!"
            state["inventory"].append(f"{self.npc.reward}")
            self.npc = None 
            self.state["npc_alive"] = False # Remove NPC from room
            return reward
        elif self.npc:
            if self.npc.required_item == "no_defeat":
                return f"You cannot attack {self.npc.name}."
            return f"You need a {self.npc.required_item} to defeat {self.npc.name}."
        return "There is no one here to attack."

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "state": self.state,
            "items": self.items,
            "npc": self.npc.to_dict() if self.npc else None,
            "images": self.images,
        }

    @classmethod
    def from_dict(cls, data):
        npc = NPC.from_dict(data['npc']) if data['npc'] else None
        return cls(
            name=data['name'],
            description=data['description'],
            state=data['state'],
            items=data['items'],
            npc=npc,
            images=data['images']
        )
