from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from Utilities.TurnDispatcher import TurnDispatcher
from View.Layouts.BoardLayout import BoardLayout
from View.Layouts.BreakLayout import BreakLayout


class GameLayout(BoxLayout):
    player_board = ObjectProperty()
    computer_board = ObjectProperty()
    break_layout = ObjectProperty()

    def __init__(self):
        super(GameLayout, self).__init__()
        self.turn_dispatcher = TurnDispatcher()
        self.turn_dispatcher.bind(x=self.change_current_player)
        self.player_board = BoardLayout(self.turn_dispatcher)
        self.computer_board = BoardLayout(self.turn_dispatcher)
        self.break_layout = BreakLayout()
        self.add_widget(self.player_board)
        self.add_widget(self.break_layout)
        self.add_widget(self.computer_board)

    def change_current_player(self, instance, value):
        if self.turn_dispatcher.x == 'player':
            self.player_board.give_turn()
        if self.turn_dispatcher.x == 'computer':
            self.computer_board.give_turn()
