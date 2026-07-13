from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Label, Button
from textual.containers import Vertical


class AddMaterialDialog(ModalScreen):

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Add Material")
            yield Button("Close", id="close")
            
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "close":
            self.dismiss()

