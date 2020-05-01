from bernard import (
    layers as lyr,
)
from bernard.i18n import (
    translate as t,
)

from src.did_the_rocket_launch_yet.responses import get_response_rocket_did_launch
from src.did_the_rocket_launch_yet.states.base import BaseStateRocket
from src.did_the_rocket_launch_yet.store import cs
from src.did_the_rocket_launch_yet.utils.bisect import bisect


class ReTryState(BaseStateRocket):

    @cs.inject()
    async def handle(self, context) -> None:
        try:
            payload = self.request.get_layer(lyr.Postback).payload
        except KeyError:
            self.send(
                lyr.Text(t.DONT_PLAY)
            )
            return
        else:
            mid = int(payload.get('current', 0))
            option = payload.get('option', 'no')

            context['count'] += 1

            if option == 'no':
                context['left'] = mid
                context['left'], context['right'], mid = bisect(context.get('left'),
                                                                context.get('right', context.get('size')))
            else:
                context['right'] = mid
                context['left'], context['right'], mid = bisect(context.get('left'),
                                                                context.get('right', context.get('size')))

            self.send(*get_response_rocket_did_launch(mid))
