# Main Game file
import copy
import tcod
from input_handlers import EventHandler
import entity_factories
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

    max_monsters_per_room = 2
    # * Loads tilesheet
    tileset = tcod.tileset.load_tilesheet(
        "./resources/icons.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # * Create a EventHandler and let it manage all events
    event_handler = EventHandler()

    # * Create player entity
    player = copy.deepcopy(entity_factories.player)

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player,
    )

    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

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
