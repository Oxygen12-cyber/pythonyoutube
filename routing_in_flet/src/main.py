import flet as ft
from pages import homepage, profilepage


def main(page: ft.Page):
    page.window.height=800
    page.window.width=412
    page.window.title_bar_hidden=True
    page.window.alignment=ft.alignment.center
    page.fonts={
        "ubuntu-sans": "assets/UbuntuSans-Regular.ttf"
    }
    page.theme=ft.Theme(font_family="ubuntu-sans")


    def route_change(e: ft.RouteChangeEvent):
        if page.route == "/":
            homepage.homepage(page)
        elif page.route == "/profile":
            profilepage.profilepage(page)
        
        page.update()

    page.on_route_change = route_change
    page.go("/")

if __name__ == '__main__':
    ft.app(main)

