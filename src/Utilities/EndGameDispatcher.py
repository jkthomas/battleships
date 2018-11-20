from kivy.event import EventDispatcher
from kivy.properties import StringProperty


class EndGameDispatcher(EventDispatcher):
    x = StringProperty('OK')
