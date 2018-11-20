from kivy.app import App
from kivy.lang import Builder
from View import GameScreen

Builder.load_file('Battleships.kv')


class BattleshipsApp(App):

    def build(self):
        return GameScreen.GameScreen()


if __name__ == '__main__':
    BattleshipsApp().run()
