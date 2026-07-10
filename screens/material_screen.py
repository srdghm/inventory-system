from textual.widget import Widget
from textual.widgets import Label, Button
from widgets.material_table import MaterialTable
from textual.app import ComposeResult

class MaterialScreen(Widget):

    def compose(self) -> ComposeResult:
        yield Label("Materials")
        yield Button(label="Add Material",id="add_material")
        yield MaterialTable()