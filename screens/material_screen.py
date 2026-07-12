from textual.containers import Horizontal,Vertical

from messages import AddMaterialRequested, MaterialFormCancelRequested
from textual.widget import Widget
from textual.widgets import Label, Button
from widgets.material_table import MaterialTable
from textual.app import ComposeResult
from inventory.repositories.material_repository import MaterialRepository
from widgets.add_material_dialouge import MaterialForm

class MaterialScreen(Widget):

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Materials")
            with Horizontal():
                yield MaterialForm()
                yield MaterialTable()
                with Vertical():
                    yield Button(label="Add Material", id="add_material")
                    yield Button(label="Delete Material", id="delete_material")

    def on_mount(self):
        repository = MaterialRepository()
        materials = repository.get_all()
        form = self.query_one(MaterialForm)
        form.hide()
        table = self.query_one(MaterialTable)
        table.load_materials(materials)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add_material":
            form = self.query_one(MaterialForm)
            form.show()
            table = self.query_one(MaterialTable)
            table.add_class("hidden")

        elif event.button.id == "delete_material":
            self.notify("Material Deleted")

    def on_add_material_requested(self, message: AddMaterialRequested) -> None:
        repository = MaterialRepository()
        repository.add(message.material)
        form = self.query_one(MaterialForm)
        form.clear()
        self.notify("material added")

    def on_material_form_cancel_requested(self, message: MaterialFormCancelRequested):
        form = self.query_one(MaterialForm)
        form.hide()
        table = self.query_one(MaterialTable)
        table.remove_class("hidden")
     
        
