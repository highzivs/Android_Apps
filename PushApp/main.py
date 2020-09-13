import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.audio import SoundLoader

class MainWindow(Screen):
    pass

class CountScreen(Screen):
    DOWN_COUNT=0
    UP_COUNT=0

    def BUTTON_DOWN(self):
        self.DOWN_COUNT=self.DOWN_COUNT+1
        return self.DOWN_COUNT

    def BUTTON_UP(self):
        self.UP_COUNT=self.UP_COUNT+1
        return self.UP_COUNT

    def PUSH_UP(self):
        if self.BUTTON_UP()==self.BUTTON_DOWN():
            return True

class NiceTryScreen(Screen):
    pass

class FinalWindow(Screen):
    def PlaySound(self):
        sound = SoundLoader.load("beep-07.wav")
        if sound:
            sound.play()

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("push_app.kv") #LOAD Kivy FILE

class PushApp(App):
    PUSH_UP_COUNT=0
    def build(self):
        return kv


if __name__=="__main__":
    PushApp().run()
