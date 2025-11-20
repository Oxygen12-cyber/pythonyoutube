import flet as ft


def main(page: ft.Page):

    page.window.height=800
    page.window.width=412
    page.window.title_bar_hidden=True

    def route_change(e: ft.RouteChangeEvent):
        if page.route == "/":
            homepage(page)
        elif page.route == "/profile":
            profilepage(page)

        page.update()
    
    page.on_route_change = route_change
    page.go("/")



    

if __name__ == '__main__':
    ft.app(main, assets_dir="src/assets")