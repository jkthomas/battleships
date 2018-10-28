from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from Generation.Generate import Generate
from kivy import utils


class BoardLayout(GridLayout):

    def __init__(self):
        super(BoardLayout, self).__init__()
        self.generate_initial_board()

    def generate_initial_board(self):
        generator = Generate()
        fields = generator.generate_all_ships_positions()
        for field_row in fields:
            for field in field_row:
                background_color = utils.get_color_from_hex('#66e0ff')  # water
                if field == 2:
                    background_color = utils.get_color_from_hex('#a6a6a6')  # ship
                # if field == 3:
                #     background_color = utils.get_color_from_hex('#ffff00')  # occupied

                self.add_widget(Button(
                    id=str(1),
                    text=str(field),
                    background_color=background_color
                ))
