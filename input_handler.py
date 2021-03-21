from typing import Optional

import tcod.event

from actions import Action, EscapeAction, BumpAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym
        t_event = tcod.event

        if key == t_event.K_UP:
            action = BumpAction(dx=0, dy=-1)
        elif key == t_event.K_DOWN:
            action = BumpAction(dx=0, dy=1)
        elif key == t_event.K_LEFT:
            action = BumpAction(dx=-1, dy=0)
        elif key == t_event.K_RIGHT:
            action = BumpAction(dx=1, dy=0)
        elif key == t_event.K_ESCAPE:
            action = EscapeAction()
        
        return action
