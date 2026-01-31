class PlayerDTO:
    """ """

    def __init__(self):
        self.nick_name: str | None = None

    def set_nick_name(self, nick_name: str):
        self.nick_name = nick_name
