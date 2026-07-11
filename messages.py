from widgets.material_table import MaterialTable
from textual.message import Message
from models.material import Material


class NavigationRequested(Message):

    def __init__(self, page : str):
        super().__init__()
        self.page = page
class AddMaterialRequested(Message):
	
	def __init__(self, material: Material):
		super().__init__()
		self.material = material

class MaterialFormCancelRequested(Message):
	def __init__(self):
		super().__init__()
