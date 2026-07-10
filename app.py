from textual.app import App, ComposeResult
from widgets.sidebar import Sidebar
from messages import NavigationRequested

class InventoryApp(App):
    CSS_PATH = "style.tcss"
    TITLE = "Inventory Management Made Easy"

    def compose(self) -> ComposeResult:
        yield Sidebar()

    def on_navigation_requested(self, message : NavigationRequested) -> None:
        self.notify(message.page)
        
    