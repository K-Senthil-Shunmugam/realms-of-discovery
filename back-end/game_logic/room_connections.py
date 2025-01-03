def create_connections():
    return {
        1: {"north": {"room": 2, "conditions": None}},  
        2: {
            "south": {"room": 1, "conditions": None},
            "north": {"room": 3, "conditions": None},  
        },
        3: {
            "north": {"room": 5, "conditions": None},  
            "south": {"room": 2, "conditions": None},
            "east": {"room": 4, "conditions": None},
        },
        4: {
            "west": {"room": 3, "conditions": None},
            "north": {"room": 6, "conditions": {"npc_talked": "wise_man"}},  
        },
        5: {"south": {"room": 3, "conditions": None},
            "north": {"room":7,"conditions":{"item_required":"sword"}}
        }, 
        6: {"south": {"room": 4, "conditions": None},
            "north": {"room": 10, "conditions": {"item_required":"diamond"}}
        },  
        7:{
            "south": {"room": 5, "conditions": None},
            "north": {"room": 8, "conditions": {"item_required":"dagger"}},  
        },
        8:{
            "south": {"room": 7, "conditions": None},
            "north": {"room": 9, "conditions": {"item_required":"shield"}},  
        },
        9:{
            "south": {"room": 8, "conditions": None}
        }
    }
