class TicTacToeBoard:
    ALL_LINES = {"A1": (("A2", "A3"), ("B1", "C1"), ("B2", "C3")),
                 "A2": (("A1", "A3"), ("B2", "C2")),
                 "A3": (("A1", "A2"), ("B3", "C3"), ("B2", "C1")),
                 "B1": (("B2", "B3"), ("A1", "C1")),
                 "B2": (("B1", "B3"), ("A2", "C2"),
                        ("A1", "C3"), ("A3", "C1")),
                 "B3": (("B1", "B2"), ("A3", "C3")),
                 "C1": (("C2", "C3"), ("A1", "B1"), ("A3", "C2")),
                 "C2": (("C1", "C3"), ("A2", "B2")),
                 "C3": (("C1", "C2"), ("A3", "B3"), ("A1", "B2"))}
    GAME_IN_PROGRESS = 'Game in progress.'
    DRAW = 'Draw!'
    X_SIGN = 'X'
    O_SIGN = 'O'
    COLUMN_NUMBERS = '321'
    ROW_LETTERS = 'ABC'
    BOARD_FORMAT = '\n' +\
                   '  -------------\n' +\
                   '3 | {} | {} | {} |\n' +\
                   '  -------------\n' +\
                   '2 | {} | {} | {} |\n' +\
                   '  -------------\n' +\
                   '1 | {} | {} | {} |\n' +\
                   '  -------------\n' +\
                   '    A   B   C  \n'

    def __init__(self):
        self.turn = None
        self.we_have_a_result = False
        self.status = __class__.GAME_IN_PROGRESS
        self.moves = []
        self.board = {"A1": " ", "B1": " ", "C1": " ",
                      "A2": " ", "B2": " ", "C2": " ",
                      "A3": " ", "B3": " ", "C3": " "}
        self.keys = [row + column
                     for column in __class__.COLUMN_NUMBERS
                     for row in __class__.ROW_LETTERS]

    def __setitem__(self, key, value):
        if value != __class__.X_SIGN and value != __class__.O_SIGN:
            raise InvalidValue("InvalidValue")
        if key not in self.board:
            raise InvalidKey("InvalidKey")
        if value == self.turn:
            raise NotYourTurn("NotYourTurn")
        if key in self.moves:
            raise InvalidMove("InvalidMove")
        if value == __class__.X_SIGN:
            self.turn = __class__.X_SIGN
        else:
            self.turn = __class__.O_SIGN
        self.board[key] = value
        self.moves.append(key)
        self.status = self.update(key, value)

    def __getitem__(self, key):
        return self.board[key]

    def __str__(self):
        return (__class__.BOARD_FORMAT).format(*[self.board[key]
                                                 for key in self.keys])

    def winner(self, key, value):
        key_lines = __class__.ALL_LINES[key]
        for line in key_lines:
            if self.board[line[0]] == value and self.board[line[1]] == value:
                return value
        return False

    def update(self, key, value):
        status = self.status
        if self.status != __class__.GAME_IN_PROGRESS:
            return self.status
        if " " not in self.board.values():
            return __class__.DRAW
        else:
            if self.winner(key, value):
                return '{} wins!'.format(self.winner(key, value))
            else:
                return __class__.GAME_IN_PROGRESS

    def game_status(self):
        return self.status


class NotYourTurn(Exception):
    pass


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass
