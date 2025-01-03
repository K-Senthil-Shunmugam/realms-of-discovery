# npc.py

class NPC:
    def __init__(self, npc_id, name, dialogue, required_item=None, reward=None):
        self.npc_id = npc_id
        self.name = name
        self.dialogue = dialogue
        self.required_item = required_item  # The item needed to defeat this NPC
        self.reward = reward  # The reward for defeating this NPC

    def to_dict(self):
        return {
            "npc_id": self.npc_id,
            "name": self.name,
            "dialogue": self.dialogue,
            "required_item": self.required_item,
            "reward": self.reward
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            npc_id=data['npc_id'],
            name=data['name'],
            dialogue=data['dialogue'],
            required_item=data.get('required_item'),
            reward=data.get('reward')
        )
