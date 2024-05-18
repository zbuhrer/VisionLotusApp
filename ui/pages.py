import flet as ft


class EventSchedulePage(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Text("Event Schedule Page Placeholder")
        ]

    def loadpage(self):
        controls = self.controls
        return controls