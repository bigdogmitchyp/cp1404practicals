"""
CP1404 Prac
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ["alpha", "beta", "charlie", "delta", "echo"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_list:
            temp_label = Label(text=name, font_size=48, color=(1, 1, 1, 1))
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
