from textual.app import App, ComposeResult
from textual.containers import Horizontal, Container
from widgets.sidebar import Sidebar
from messages import NavigationRequested
from screens.dashboard_screen import DashboardScreen
from screens.material_screen import MaterialScreen


class InventoryApp(App):

    CSS_PATH = "style.tcss"
    TITLE = "Inventory Management Made Easy"

    PAGE_MAP = {
        "dashboard": DashboardScreen,
        "materials": MaterialScreen,
    }

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Sidebar()
            yield Container(id="content")

    def on_mount(self) -> None:
        self.post_message(
            NavigationRequested("dashboard")
        )

    def on_navigation_requested(
        self,
        message: NavigationRequested
    ) -> None:

        content = self.query_one("#content")

        content.remove_children()

        page_class = self.PAGE_MAP[message.page]

        content.mount(page_class())
        
        
    