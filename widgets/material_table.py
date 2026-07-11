from textual.widgets import DataTable
from models.material import Material

class MaterialTable(DataTable):

    def on_mount(self) -> None:
        self.add_columns(
            "Id",
            "Description",
            "Unit",
            "Rate",
            "Quantity"
        )
    def load_materials (self, materials: list[Material]) -> None:
        self.clear()
        for material in materials:
            self.add_row(
                str(material.id), 
                str(material.name), 
                str(material.unit),
                str(material.rate),
                str(material.quantity)
                )
