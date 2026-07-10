from textual.widgets import DataTable


class MaterialTable(DataTable):

    def on_mount(self) -> None:
        self.add_columns(
            "Description",
            "Unit",
            "Rate",
            "Quantity"
        )
