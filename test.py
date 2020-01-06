from Connect4 import Field, Players, Game
field1 = Field(7, 10)
players = Players("Sasha", "Ola")
field2 = Field(4, 4)
field2.space[1][1] = "X"
game1 = Game(players, field2)
game1.second_space_filling()
print(field2.second_space)
# game1.moves()
