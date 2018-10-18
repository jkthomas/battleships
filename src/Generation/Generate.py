import random
from Utilities import Fieldtype
from Utilities import Direction


class Generate:
    board = []
    ships = []

    def __init__(self, board):
        # self.board = board
        self.board = [[0 for x in range(5)] for y in range(5)]
        self.ships_length = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    def generate_positions(self):
        for ship_length in self.ships_length:
            self.generate_ship_position(ship_length)

    def generate_ship_position(self, ship_length):
        # board is square
        position_x = random.choice(self.board.__len__())
        position_y = random.choice(self.board.__len__())
        generation_direction = random.choice([1, 2, 3, 4])
        self.check_if_enough_space(position_x, position_y, generation_direction, ship_length)


    def check_if_enough_space(self, position_x, position_y, generation_direction, ship_length):
        self.check_field_space(position_x, position_y)
        if self.board[position_x][position_y] == Fieldtype.Fieldtype.Water:
            if generation_direction == Direction.Direction.Down:


    def check_field_space(self, position_x, position_y):
        if self.board[position_x][position_y] == Fieldtype.Fieldtype.Water:
            return True
        else:
            return False