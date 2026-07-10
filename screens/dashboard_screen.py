from textual.widget import Widget
from textual.widgets import Label


class DashboardScreen(Widget):

    def compose(self):
        yield Label("Dashboard")