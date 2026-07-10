from textual.message import Message


class NavigationRequested(Message):

    def __init__(self, page : str):
        super().__init__()
        self.page = page

