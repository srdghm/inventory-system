from textual.containers import Vertical
from textual.app import ComposeResult
from textual.widgets import Button, Label


class Sidebar(Vertical):
    MENU_ITEMS = [
        {"id": "dashboard", "label": "Dashboard"},
        {"id": "materials", "label": "Materials"},
        {"id": "purchases", "label": "Purchases"},
        {"id": "estimates", "label": "Estimates"},
        {"id": "reports", "label": "Reports"},
        {"id": "settings", "label": "Settings"},
    ]
    def compose(self) -> ComposeResult:

        yield Label("Inventory Management", id="sidebar-title")
        for item in self.MENU_ITEMS:
            yield Button(item["label"], id=item["id"], classes="nav-button")