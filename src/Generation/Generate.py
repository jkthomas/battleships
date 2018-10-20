import random
from Utilities import Fieldtype
from Utilities import Direction


class Generate(object):
    board_length = 10
    board = []
    ships = []

    def __init__(self):
        # self.board = board
        self.board = [[1 for x in range(self.board_length)] for y in range(self.board_length)]
        self.ships_length = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    def generate_all_ships_positions(self):
        for ship_length in self.ships_length:
            self.generate_single_ship_position(ship_length)

        return self.board

    def generate_single_ship_position(self, ship_length):
        board_indices = []
        for i in range(self.board_length - ship_length + 1):
            board_indices.append(i)

        while True:
            generation_direction = random.choice([Direction.Direction.Vertical.value,
                                                  Direction.Direction.Horizontal.value])
            # We generate first ship point with margin at right/bottom edge so we will always fit the rest of it
            if generation_direction == Direction.Direction.Vertical.value:
                row_position = random.choice(board_indices)
                column_position = random.choice(board_indices)
            elif generation_direction == Direction.Direction.Vertical.value:
                row_position = random.choice(board_indices)
                column_position = random.choice(board_indices)
            else:
                row_position = random.choice(board_indices)
                column_position = random.choice(board_indices)

            if self.append_ship_space_on_board(row_position, column_position, generation_direction, ship_length):
                return
            else:
                continue

    def append_ship_space_on_board(self, row_position, column_position, generation_direction, ship_length):
        if self.check_ship_space(row_position, column_position, generation_direction, ship_length):
            self.generate_ship_on_board(row_position, column_position, generation_direction, ship_length)
            return True
        else:
            # throw
            return False

    def check_ship_space(self, row_position, column_position, generation_direction, ship_length):
        if generation_direction == Direction.Direction.Vertical.value:
            for row_offset in range(ship_length):
                if self.board[row_position + row_offset][column_position] != Fieldtype.Fieldtype.Water.value:
                    return False

            return True
        elif generation_direction == Direction.Direction.Horizontal.value:
            for column_offset in range(ship_length):
                if self.board[row_position][column_position + column_offset] != Fieldtype.Fieldtype.Water.value:
                    return False

            return True
        else:
            # throw
            return False

    def generate_ship_on_board(self, row_position, column_position, generation_direction, ship_length):
        ship_row_positions = []
        ship_column_positions = []

        if generation_direction == Direction.Direction.Vertical.value:
            for row_offset in range(ship_length):
                self.board[row_position + row_offset][column_position] = Fieldtype.Fieldtype.Ship.value
                ship_row_positions.append(row_position + row_offset)

            ship_column_positions.append(column_position)
            self.generate_occupied_fields_on_board(ship_row_positions, ship_column_positions)
        elif generation_direction == Direction.Direction.Horizontal.value:
            for column_offset in range(ship_length):
                self.board[row_position][column_position + column_offset] = Fieldtype.Fieldtype.Ship.value
                ship_column_positions.append(column_position + column_offset)

            ship_row_positions.append(row_position)
            self.generate_occupied_fields_on_board(ship_row_positions, ship_column_positions)
        else:
            # throw
            return False

    def generate_occupied_fields_on_board(self, ship_row_positions, ship_column_positions):
        # No corners
        # Top/bottom line
        if ship_row_positions[0] != 0:
            for column_position in ship_column_positions:
                self.board[ship_row_positions[0] - 1][column_position] = Fieldtype.Fieldtype.Occupied.value
        if ship_row_positions[len(ship_row_positions) - 1] != 9:
            for column_position in ship_column_positions:
                self.board[ship_row_positions[len(ship_row_positions) - 1] + 1][
                    column_position] = Fieldtype.Fieldtype.Occupied.value

        # Left/right line
        if ship_column_positions[0] != 0:
            for row_position in ship_row_positions:
                self.board[row_position][ship_column_positions[0] - 1] = Fieldtype.Fieldtype.Occupied.value
        if ship_column_positions[len(ship_column_positions) - 1] != 9:
            for row_position in ship_row_positions:
                self.board[row_position][
                    ship_column_positions[len(ship_column_positions) - 1] + 1] = Fieldtype.Fieldtype.Occupied.value

        # TODO: Add corners checking
