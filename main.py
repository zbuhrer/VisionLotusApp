import flet as ft


def main(page: ft.Page) -> None:
    def show_auction_info(self, e):
        print("Auction information page opened!")

    def show_event_schedules(self):
        print("Event schedules page opened!")
        
        appbody.value="Event schedules page placeholder."
        page.update()
        
        return 

    def show_food_truck_schedule(self, e):
        print("Food truck schedule page opened!")

    def show_maps_to_event(self, e):
        print("Maps to the event page opened!")

    def show_special_guests_and_speakers(self, e):
        print("Special guests and speakers page opened!")

    appbar = ft.AppBar(
        leading=ft.PopupMenuButton(icon=ft.icons.HOME_OUTLINED,items=[
            ft.PopupMenuItem(text="Event Schedule",on_click=show_event_schedules),
            ft.PopupMenuItem(text="Map"),
            ft.PopupMenuItem(text="Auction Information",on_click=show_auction_info),
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
    
    appbody = ft.Text(value="Vision Home Page Placeholder")
 


    page.appbar = appbar
    page.add(appbody)

if __name__ == "__main__":
    ft.app(target=main)
