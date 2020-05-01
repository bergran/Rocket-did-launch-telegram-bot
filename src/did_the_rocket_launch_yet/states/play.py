from bernard import (
    layers as lyr,
)
from bernard.i18n import (
    translate as t,
)

from src.did_the_rocket_launch_yet.requests import get_video_info
from src.did_the_rocket_launch_yet.responses import get_response_rocket_did_launch
from src.did_the_rocket_launch_yet.states.base import BaseStateRocket
from src.did_the_rocket_launch_yet.store import cs
from src.did_the_rocket_launch_yet.utils.bisect import bisect


class PlayState(BaseStateRocket):

    @cs.inject()
    async def handle(self, context) -> None:
        response = await get_video_info()

        if response:
            context['count'] = 0
            context['size'] = response.get('frames', 0)
            context['left'], context['right'], mid = bisect(0, context['size'] - 1)

            self.send(*get_response_rocket_did_launch(mid))
        else:
            self.send(
                lyr.Text(t.ERROR)
            )
