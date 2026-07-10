from textual.app import App, ComposeResult
from widgets.sidebar import Sidebar

class InventoryApp(App):
    CSS_PATH = "style.tcss"
    TITLE = "Inventory Management Made Easy"

    def compose(self) -> ComposeResult:
        yield Sidebar()