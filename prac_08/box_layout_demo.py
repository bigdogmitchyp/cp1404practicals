from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Class for box layouts kv GUI"""
    def build(self):
        """Builds kv GUI frame"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Prints on greeting on a label"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clears the labels """
        self.root.ids.output_label.text = " "
        self.root.ids.input_name.text = " "


BoxLayoutDemo().run()
