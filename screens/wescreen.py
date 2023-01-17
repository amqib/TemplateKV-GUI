from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.core.text import LabelBase

class Wescreen(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/wescreen.kv")
        super().__init__(**kw)

    def current_slide(self, index):
        for i in range(3):
            if index == i:
                self.ids[f"slide{index}"].color = 253/255,140/255,95/255,255/255
            else:
                self.ids[f"slide{i}"].color = 233/255,237/255,240/255,255/255

    def next(self):
        self.ids.carousel.load_next(mode="next")


