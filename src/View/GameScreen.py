from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from View.Layouts import GameLayout


class GameScreen(Screen):
    game_layout = ObjectProperty()

    def __init__(self):
        Screen.__init__(self)
        self.game_layout = GameLayout.GameLayout()
        self.add_widget(self.game_layout)
