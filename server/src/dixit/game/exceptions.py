

class GameException(Exception):

    @property
    def msg(self):
        return getattr(self, 'error', None) or str(self)


class GameDeckExhausted(GameException):
    """
    The card deck has been exhausted and dealing is not possible
    """


class GameRoundIncomplete(GameException):
    """
    The round can't be closed because actions are still pending
    """


class GameInvalidPlay(GameException):
    """
    The play can't be performed
    """
