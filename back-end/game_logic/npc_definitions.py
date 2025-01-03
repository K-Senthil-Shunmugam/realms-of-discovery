# npc_definitions.py

from game_logic.npc import NPC

def create_npcs():
    return {
        "wise_man": NPC("wise_man", "Wise Man", "The path to wisdom is long, but you are ready for it. Make sure you get the bow before you face the orc.",required_item="no_defeat"),
        "orc": NPC("orc", "Fierce Orc", "The orc growls menacingly.", required_item="bow", reward="diamond"),
    }
