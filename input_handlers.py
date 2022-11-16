# Transforms player input in actions
from typing import Optional

import tcod.event

from actions import Action, EscapeAction, BumpAction

#! Defines main transform input => action
class EventHandler(tcod.event.EventDispatch[Action]):
    # * Event received is QUIT
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    # * Event received is a key being pressed
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        # * Maps directional key to movement, 1 tile per press
        if key == tcod.event.K_UP:
            action = BumpAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(dx=1, dy=0)

        # * Invokes closing action when esc is pressed
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        #! returns null if no valid action is invoked
        return action
