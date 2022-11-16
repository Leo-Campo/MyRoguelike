from __future__ import annotations
from typing import Set, Iterable, Any, TYPE_CHECKING
from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap
    from input_handlers import EventHandler

from input_handlers import MainGameEventHandler


class Engine:
    """
    Class responsible to create the console window, load the map and handling player actions
    """

    def __init__(
        self,
        player: Actor,
    ) -> None:
        self.event_handler = MainGameEventHandler(self)
        self.player = player

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                entity.ai.perform()

    def handle_events(self, events: Iterable[Any]) -> None:
        """
        Uses the given action_handler to handle actions
        """
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)
            self.handle_enemy_turns()
            self.update_fov()  # * Update the fov before the players next action

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view"""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # * If a tile is "visible" it should be added to "explored"
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, context: Context) -> None:
        """
        Renders the map
        The map itself will render its entities
        """
        self.game_map.render(console)

        console.print(
            x=1, y=47, string=f"{self.player.fighter.hp}/{self.player.fighter.max_hp}"
        )

        context.present(console)
        console.clear()
