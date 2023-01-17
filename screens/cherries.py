from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Cherries(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/cherries.kv")
        super().__init__(**kw)
