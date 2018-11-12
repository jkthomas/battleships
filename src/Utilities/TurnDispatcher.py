from kivy.event import EventDispatcher
from kivy.properties import StringProperty


class TurnDispatcher(EventDispatcher):
    x = StringProperty('player')
