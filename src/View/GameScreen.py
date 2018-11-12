from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from View.Layouts.GameLayout import GameLayout
from kivy.core.window import Window


class GameScreen(Screen):
    player_points = 0
    computer_points = 0
    game_layout = ObjectProperty()

    def __init__(self):
        Screen.__init__(self)
        self.game_layout = GameLayout()
        self.add_widget(self.game_layout)
        Window.size = (1200, 600)
