from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.templates import ScaleWidget
from kivy.animation import Animation
from kivy.metrics import dp


class ScaleCard(MDFloatLayout, HoverBehavior):

    opan_card = True
    desc = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anim_big_image = Animation(
            scale_value_x = 1,
            scale_value_y = 1,
            d = 0.4,
            t = "in_quart",
            pos_hint= {'center_x': 0.9},
        )
        self.anim_big_image.bind(on_complete=self.show_desc_box)
        self.anim_small_image = Animation(
            scale_value_x = 0.7,
            scale_value_y = 0.7,
            d = 0.4,
            t = "in_quart",
            pos_hint= {'center_x': 0.5},
        )
    def show_desc_box(self,*args):
        """
        Called at the end of image animation of opening the card.
        """
        self.desc = DescBox(y=self.y + dp(10))
        self.add_widget(self.desc, index = -1)
        Animation(
            pos_hint= {'center_x': 0.5}, opacity=1, d=0.1
        ).start(self.desc)

    def on_enter(self):
        
        self.opan_card = not self.opan_card

        if not self.opan_card:

            self.anim_big_image.start(self.ids.image)
            Animation(
                size=(dp(320), dp(240)),
                radius=[dp(24),dp(24),dp(24),dp(24)],
                d= 0.2,
                t="in_quart",
            ).start(self)

    def on_leave(self):

        self.opan_card = True
        self.anim_small_image.start(self.ids.image)

        if self.desc:
            self.remove_widget(self.desc)

        Animation(
            size=(dp(200), dp(200)),
            radius=[dp(100),dp(100),dp(100),dp(100)],
            d= 0.3,
            t="in_quart",
        ).start(self)
        

class ScaleImage(Image, ScaleWidget):
    scale_value_x = NumericProperty(0.7)
    scale_value_y = NumericProperty(0.7)

class DescBox(MDBoxLayout):
    pass


class Cardtwo(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/cardtwo.kv")
        super().__init__(**kw)

