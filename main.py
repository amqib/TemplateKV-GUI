from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager


from screens.screens import *

class WindowManager(ScreenManager):
    pass

class Qibtemplate(MDApp):
    CLASSES = {
        'Wescreen':'screens.wescreen',
        'Cardtwo':'screens.cardtwo',
        'Menucard':'screens.menucard',
        'Cherries':'screens.cherries',
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]
    KV_FILES = [
        'kv/wescreen.kv',
        'kv/cardtwo.kv',
        'kv/menucard.kv',        
        'kv/cherries.kv',
    ]
    def build(self):
        self.wm = WindowManager()
        screens = [
            Cardtwo(name="cardtwo"),
            Wescreen(name="wescreen"),
            Menucard(name="menucard"),
            Cherries(name="cherries"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == '__main__':
    Qibtemplate().run()