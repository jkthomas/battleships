from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from View.Layouts.BoardLayout import BoardLayout
from View.Layouts.BreakLayout import BreakLayout


class GameLayout(BoxLayout):
    player_board = ObjectProperty()
    computer_board = ObjectProperty()
    break_layout = ObjectProperty()

    def __init__(self):
        super(GameLayout, self).__init__()
        self.player_board = BoardLayout()
        self.computer_board = BoardLayout()
        self.break_layout = BreakLayout()

        self.add_widget(self.player_board)
        self.add_widget(self.break_layout)
        self.add_widget(self.computer_board)
