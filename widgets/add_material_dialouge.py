from textual.app import ComposeResult
from textual.widgets import Label, Input, Button
from textual.containers import Vertical, Horizontal
from models.material import Material
from messages import AddMaterialRequested


class MaterialForm(Vertical):

    def compose(self) -> ComposeResult:
        yield Label("Name")
        yield Input(id="name")

        yield Label("Unit")
        yield Input(id="unit")

        yield Label("Rate")
        yield Input(id="rate")

        yield Label("Quantity")
        yield Input(id="quantity")

        with Horizontal():
            yield Button("Save", id="save")
            yield Button("Cancel", id="cancel")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancel":
            self.clear()
            self.hide()
        if event.button.id == "save":
            
            name = self.query_one("#name", Input).value
            unit = self.query_one("#unit", Input).value
            rate = int(self.query_one("#rate", Input).value)
            quantity = int(self.query_one("#quantity", Input).value)

            mat = Material(None,name,unit, rate, quantity)
            
            self.post_message(AddMaterialRequested(mat))
                        
            self.notify("msg posted")

    def clear(self):
                    self.query_one("#name", Input).value = ""
                    self.query_one("#unit", Input).value = ""
                    self.query_one("#rate", Input).value = ""
                    self.query_one("#quantity", Input).value = ""
    def hide(self):
            self.add_class("hidden")
    def show(self):
            self.remove_class("hidden")
