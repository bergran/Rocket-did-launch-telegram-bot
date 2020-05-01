from bernard import (
    layers as lyr,
)
from bernard.i18n import (
    translate as t,
)

from src.did_the_rocket_launch_yet.states.base import BaseStateRocket
from src.did_the_rocket_launch_yet.store import cs


class NoPlayState(BaseStateRocket):

    @cs.inject()
    async def handle(self, context) -> None:
        self.send(
            lyr.Text(t.DONT_PLAY),
        )
