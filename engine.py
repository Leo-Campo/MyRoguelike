from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from entity import Entity
from input_handlers import EventHandler
from game_map import GameMap


class Engine:
    """
    Class responsible to create the console window, load the map and handling player actions
    """

    def __init__(
        self,
        entities: Set[Entity],
        event_handler: EventHandler,
        game_map: GameMap,
        player: Entity,
    ) -> None:
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        """
        Uses the given action_handler to handle actions
        """
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        """
        Renders the given set of entities on the console screen
        """
        self.game_map.render(console)
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)
        console.clear()