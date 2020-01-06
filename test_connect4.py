from Connect4 import Field, Players, Game


def test_second_space_filling():
    field1 = Field(4, 4)
    field1.space[1][1] = "X"
    # field1.space[1][2] = "X"
    suma = 0
    players = Players("Sasha", "Ola")
    game1 = Game(players, field1)
    game1.second_space_filling()
    print(field1.second_space)
    for row in field1.second_space:
        for element in row:
            if element == "X":
                suma += 1
    assert suma == 8
