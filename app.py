from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Horizontal, Vertical

class InventoryApp(App):
    CSS_PATH = "style.tcss"
    TITLE = "Inventory Management Made Easy"

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id = "sidebar"):
                yield Button("Dashboard")
                yield Button("Materials")
                yield Button("Labour")
                yield Button("Reports")
            with Vertical(id= "content"):
                yield Static("Welcome to Inventory Management System")
        yield Footer()
