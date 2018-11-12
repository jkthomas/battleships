from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from Generation.Generate import Generate
from kivy import utils


class BoardLayout(GridLayout):

    def __init__(self, turn_dispatcher, is_computer):
        super(BoardLayout, self).__init__()
        self.turn_dispatcher = turn_dispatcher
        self.is_computer = is_computer
        self.board_turn = True
        self.ship_fields_hit = 0
        self.generate_initial_board()

    def generate_initial_board(self):
        generator = Generate()
        fields = generator.generate_all_ships_positions()
        field_id = 1
        for field_row in fields:
            for field in field_row:
                background_color = utils.get_color_from_hex('#66e0ff')  # water
                if field == 2:
                    background_color = utils.get_color_from_hex('#a6a6a6')  # ship
                # if field == FieldType.Occupied:
                #     background_color = utils.get_color_from_hex('#ffff00')  # occupied

                field_button = Button(
                    id=str(field_id),
                    text=str(field),
                    background_color=background_color)

                if not self.is_computer:
                    field_button.bind(on_release=self.player_hit_field)
                self.add_widget(field_button)
                field_id += 1

    def give_turn(self):
        self.board_turn = True
        if self.is_computer:
            self.computer_hit_field()

    def player_hit_field(self, button_instance):
        if self.board_turn:
            if button_instance.text == '2':
                button_instance.background_color = utils.get_color_from_hex('#66ff33')
                self.ship_fields_hit += 1
                if self.ship_fields_hit == 20:
                    self.add_widget(Label(text="PRZEGRANA", text_size=(200, None), halign='right'))
                    for element in self.children:
                        element.disabled = True
            else:
                button_instance.disabled = True
                button_instance.background_color = utils.get_color_from_hex('#ff0000')
                self.board_turn = False

                if self.turn_dispatcher.x == 'player':
                    self.turn_dispatcher.x = 'computer'
                #else:
                #    self.turn_dispatcher.x = 'player'

    def computer_hit_field(self):
        while True:
            button_index = 0
            self.ids.button_index.disabled = True
            if self.ids.button_index.text == '2':
                self.ids.button_index.background_color = utils.get_color_from_hex('#66ff33')
                self.ship_fields_hit += 1
                if self.ship_fields_hit == 20:
                    self.add_widget(Label(text="PRZEGRANA", text_size=(200, None), halign='right'))
                    for element in self.children:
                        element.disabled = True
                    break
            else:
                self.ids.button_index.disabled = True
                self.ids.button_index.background_color = utils.get_color_from_hex('#ff0000')
                self.board_turn = False

                if self.turn_dispatcher.x == 'computer':
                    self.turn_dispatcher.x = 'player'
                break
