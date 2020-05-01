from bernard import (
    layers as lyr,
)
from bernard.i18n import (
    translate as t,
)
from bernard.platforms.telegram import layers as tll

from src.did_the_rocket_launch_yet.states.base import BaseStateRocket
from src.did_the_rocket_launch_yet.store import cs


class WinState(BaseStateRocket):

    @cs.inject()
    async def handle(self, context) -> None:
        self.send(
            lyr.Text(t.WIN),
            lyr.Text(t.PLAY_AGAIN),
            tll.InlineKeyboard([
                [tll.InlineKeyboardCallbackButton(
                    text=t.YES_LAUNCH,
                    payload={
                        'action': 'play',
                    },
                )],
                [tll.InlineKeyboardCallbackButton(
                    text=t.NO_LAUNCH,
                    payload={
                        'action': 'no_play',
                    },
                )]
            ])
        )
