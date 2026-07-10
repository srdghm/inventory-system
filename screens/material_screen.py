from textual.widget import Widget
from textual.widgets import Label


class MaterialScreen(Widget):

    def compose(self):
        yield Label("Materials")