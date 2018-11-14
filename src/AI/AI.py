import random
from Utilities import Fieldtype
from AI import AIState
from AI import DirectionList
from Utilities import Direction
from Generation.Generate import Generate
import numpy as np


class AI(object):

    def __init__(self, fields):
        super(AI, self).__init__()
        self.fields = fields

        self.board_length = 10
        self.board = []

        self.state = AIState.AIState.Searching

        self.four_masted_ships = 1
        self.three_masted_ships = 2
        self.two_masted_ships = 3
        self.one_masted_ships = 4
        self.ship_length = 1 #length of the hit ship
        self.dirs = DirectionList.DirectionList.Top

        self.row_position = 0
        self.column_position = 0

        #selected point after hit
        self.temp_row_position = 0
        self.temp_column_position = 0
        self.index = 1

        self.direction = Direction.Direction.Undefined
        self.moves = []

    def make_proper_move(self):
        while True:
            m = self.make_move()
            if m not in self.moves and m is not None:
                self.moves.append(m)
                return m
            #else:
            #    break


    def generate_empty_board(self):
        self.board = [[1 for x in range(self.board_length)] for y in range(self.board_length)]

    def select_random_field(self):
        while True:
            self.row_position = random.randint(0, 9)
            self.column_position = random.randint(0, 9)
            #print(str(self.row_position) + " " + str(self.column_position) + " " + str(
            #    self.fields[self.row_position][self.column_position]) + " " + str(self.row_position + 10 * self.column_position))

            if self.board[self.row_position][self.column_position] != Fieldtype.Fieldtype.Hit.value and self.board[self.row_position][
                self.column_position] != Fieldtype.Fieldtype.Miss.value:
                break

            else:
                continue

    def make_move(self):  # returns the x,y position which is chosen by the Algorithm
        # AI is searching for a ship on the board

        if self.state == AIState.AIState.Searching:
            self.select_random_field()
            if self.fields[self.row_position][self.column_position] == Fieldtype.Fieldtype.Ship.value:
                # changing state - found a ship
                self.state = AIState.AIState.Hit
                # saving coords of that ship
                # self.temp_column_position = self.column_position
                # self.temp_row_position = self.row_position

                self.board[self.row_position][self.column_position] = Fieldtype.Fieldtype.Hit.value
            else:
                self.board[self.row_position][self.column_position] = Fieldtype.Fieldtype.Miss.value
            return 10 * self.row_position + self.column_position

        elif self.state == AIState.AIState.Hit:  # if hit, check if it was a one_masted_ship or not
            #if self.two_masted_ships > 0 or self.three_masted_ships > 0 or self.four_masted_ships > 0: #if there are longer ships than 1, search for that ships

                #top
                if self.dirs == DirectionList.DirectionList.Top and self.row_position > 0: # and self.board[self.row_position - self.index][self.column_position]!=Fieldtype.Fieldtype.Miss:
                    self.temp_row_position = self.row_position - self.index
                    if self.temp_row_position >= 0 and self.board[self.row_position - self.index][self.column_position]!=Fieldtype.Fieldtype.Miss:
                        if self.fields[self.temp_row_position][self.column_position] == Fieldtype.Fieldtype.Ship.value:
                            self.board[self.temp_row_position][self.column_position] = Fieldtype.Fieldtype.Hit.value
                            self.ship_length += 1
                            self.index += 1
                            self.direction=Direction.Direction.Vertical
                            return 10 * self.temp_row_position + self.column_position
                        else:
                            self.board[self.temp_row_position][self.column_position] = Fieldtype.Fieldtype.Miss.value
                            self.dirs = DirectionList.DirectionList.Bottom
                            self.index = 1
                            return 10 * self.temp_row_position + self.column_position
                    else:
                        self.dirs = DirectionList.DirectionList.Bottom
                        self.make_move()
                elif self.dirs == DirectionList.DirectionList.Top:
                    self.dirs = DirectionList.DirectionList.Bottom

                #bottom
                if self.dirs == DirectionList.DirectionList.Bottom and self.row_position < self.board_length-1: #and self.board[self.row_position + self.index][self.column_position]!=Fieldtype.Fieldtype.Miss:
                    self.temp_row_position = self.row_position + self.index
                    if self.temp_row_position < self.board_length and self.board[self.row_position + self.index][self.column_position]!=Fieldtype.Fieldtype.Miss:
                        if self.fields[self.temp_row_position][self.column_position] == Fieldtype.Fieldtype.Ship.value:
                            self.board[self.temp_row_position][self.column_position] = Fieldtype.Fieldtype.Hit.value
                            self.ship_length += 1
                            self.index += 1
                            self.direction=Direction.Direction.Vertical
                            return 10 * self.temp_row_position + self.column_position
                        else:
                            self.board[self.temp_row_position][self.column_position] = Fieldtype.Fieldtype.Miss.value
                            self.dirs = DirectionList.DirectionList.Left
                            self.index = 1
                            return 10 * self.temp_row_position + self.column_position
                    else:
                        self.dirs=DirectionList.DirectionList.Left
                        self.make_move()
                elif self.dirs == DirectionList.DirectionList.Bottom:
                    self.dirs = DirectionList.DirectionList.Left

                #left
                if self.dirs == DirectionList.DirectionList.Left and self.column_position > 0 and self.direction != Direction.Direction.Vertical: # and self.board[self.row_position][self.column_position - self.index]!=Fieldtype.Fieldtype.Miss:
                    self.temp_column_position = self.column_position - self.index
                    if self.temp_column_position >= 0 and self.board[self.row_position][self.column_position - self.index]!=Fieldtype.Fieldtype.Miss:
                        if self.fields[self.row_position][self.temp_column_position] == Fieldtype.Fieldtype.Ship.value:
                            self.board[self.row_position][self.temp_column_position] = Fieldtype.Fieldtype.Hit.value
                            self.ship_length += 1
                            self.index += 1
                            self.direction=Direction.Direction.Horizontal
                            return 10 * self.row_position + self.temp_column_position
                        else:
                            self.board[self.row_position][self.temp_column_position] = Fieldtype.Fieldtype.Miss.value
                            self.dirs = DirectionList.DirectionList.Right
                            self.index = 1
                            return 10 * self.row_position + self.temp_column_position
                    else:
                        self.dirs = DirectionList.DirectionList.Right
                        self.make_move()
                elif self.dirs == DirectionList.DirectionList.Left:
                    self.dirs = DirectionList.DirectionList.Right

                #right
                if self.dirs == DirectionList.DirectionList.Right and self.column_position < self.board_length - 1 and self.direction != Direction.Direction.Vertical: # and self.board[self.row_position][self.column_position + self.index] != Fieldtype.Fieldtype.Miss:
                    self.temp_column_position = self.column_position + self.index
                    if self.temp_column_position < self.board_length:  #and self.board[self.row_position][self.column_position + self.index] != Fieldtype.Fieldtype.Miss:
                        if self.fields[self.row_position][self.temp_column_position] == Fieldtype.Fieldtype.Ship.value:
                            self.board[self.row_position][self.temp_column_position] = Fieldtype.Fieldtype.Hit.value
                            self.ship_length += 1
                            self.index += 1
                            self.direction=Direction.Direction.Horizontal
                            return 10 * self.row_position + self.temp_column_position
                        else:
                            self.board[self.row_position][self.temp_column_position] = Fieldtype.Fieldtype.Miss.value
                            self.dirs = DirectionList.DirectionList.Empty
                            self.index = 1
                            return 10 * self.row_position + self.temp_column_position
                    else:
                        self.dirs = DirectionList.DirectionList.Top
                        self.state = AIState.AIState.Searching
                        self.index = 1
                        self.make_move()
                elif self.dirs == DirectionList.DirectionList.Right:
                    self.dirs = DirectionList.DirectionList.Empty
                    self.make_move()

                else:

                    if self.ship_length == 4:
                        self.four_masted_ships-=1
                    elif self.ship_length == 3:
                        self.three_masted_ships-=1
                    elif self.ship_length == 2:
                        self.two_masted_ships-=1
                    elif self.ship_length == 1:
                        self.one_masted_ships-=1

                    self.generate_occupied_tiles(self.row_position, self.column_position)
                    #print("Statek mial dlugosc: %d, zostalo %d x4, %d x3, %d x2, %d x1" % (self.ship_length, self.four_masted_ships, self.three_masted_ships, self.two_masted_ships, self.one_masted_ships))
                    #self.generate_occupied_tiles(self.direction)
                    self.direction = Direction.Direction.Undefined
                    self.ship_length = 1
                    self.dirs = DirectionList.DirectionList.Top
                    self.state = AIState.AIState.Searching
                    self.select_random_field()
                    if self.fields[self.row_position][self.column_position] == Fieldtype.Fieldtype.Ship.value:
                        # changing state - found a ship
                        self.state = AIState.AIState.Hit
                        # saving coords of that ship
                        # self.temp_column_position = self.column_position
                        # self.temp_row_position = self.row_position

                        self.board[self.row_position][self.column_position] = Fieldtype.Fieldtype.Hit.value
                    else:
                        self.board[self.row_position][self.column_position] = Fieldtype.Fieldtype.Miss.value
                    return 10 * self.row_position + self.column_position
                    #self.make_move()

            # else: #there are only one_masted_ships left
            #     self.state = AIState.AIState.Searching
            #     self.select_random_field()
            #     if self.fields[self.row_position][self.column_position] == Fieldtype.Fieldtype.Ship.value:
            #         # changing state - found a ship
            #         self.state = AIState.AIState.Hit
            #         # saving coords of that ship
            #         # self.temp_column_position = self.column_position
            #         # self.temp_row_position = self.row_position
            #
            #         self.board[self.row_position][self.column_position] = Fieldtype.Fieldtype.Hit.value
            #     else:
            #         self.board[self.row_position][self.column_position] = Fieldtype.Fieldtype.Miss.value
            #     return 10 * self.row_position + self.column_position

    def print_tab(self):
        print("-----------")
        print(np.matrix(self.board))
        print("\n")
        print(np.matrix(self.fields))
        print("Zostalo %d x4, %d x3, %d x2, %d x1" % (
        self.four_masted_ships, self.three_masted_ships, self.two_masted_ships,
        self.one_masted_ships))
        print("\n\n")

    def generate_occupied_tiles(self, y, x):
        if self.direction == Direction.Direction.Vertical:
            while y-1>=0 and y-1 != Fieldtype.Fieldtype.Miss.value:
                y-=1
            while y+1 < self.board_length and self.board[y+1][x]!=Fieldtype.Fieldtype.Miss.value:
                temporary=[y-1, y, y+1, y+2]
                for tempy in temporary:
                    for tempx in range(x - 1, x + 2):
                        if 0 <= tempy < self.board_length:
                            if 0 <= tempx < self.board_length:
                                if self.board[tempy][tempx] != Fieldtype.Fieldtype.Hit.value:
                                   self.board[tempy][tempx] = Fieldtype.Fieldtype.Miss.value
                y+=1

        elif self.direction == Direction.Direction.Horizontal:
            while x-1 >= 0 and self.board[y][x-1] == Fieldtype.Fieldtype.Hit.value:
                x = x-1
            while x+1 < self.board_length and self.board[y][x+1] != Fieldtype.Fieldtype.Miss.value:
                for tempy in range(y - 1, y + 2):
                    for tempx in range(x - 1, x + 3):
                        if 0 <= tempy < self.board_length:
                            if 0 <= tempx < self.board_length:
                                if self.board[tempy][tempx] != Fieldtype.Fieldtype.Hit.value:
                                    self.board[tempy][tempx] = Fieldtype.Fieldtype.Miss.value
                x+=1

        else:
            #self.print_tab()
            for tempy in range(y-1, y+2):
                for tempx in range(x-1, x+2):
                    if 0 <= tempy < self.board_length:
                        if 0 <= tempx < self.board_length:
                            if self.board[tempy][tempx] != Fieldtype.Fieldtype.Hit.value:
                                self.board[tempy][tempx] = Fieldtype.Fieldtype.Miss.value
            #self.print_tab()

    def ships_left(self):
        if self.one_masted_ships == 0 and self.two_masted_ships == 0 and self.three_masted_ships == 0 and self.four_masted_ships == 0:
            return False
        else:
            return True

    def can_make_proper_move(self):
        moves = 0
        for y in range(0, self.board_length-1):
            for x in range(0, self.board_length-1):
                if self.board[y][x] == Fieldtype.Fieldtype.Water.value:
                    moves += 1
        if moves == 0:
            return False
        else:
            return True
