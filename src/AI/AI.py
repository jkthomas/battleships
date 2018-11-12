import random
from Utilities import Fieldtype
from AI import AIState
from Generation.Generate import Generate


class AI(object):

    def __init__(self):
        super(AI, self).__init__()
        generator = Generate()
        self.fields = generator.generate_all_ships_positions()

        self.board_length = 10
        self.board = []

        self.state = AIState.AIState.Searching

        self.four_masted_ships = 1
        self.three_masted_ships = 2
        self.two_masted_ships = 3
        self.one_masted_ships = 4

        self.temp_x = 0
        self.temp_y = 0

    def generate_empty_board(self):
        self.board = [[1 for x in range(self.board_length)] for y in range(self.board_length)]

    def make_move(self): # returns the x,y position which is chosen by the Algorithm
        #AI is searching for a ship on the board
        if self.state == AIState.AIState.Searching:

            while True:
                x = random.randint(0,9)
                y = random.randint(0,9)
                print(str(x)+" "+str(y)+" "+str(self.fields[x][y]) + " "+ str(x+10*y))


                if self.fields[x][y] != Fieldtype.Fieldtype.Hit.value:
                    self.state = AIState.AIState.Hit
                    return
                else:
                    continue

            return x+10*y

        elif self.state == AIState.AIState.Hit:
            # if hit, check if it was a one_masted_ship or not
            print("nie")


