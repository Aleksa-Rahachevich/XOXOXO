import random


class Field:
    """
        Stworzenie  planszy z liczbą wierszów i kolumn podaną przez użytkownika
    """
    def __init__(self, number_of_rows, number_of_columns):
        self.number_of_columns = number_of_columns
        self.number_of_rows = number_of_rows
        self.space = []
        self.second_space = []
        for i in range(number_of_rows):
            self.space.append(["."] * number_of_columns)
            self.second_space.append(["."] * self.number_of_columns)


class Players:
    """
        Stworzenie graczy z imionami podanymi przez użytkowników
    """
    def __init__(self, first, second=None):
        self.first = first
        self.second = second
    
    def first_player(self):
        print(f'Enter the name of the first player:')
        self.first = input()
        return self.first

    def second_player(self):
        print(f'enter the name of the second player or type "Computer":')
        self.second = input()
        return self.second


class Game:
    def __init__(self, players, field, game_move=0):
        self.players = players
        self.field = field
        self._game_move = game_move
        self.player_row_number = -1
        self.player_column_number = -1
    
    def get_game_move(self):
        return self._game_move

    def set_game_move(self, value):
        self._game_move = value
        return self._game_move

    def computer_or_player(self):
        if (self.players.second is None or self.players.second == "Computer"):
            if self._game_move % 2 == 1:
                print("Computer move")
                self.computer_actions()
            else:
                self.players_actions()
        else:
            self.players_actions()

    def computer_actions(self):
        self.players.second = "Computer"
        self.coordinate_selection(self.coordinate_list())

    def players_actions(self):
        self.player_column_number = int(self.input_column()) - 1
        return self.player_column_number

    def moves(self):
        self.print()
        while not self.game_is_over():
            self.computer_or_player()
            self.player_row_number = self.field.number_of_rows - 1
            while (self.field.space[self.player_row_number][self.player_column_number] != "." and self.player_row_number != 0):
                self.player_row_number -= 1
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
        row = self.player_row_number  # выдает ошибку при
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

    def input_column(self):
        name = self.players.second if self._game_move % 2 == 1 else self.players.first
        print(f'{name}, your turn')
        return input()

    def game_over(self):
        name = self.players.first if self._game_move % 2 == 1 else self.players.second
        print(f'GAME OVER, {name} won')

    def second_space_filling(self):
        i = 0
        j = 0
        while (i < self.field.number_of_rows):
            while (j < self.field.number_of_columns):
                if (self.field.space[i][j] == "."):
                    if self.check_value(i, j):
                        self.field.second_space[i][j] = "X"
                else:
                    self.field.second_space[i][j] = "."
                j += 1
            j = 0
            i += 1
        return self.field.second_space

    def check_value(self, row, column):
        for i in range(
            max(row - 1, 0),
            min(
                min(row + 1, self.field.number_of_rows) + 1,
                self.field.number_of_rows
                )
        ):
            for j in range(max(column - 1, 0), min(min(column + 1, self.field.number_of_columns) + 1, self.field.number_of_columns)):
                if (i != row or j != column):
                    if (self.field.space[i][j] != "."):
                        return True
        return False

    def coordinate_list(self):
        coordinates = []
        row = 0
        column = 0
        self.second_space_filling()
        while row < self.field.number_of_rows:
            while column < self.field.number_of_columns:
                if self.field.second_space[row][column] == "X":
                    coordinates.append(str(row) + "," + str(column))
                column += 1
            column = 0
            row += 1
        return coordinates

    def coordinate_selection(self, coordinates):
        coordinate = random.choice(coordinates).split(',')
        self.player_row_number = int(coordinate[0])
        self.player_column_number = int(coordinate[1])
        return self.player_column_number, self.player_row_number

    def print(self):
        for i in range(self.field.number_of_columns):
            print(i + 1, end=' ')
        print()
        print(f"-" * self.field.number_of_columns * 2)
        for row in self.field.space:
            for element in row:
                print(element, end=' ')
            print()
    
#    def load_scores_from_file(self):
#        with open("High_scores.txt", newline="") as file:
#            self.people = PeopleCsvReader(file).read()

#    def save_scores_to_file(self):
#        with open(path, "w", newline="") as file:
#            PeopleCsvWriter(file).write(self.people)
