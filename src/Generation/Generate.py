import random
from Utilities import Fieldtype
from Utilities import Direction


class Generate:
    board = []
    ships = []

    def __init__(self, board):
        # self.board = board
        self.board = [[0 for x in range(10)] for y in range(10)]
        self.ships_length = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    def generate_all_ships_positions(self):
        for ship_length in self.ships_length:
            self.generate_single_ship_position(ship_length)

    def generate_single_ship_position(self, ship_length):
        while True:
            generation_direction = random.choice([Direction.Direction.Vertical.value,
                                                  Direction.Direction.Horizontal.value])
            # We generate first ship point with margin at right/bottom edge so we will always fit the rest of it
            if generation_direction == Direction.Direction.Vertical.value:
                position_x = random.choice(self.board.__len__() - ship_length)
                position_y = random.choice(self.board.__len__())
            elif generation_direction == Direction.Direction.Vertical.value:
                position_x = random.choice(self.board.__len__())
                position_y = random.choice(self.board.__len__() - ship_length)
            else:
                position_x = random.choice(self.board.__len__() - ship_length)
                position_y = random.choice(self.board.__len__() - ship_length)

            if self.append_ship_space_on_board(position_x, position_y, generation_direction, ship_length):
                return
            else:
                continue

    def append_ship_space_on_board(self, position_x, position_y, generation_direction, ship_length):
        if self.check_ship_space(position_x, position_y, generation_direction, ship_length):
            self.generate_ship_on_board(position_x, position_y, generation_direction, ship_length)
            return True
        else:
            # throw
            return False

    def check_ship_space(self, position_x, position_y, generation_direction, ship_length):
        if generation_direction == Direction.Direction.Vertical.value:
            for x_offset in range(ship_length):
                if self.board[position_x + x_offset][position_y] != Fieldtype.Fieldtype.Water.value:
                    return False

            return True
        elif generation_direction == Direction.Direction.Horizontal.value:
            for y_offset in range(ship_length):
                if self.board[position_x][position_y + y_offset] != Fieldtype.Fieldtype.Water.value:
                    return False

            return True
        else:
            # throw
            return False

    def generate_ship_on_board(self, position_x, position_y, generation_direction, ship_length):
        for x_offset in range(ship_length):
            self.board[position_x + x_offset][position_y] = Fieldtype.Fieldtype.Ship.value
        for y_offset in range(ship_length):
            self.board[position_x][position_y + y_offset] = Fieldtype.Fieldtype.Ship.value

