from bernard import (
    layers as lyr,
)
from bernard.i18n import (
    translate as t,
)
from bernard.platforms.telegram import (
    layers as tll
)

from src.did_the_rocket_launch_yet.states.base import BaseStateRocket


class StartState(BaseStateRocket):

    async def handle(self) -> None:
        name = await self.request.user.get_friendly_name()

        self.send(
            lyr.Text(t('WELCOME', name=name)),
            tll.InlineKeyboard([
                [tll.InlineKeyboardCallbackButton(
                    text=t.YES_START,
                    payload={'action': 'play'},
                )],
                [tll.InlineKeyboardCallbackButton(
                    text=t.NO_START,
                    payload={'action': 'no_play'},
                )]
            ]))
