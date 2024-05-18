import flet as ft

from ui.pages import EventSchedulePage as ESP

def main(page: ft.Page) -> None:
    def __init__():
        page.update()
        

    def show_auction_info(self, e):
        print("Auction information page opened!")

    def show_event_schedules(self):
        print("Event schedules page opened!")
        self.ESP = ESP()
        self.ESP.loadpage()
        appbody.controls=[self.ESP]
        page.update()
        
        return 

    def show_maps_to_event(self, e):
        print("Maps to the event page opened!")

    def show_special_guests_and_speakers(self, e):
        # this is pseudocode, you'll know what I mean:
        # from ui.specialguests import List as L
        # self.guestlist = L()
        # appbody.controls = [self.guestlist]

        
        print("Special guests and speakers page opened!")

    
    appbar = ft.AppBar(
        leading=ft.IconButton(icon=ft.icons.HOME_OUTLINED, on_click=main.__init__()),
        title=ft.Text(value="Vision Lotus",color=ft.colors.RED_400),
        center_title=False,
        bgcolor=ft.colors.BLACK,
        actions=[
            ft.PopupMenuButton(icon=ft.icons.MENU,
                               bgcolor=ft.colors.GREY_800,
                               items=[
            ft.PopupMenuItem(text="Presenter Application"),
            ft.PopupMenuItem(text="Volunteer Application"),
            ft.PopupMenuItem(text="Sponsorship Application"),
            ft.PopupMenuItem(text="Vendor Application"),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(text="Event Schedule",on_click=show_event_schedules),
            ft.PopupMenuItem(text="Map"),
            ft.PopupMenuItem(text="Auction Information",on_click=show_auction_info),
            ])])
    
    appbody = ft.Column(controls=[
        ft.Text(value="Vision Home Page Placeholder")
    ])
 


    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE,
            secondary=ft.colors.GREY,
        ),
        font_family="Open Sans"
    )
    page.appbar = appbar
    page.add(appbody)

if __name__ == "__main__":
    ft.app(target=main)
