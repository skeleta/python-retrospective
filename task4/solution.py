class TicTacToeBoard:
    WINNING_KEYS = (['A1', 'A2', 'A3'],
                    ['B1', 'B2', 'B3'],
                    ['C1', 'C2', 'C3'],
                    ['A1', 'B1', 'C1'],
                    ['A2', 'B2', 'C2'],
                    ['A3', 'B3', 'C3'],
                    ['A1', 'B2', 'C3'],
                    ['A3', 'B2', 'C1'])
    GAME_IN_PROGRESS = 'Game in progress.'
    DRAW = 'Draw!'
    X_SIGN = 'X'
    O_SIGN = 'O'
    EMPTY = ' '
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
        self.status = __class__.GAME_IN_PROGRESS
        self.moves = []
        self.board = {"A1": " ", "B1": " ", "C1": " ",
                      "A2": " ", "B2": " ", "C2": " ",
                      "A3": " ", "B3": " ", "C3": " "}
        self._keys = [row + column
                      for column in __class__.COLUMN_NUMBERS
                      for row in __class__.ROW_LETTERS]

    def __setitem__(self, key, value):
        if value != self.X_SIGN and value != self.O_SIGN:
            raise InvalidValue("InvalidValue")
        if key not in self.board:
            raise InvalidKey("InvalidKey")
        if value == self.turn:
            raise NotYourTurn("NotYourTurn")
        if key in self.moves:
            raise InvalidMove("InvalidMove")
        if value == self.X_SIGN:
            self.turn = self.X_SIGN
        else:
            self.turn = self.O_SIGN
        self.board[key] = value
        self.moves.append(key)
        self.status = self.__update(key, value)

    def __getitem__(self, key):
        return self.board[key]

    def __str__(self):
        return (self.BOARD_FORMAT).format(*[self.board[key]
                                            for key in self._keys])

    def __winner(self, value):
        for key_line in self.WINNING_KEYS:
            if all(self.board[i] == value != self.EMPTY for i in key_line):
                return True
        return False

    def __update(self, key, value):
        status = self.status
        if self.status != self.GAME_IN_PROGRESS:
            return self.status
        if self.EMPTY not in self.board.values():
            return self.DRAW
        else:
            if self.__winner(value):
                return '{} wins!'.format(self.turn)
            else:
                return self.GAME_IN_PROGRESS

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
