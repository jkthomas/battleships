from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from AI.AI import AI
from Generation.Generate import Generate
from kivy import utils


showcase_mode = True


class BoardLayout(GridLayout):

    def __init__(self, turn_dispatcher, endgame_dispatcher, is_computer):
        super(BoardLayout, self).__init__()
        self.turn_dispatcher = turn_dispatcher
        self.endgame_dispatcher = endgame_dispatcher
        self.is_computer = is_computer
        self.board_turn = True
        self.ship_fields_hit = 0
        self.computer = None
        self.generate_initial_board()

    def generate_initial_board(self):
        generator = Generate()
        fields = generator.generate_all_ships_positions()
        self.computer = AI(fields)
        field_id = 0
        if showcase_mode:
            textsize = [0, 0]
        else:
            textsize = [0.1, 0.1]
        for field_row in fields:
            for field in field_row:
                background_color = utils.get_color_from_hex('#66e0ff')  # water
                if field == 2:
                    if self.is_computer:
                        background_color = utils.get_color_from_hex('#a6a6a6')  # ship
                    else:
                        if showcase_mode:
                            background_color = utils.get_color_from_hex('#a6a6a6')  # ship

                field_button = Button(
                    id=str(field_id),
                    text=str(field),
                    text_size=textsize,
                    background_color=background_color)

                if not self.is_computer:
                    field_button.bind(on_release=self.player_hit_field)
                self.add_widget(field_button)
                field_id += 1
        if self.is_computer:
            self.add_widget(Label(text="PLANSZA GRACZA", text_size=(300, None), halign='right'))
        else:
            self.add_widget(Label(text="PLANSZA KOMPUTERA", text_size=(300, None), halign='right'))

    def give_turn(self):
        self.board_turn = True
        if self.is_computer:
            self.computer_hit_field()

    def player_hit_field(self, button_instance):
        if self.board_turn:
            if button_instance.text == '2':
                button_instance.background_color = utils.get_color_from_hex('#66ff33')
                button_instance.unbind(on_release=self.player_hit_field)
                self.ship_fields_hit += 1
                if self.ship_fields_hit == 20:
                    self.add_widget(Label(text="PRZEGRANA", text_size=(400, None), halign='right'))
                    self.endgame_dispatcher.x = 'STOP'
            else:
                button_instance.disabled = True
                button_instance.background_color = utils.get_color_from_hex('#ff0000')
                self.board_turn = False

                if self.turn_dispatcher.x == 'player':
                    self.turn_dispatcher.x = 'computer'

    def computer_hit_field(self):
        computer_turn = True
        while computer_turn:
            button_index = self.computer.make_proper_move()
            for button in self.children:
                if button.id == str(button_index):
                    if button.text == '2':
                        button.background_color = utils.get_color_from_hex('#66ff33')
                        self.ship_fields_hit += 1
                        if self.ship_fields_hit == 20:
                            self.add_widget(Label(text="PRZEGRANA", text_size=(400, None), halign='right'))
                            self.endgame_dispatcher.x = 'STOP'
                            break
                    else:
                        button.disabled = True
                        button.background_color = utils.get_color_from_hex('#ff0000')
                        self.board_turn = False
                        computer_turn = False
                    break

        if self.turn_dispatcher.x == 'computer':
            self.turn_dispatcher.x = 'player'
