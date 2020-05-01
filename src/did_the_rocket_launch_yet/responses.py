import logging

from bernard import (
    layers as lyr,
)
from bernard.i18n import (
    translate as t,
)
from bernard.platforms.telegram import layers as tll

from src.did_the_rocket_launch_yet.utils.urls_rocket import get_url_rocket_frame

logger = logging.getLogger('bisect')


def get_response_rocket_did_launch(mid):
    return [
        lyr.Text(get_url_rocket_frame(mid)),
        lyr.Text(t.LAUNCH),
        tll.InlineKeyboard([
            [tll.InlineKeyboardCallbackButton(
                text=t.YES_LAUNCH,
                payload={
                    'action': 'choose_option_player',
                    'current': mid,
                    'option': 'yes'
                },
            )],
            [tll.InlineKeyboardCallbackButton(
                text=t.NO_LAUNCH,
                payload={
                    'action': 'choose_option_player',
                    'current': mid,
                    'option': 'no'
                },
            )]
        ])
    ]
