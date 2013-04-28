class TicTacToeBoard:
    GAME_IN_PROGRESS = 'Game in progress.'
    X_WINS = 'X wins!'
    Y_WINS = 'Y wins!'
    DRAW = 'Draw!'
    X_SIGN = 'X'
    O_SIGN = 'O'

    def __init__(self):
        self.turn = None
        self.we_have_a_result = False
        self.status = __class__.GAME_IN_PROGRESS
        self.moves = []
        self.board = {"A1": " ", "B1": " ", "C1": " ",
                      "A2": " ", "B2": " ", "C2": " ",
                      "A3": " ", "B3": " ", "C3": " "}
        self.rows = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]

    def __setitem__(self, key, value):
        if value != __class__.X_SIGN and value != __class__.O_SIGN:
            raise InvalidValue("InvalidValue")
        if key not in self.board:
            raise InvalidKey("InvalidKey")
        if self.turn == value:
            raise NotYourTurn("NotYourTurn")
        if key in self.moves:
            raise InvalidMove("InvalidMove")
        if value == __class__.X_SIGN:
            self.turn = __class__.X_SIGN
        else:
            self.turn = __class__.O_SIGN
        self.board[key] = value
        self.rows = [[self.board["A3"], self.board["B3"], self.board["C3"]],
                     [self.board["A2"], self.board["B2"], self.board["C2"]],
                     [self.board["A1"], self.board["B1"], self.board["C1"]]]
        self.moves.append(key)
        self.status = self.update(key, value)

    def __getitem__(self, key):
        return self.board[key]

    def __str__(self):
        return '\n  -------------\n' +\
            '3 | ' + self.board["A3"] + ' | ' + self.board["B3"] +\
            ' | ' + self.board["C3"] + ' |\n' +\
            '  -------------\n' +\
            '2 | ' + self.board["A2"] + ' | ' + self.board["B2"] +\
            ' | ' + self.board["C2"] + ' |\n' +\
            '  -------------\n' +\
            '1 | ' + self.board["A1"] + ' | ' + self.board["B1"] +\
            ' | ' + self.board["C1"] + ' |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'



    def update(self, kay, value):
        status = self.status
        if self.status != __class__.GAME_IN_PROGRESS:
            return self.status
        if " " not in self.board.values():
            return __class__.DRAW
        else:
            for i in range(0, 3):
                if self.rows[i][0] == self.rows[i][1] == self.rows[i][2] != " " \
                        or self.rows[0][i] == self.rows[1][i] == self.rows[2][i] \
                        != " ":
                    if self.we_have_a_result is not True:
                        self.we_have_a_result = True
                        status = self.turn + ' wins!'
            if self.rows[0][0] == self.rows[1][1] == self.rows[2][2] != " " \
                    or self.rows[2][0] == self.rows[1][1] == self.rows[0][2] \
                    != " ":
                if self.we_have_a_result is not True:
                    self.we_have_a_result = True
                    status = self.turn + ' wins!'
        return status

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
