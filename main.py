# Main Game file
import copy
import tcod
import entity_factories
from procgen import generate_dungeon
from engine import Engine


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

    # * Create player entity
    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)
    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        max_monsters_per_room=max_monsters_per_room,
        map_width=map_width,
        map_height=map_height,
        engine=engine,
    )

    engine.update_fov()

    # * New Terminal
    with tcod.context.new_terminal(
        screen_width, screen_height, tileset=tileset, title="MyRogueLike", vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_width, order="F")

        # * Game loop
        while True:
            engine.render(console=root_console, context=context)
            engine.event_handler.handle_events()

            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
