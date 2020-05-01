import logging

from bernard import (
    layers as lyr,
)
from bernard.engine.triggers import BaseTrigger

from src.did_the_rocket_launch_yet.store import cs

logger = logging.getLogger('bisect')

class GameTrigger(BaseTrigger):
    """
    This trigger will try to interpret what the user sends as a number. If it
    is a number, then it's compared to the number to guess in the context.
    The `is_win` parameter allows to say if you want the trigger to activate
    when the guess is right or not.
    """

    def __init__(self, request, is_win):
        super().__init__(request)
        self.is_win = is_win

    # noinspection PyMethodOverriding
    @cs.inject()
    async def rank(self, context) -> float:
        try:
            self.request.get_layer(lyr.Postback).payload
        except KeyError:
            return .0

        left = context.get('left')
        right = context.get('right')
        if left is None or right is None:
            return .0

        logger.debug(context)
        is_win = context.get('count') >= 16 or left + 1 >= right

        return 1. if is_win == self.is_win else .0
