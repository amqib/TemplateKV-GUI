from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Menucard(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/menucard.kv")
        super().__init__(**kw)
