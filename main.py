import flet as ft

class ConventionApp(ft.UserControl):
    def __init__(self):
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.ARROW_BACK),
            title=ft.Text("Vision Lotus", style=ft.TextStyle(color=ft.colors.RED)),
            center_title=False,
            bgcolor=ft.colors.BLACK,
            )
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
    app = ConventionApp()
    page.appbar = app.appbar
    page.add(ft.Text("Vision Lotus!", style=ft.TextStyle(color=ft.colors.RED)))

if __name__ == "__main__":
    ft.app(target=main)
