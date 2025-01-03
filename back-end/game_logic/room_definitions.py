from game_logic.room import Room
from game_logic.npc_definitions import create_npcs



def create_rooms():
    npcs = create_npcs()

    rooms = {
        1: Room(
            "Room 1",
            "A quiet room with a wooden door to the north.",
            {},
            images={"default": "http://192.168.192.25:5000/images/room1_default.jpeg"},
        ),
        2: Room(
            "Room 2",
            "A dimly lit room with a sword on the pedestal.",
            {"sword_present": True},
            items=["sword"],
            images={
                "default": "http://192.168.192.25:5000/images/room2_default.jpeg",
                "sword_present": "http://192.168.192.25:5000/images/room2_with_sword.jpeg",
            },
        ),
        3: Room(
            "Room 3",
            "A hallway connecting several rooms.",
            {},
            images={"default": "http://192.168.192.25:5000/images/room3_default.jpeg"},
        ),
        4: Room(
            "Room 4",
            "An empty room with a locked door to the north.",
            {},
            images={"default": "http://192.168.192.25:5000/images/room4_default.jpeg"},
        ),
        5: Room(
            "Room 5",
            "A room with an old wise man.",
            {},
            npc=npcs["wise_man"],
            images={"default": "http://192.168.192.25:5000/images/room5_default.jpeg"},
        ),
        6: Room(
            "Room 6",
            "A scorching room with molten lava flows and a fierce orc guarding a precious diamond.",
            {"npc_alive": True},
            npc=npcs["orc"],
            images={
                "default": "http://192.168.192.25:5000/images/room6_default.jpeg",
                "npc_alive": "http://192.168.192.25:5000/images/room6_orc_alive.jpeg",
            },
        ),
        7: Room(
            "Room 7",
            "A secluded haven where a gleaming dagger rests.",
            {"dagger_present": True},
            items=["dagger"],
            images={
                "default": "http://192.168.192.25:5000/images/room7_default.jpeg",
                "dagger_present": "http://192.168.192.25:5000/images/room7_with_dagger.jpeg",
            },
        ),
        8: Room(
            "Room 8",
            "A hidden alcove where a sturdy shield lies waiting in silence.",
            {"shield_present": True},
            items=["shield"],
            images={
                "default": "http://192.168.192.25:5000/images/room8_default.jpeg",
                "shield_present":"http://192.168.192.25:5000/images/room8_with_shield.jpeg",
            },
        ),
        9: Room(
            "Room 10",
            "A secluded retreat where an elegant bow rests in the shadows.",
            {"bow_present": True},
            items=["bow"],
            images={
                "default": "http://192.168.192.25:5000/images/room9_default.jpeg",
                "bow_present": "http://192.168.192.25:5000/images/room9_with_bow.jpeg",
            },
        ),
        10: Room(
            "Game Over",
            "Quest is Complete",
            {},
            images={"default": "http://192.168.192.25:5000/images/room10_default.jpeg"},
        ),
    }

    return rooms
