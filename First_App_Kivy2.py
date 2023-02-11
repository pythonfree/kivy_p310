from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        self.title = "App on Kivy"
        self.icon = "vlc_video_movie_audio_play_player_icon_233873.ico"
        label = Label(text="Hello from Kivy!")
        return label


if __name__ == '__main__':
    app = MainApp()
    app.run()
