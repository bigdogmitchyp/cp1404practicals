"""
CP1404 Prac
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

name_list = ["alpha", "beta", "charlie", "delta", "echo"]


class DynamicLabelsApp(App):
    """Class for dynamic label app"""
    def build(self):
        """Build kv GUI frame"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Creates widgets for each name in name list"""
        for name in name_list:
            temp_label = Label(text=name, font_size=48, color=(1, 1, 1, 1))
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
