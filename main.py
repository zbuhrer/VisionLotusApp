import flet as ft

class VisionLotus(ft.UserControl):
    def __init__(self):
        
        self.appbar = ft.AppBar(
            leading=ft.PopupMenuButton(icon=ft.icons.HOME_OUTLINED,items=[
                ft.PopupMenuItem(text="Auction Information",on_click=self.show_auction_info),
                ft.PopupMenuItem(text="Class Schedule",on_click=self.show_class_schedules)
                ]),
            title=ft.Text("Vision Lotus", style=ft.TextStyle(color=ft.colors.RED)),
            center_title=False,
            bgcolor=ft.colors.BLACK,
            actions=[
                ft.PopupMenuButton(icon=ft.icons.MENU,items=[
                ft.PopupMenuItem(text="Presenter Application"),
                ft.PopupMenuItem(text="Volunteer Application"),
                ft.PopupMenuItem(text="Sponsorship Application"),
                ft.PopupMenuItem(text="Vendor Application"),])])
            
    def show_auction_info(self, e):
        print("Auction information page opened!")

    def show_class_schedules(self, e):
        print("Class schedules page opened!")

    def show_food_truck_schedule(self, e):
        print("Food truck schedule page opened!")

    def show_maps_to_event(self, e):
        print("Maps to the event page opened!")

    def show_special_guests_and_speakers(self, e):
        print("Special guests and speakers page opened!")

def main(page: ft.Page) -> None:
    app = VisionLotus()
    page.appbar = app.appbar
    page.add(ft.Text("Vision Lotus!", style=ft.TextStyle(color=ft.colors.RED)))

if __name__ == "__main__":
    ft.app(target=main)
