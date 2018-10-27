from kivy.uix.screenmanager import Screen

import Generation.Generate
import numpy as np
from kivy.app import App
from kivy.lang import Builder
from View import GameScreen

Builder.load_file('Battleships.kv')


class BattleshipsApp(App):

    def build(self):
        return GameScreen.GameScreen()


if __name__ == '__main__':
    BattleshipsApp().run()

# def main():
#     generator = Generation.Generate.Generate()
#     gameboard = generator.generate_all_ships_positions()
#     print(np.matrix(gameboard))
#
#
# if __name__ == "__main__":
#     main()
