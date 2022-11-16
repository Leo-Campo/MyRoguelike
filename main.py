# Main Game file

import tcod
from input_handlers import EventHandler
from entity import Entity
from engine import Engine
from game_map import GameMap
from procgen import generate_dungeon


def main() -> None:
    # * Display measurements in tiles
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    # * Loads tilesheet
    tileset = tcod.tileset.load_tilesheet(
        "./resources/icons.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # * Create a EventHandler and let it manage all events
    event_handler = EventHandler()

    # * Create player entity
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player,
    )

    engine = Engine(
        entities=entities, event_handler=event_handler, game_map=game_map, player=player
    )

    # * New Terminal
    with tcod.context.new_terminal(
        screen_width, screen_height, tileset=tileset, title="MyRogueLike", vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_width, order="F")

        # * Game loop
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
