from textual.widget import Widget
from textual.widgets import Label, Button
from widgets.material_table import MaterialTable
from textual.app import ComposeResult
from inventory.repositories.material_repository import MaterialRepository

class MaterialScreen(Widget):

    def compose(self) -> ComposeResult:
        yield Label("Materials")
        yield Button(label="Add Material",id="add_material")
        yield MaterialTable()

    def on_mount(self):
        repository = MaterialRepository()

        materials = repository.get_all()

        table = self.query_one(MaterialTable)

        table.load_materials(materials)