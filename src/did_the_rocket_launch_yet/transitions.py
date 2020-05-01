# coding: utf-8

from bernard.engine import (
    Tr,
    triggers as trg,
)
from bernard.platforms.telegram.layers import BotCommand

from .states import StartState, PlayState, ReTryState
from .states.no_play import NoPlayState
from .states.win import WinState
from .trigger import GameTrigger

transitions = [
    Tr(
        dest=StartState,
        factory=trg.Equal.builder(BotCommand('/start')),
    ),
    Tr(
        dest=NoPlayState,
        factory=trg.Action.builder('no_play')
    ),
    Tr(
        dest=PlayState,
        factory=trg.Action.builder('play')
    ),
    Tr(
        dest=ReTryState,
        origin=PlayState,
        factory=GameTrigger.builder(is_win=False)
    ),
    Tr(
        dest=ReTryState,
        origin=ReTryState,
        factory=GameTrigger.builder(is_win=False)
    ),
    Tr(
        dest=WinState,
        origin=ReTryState,
        factory=GameTrigger.builder(is_win=True)
    ),
    Tr(
        dest=WinState,
        origin=PlayState,
        factory=GameTrigger.builder(is_win=True)
    ),
]
