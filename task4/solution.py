class TicTacToeBoard:
    def __init__(self):
        self.turn = None
        self.we_have_a_result = False
        self.status = "Game in progress."
        self.moves = []
        self.items = {"A1": " ", "B1": " ", "C1": " ",
                      "A2": " ", "B2": " ", "C2": " ",
                      "A3": " ", "B3": " ", "C3": " "}
        self.rows = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]

    def __setitem__(self, i, y):
        if y != "X" and y != "O":
            raise InvalidValue("InvalidValue")
        if i not in self.items:
            raise InvalidKey("InvalidKey")
        if self.turn == y:
            raise NotYourTurn("NotYourTurn")
        if i in self.moves:
            raise InvalidMove("InvalidMove")
        if y == "X":
            self.turn = "X"
        else:
            self.turn = "O"
        self.items[i] = y
        self.rows = [[self.items["A3"], self.items["B3"], self.items["C3"]],
                     [self.items["A2"], self.items["B2"], self.items["C2"]],
                     [self.items["A1"], self.items["B1"], self.items["C1"]]]
        self.moves.append(i)
        self.game_current_status()

    def __getitem__(self, i):
        return self.items[i]

    def __str__(self):
        return '\n  -------------\n' +\
            '3 | ' + self.items["A3"] + ' | ' + self.items["B3"] +\
            ' | ' + self.items["C3"] + ' |\n' +\
            '  -------------\n' +\
            '2 | ' + self.items["A2"] + ' | ' + self.items["B2"] +\
            ' | ' + self.items["C2"] + ' |\n' +\
            '  -------------\n' +\
            '1 | ' + self.items["A1"] + ' | ' + self.items["B1"] +\
            ' | ' + self.items["C1"] + ' |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'

    def game_current_status(self):
        for i in range(0, 3):
            if self.rows[i][0] == self.rows[i][1] == self.rows[i][2] != " " \
                    or self.rows[0][i] == self.rows[1][i] == self.rows[2][i] \
                    != " ":
                if self.we_have_a_result is not True:
                    self.we_have_a_result = True
                    self.status = self.turn + ' wins!'
        if self.rows[0][0] == self.rows[1][1] == self.rows[2][2] != " " \
                or self.rows[2][0] == self.rows[1][1] == self.rows[0][2] \
                != " ":
            if self.we_have_a_result is not True:
                self.we_have_a_result = True
                self.status = self.turn + ' wins!'
        if " " not in self.rows[0] and " " not in self.rows[1] \
                and " " not in self.rows[2]:
            if self.we_have_a_result is not True:
                self.we_have_a_result = True
                self.status = 'Draw!'

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
