from textual.containers import Horizontal,Vertical

from messages import AddMaterialRequested
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
                    yield Button(label = "Edit Material", id = "edit_material")
                    yield Button(label="Insert Material", id= "insert_material")

    def on_mount(self):
        repository = MaterialRepository()
        materials = repository.get_all()
        form = self.query_one(MaterialForm)
        form.hide()
        table = self.query_one(MaterialTable)
        table.load_materials(materials)
        table.cursor_type ="row"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        
        if event.button.id == "add_material":
            form = self.query_one(MaterialForm)
            form.show()
            
        elif event.button.id == "delete_material":
            table = self.query_one(MaterialTable)
    
            # 1. Verify a row is actually highlighted
            if table.cursor_row is not None:
                current_row_index = table.cursor_row
                # Grab the whole row as a list, then pick index 0 (the first cell)
                row_data = table.get_row_at(current_row_index)
                cell_value = row_data[0]
                self.notify("cell value:"+str(cell_value))
                # 5. Run your database deletion logic
                repository = MaterialRepository()
                repository.remove_row(cell_value) 
                table.clear() 
                material = repository.get_all()
                table.load_materials(material)
                      
                #self.notify(f"Material Deleted: {selected_row_id}")
             #else:
               # self.notify("Please select a row first!", severity="warning")

         # elif event.button.id == "edit_material":
         #    self.notify("Material Edited")

         # elif event.button.id == "insert_material":
         #    self.notify("Material Inserted")

    def on_add_material_requested(self, message: AddMaterialRequested) -> None:
        repository = MaterialRepository()
        repository.add(message.material)
        materials = repository.get_all()
        form = self.query_one(MaterialForm)
        form.clear()
        table = self.query_one(MaterialTable)
        table.load_materials(materials)
        self.notify("material added")
        
