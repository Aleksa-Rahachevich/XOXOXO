# import numpy as np


class Field:
    def __init__(self, number_of_rows, number_of_columns):
        self.number_of_columns = number_of_columns
        self.number_of_rows = number_of_rows
        self.space = []
        for i in range(number_of_rows):
            self.space.append(["."] * number_of_columns)


class Players:
    def __init__(self, first, second=None):
        self.first = first
        self.second = second


class Game:
    def __init__(self, players, field, game_move=0):
        self.players = players
        self.field = field
        self._game_move = game_move

    def computer_or_player(self):
        if self.players.second is None:
            self.computer_actions()
        else:
            self.players_actions()

    def computer_actions(self):
        self.players.second = "Computer"
 # self.moves()

    def players_actions(self):
        self.player_row_number = int(self.input_row()) - 1
        self.player_column_number = int(self.input_column()) - 1
        return self.player_column_number, self.player_row_number

    def moves(self):
        self.print()
        while not self.game_is_over():
            self.computer_or_player()
            if (self.field.space[self.player_row_number][self.player_column_number] == "."):
                self.field.space[self.player_row_number][self.player_column_number] = "O" if self._game_move % 2 == 1 else "X"
            self.print()
            print()
            self._game_move += 1
        self.game_over()

        return self.field

    def game_is_over(self):
        if (self._game_move == 0):
            return False
        if (self.check_row() is True or self.check_column() is True or self.check_first_diagonal() is True or self.check_second_diagonal() is True):
            return True
        return False

    def check_row(self):
        row = self.player_row_number
        for a in range(self.field.number_of_columns - 3):
            if (self.field.space[row][a] == self.field.space[row][a + 1] == self.field.space[row][a + 2] == self.field.space[row][a + 3] != "."):
                return True
        return False

    def check_column(self):
        column = self.player_column_number
        for a in range(self.field.number_of_rows - 3):
            if (self.field.space[a][column] == self.field.space[a+1][column] == self.field.space[a+2][column] == self.field.space[a+3][column] != "."):
                return True
        return False

    def check_first_diagonal(self):
        row = self.player_row_number
        column = self.player_column_number
        while (row != 0 and column != 0):
            row -= 1
            column -= 1
        while (row < self.field.number_of_rows - 3 and column < self.field.number_of_columns - 3):            
            if (self.field.space[row][column] == self.field.space[row + 1][column + 1] == self.field.space[row + 2][column + 2] == self.field.space[row + 3][column + 3] != "."):
                return True
            row += 1
            column += 1
        return False

    def check_second_diagonal(self):
        row = self.player_row_number
        column = self.player_column_number
        while (row != self.field.number_of_rows - 1 and column != 0):
            row += 1
            column -= 1
        while (row > self.field.number_of_rows - 5 and column < self.field.number_of_columns - 3):
            if (self.field.space[row][column] == self.field.space[row - 1][column + 1] == self.field.space[row - 2][column + 2] == self.field.space[row - 3][column + 3] != "."):
                return True
            row -= 1
            column += 1
        return False

    def input_row(self):
        name = self.players.second if self._game_move % 2 == 1 else self.players.first
        print(f'{name}: сейчас твоя очередь(строка)')
        return input()

    def input_column(self):
        name = self.players.second if self._game_move % 2 == 1 else self.players.first
        print(f'{name}: сейчас твоя очередь(столбец)')
        return input()

    def game_over(self):
        name = self.players.first if self._game_move % 2 == 1 else self.players.second
        print(f'GAME OVER, {name} won')

    def print(self):
        for row in self.field.space:
            for element in row:
                print(element, end=' ')
            print()
