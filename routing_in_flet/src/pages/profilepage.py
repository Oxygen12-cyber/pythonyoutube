import flet as ft


class SizedBox(ft.Container):
    def __init__(self, height: int = 0, width: int = 0, child = None):
        super().__init__()
        self.height=height
        self.width=width
        self.content=child





def profilepage(page):
    page.views.clear()
    page.views.append(
        ft.View(
            "/profile",spacing=0,padding=0,bgcolor="white",
            appbar=ft.AppBar(
                bgcolor="white",
                leading=ft.Container(
                    padding=5,
                    content=ft.ElevatedButton(
                    on_click=lambda _: page.go("/"),
                    height=18,width=18,
                    style=ft.ButtonStyle(shape=ft.CircleBorder(), color="black", bgcolor="black"), 
                    content=ft.Icon(
                        ft.Icons.CHEVRON_LEFT_ROUNDED, color="white", size=18)
                    )
                ),
                title=ft.Text(
                    "Profile", color="black",size=24,
                    weight=ft.FontWeight.BOLD,
                ),center_title=True,

            ),
            controls=[
                ft.Container(
                    expand=True,
                    alignment = ft.alignment.center,
                    content=ft.Column(
                        [
                            SizedBox(height=25),
                            ft.Container(
                                width=200, height=200,border_radius=200,bgcolor="yellow",
                                content=ft.Image(src="../assets/avatar_image2.png", fit=ft.ImageFit.COVER)
                            ),
                            SizedBox(height=10),
                            ft.Text(
                                "Alexdra Jamie", size=18, weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK87,text_align=ft.TextAlign.CENTER,
                                spans=[
                                    ft.TextSpan(
                                        "\n HI I'm Jamie. Age : 23 Nationality : SA",
                                        style=ft.TextStyle(
                                            size=14,color=ft.Colors.BLACK38, weight=ft.FontWeight.W_400
                                        )
                                    )
                                ]
                            ),
                            SizedBox(height=40),
                            ft.IconButton(
                                ft.Icons.CHEVRON_LEFT_ROUNDED, icon_color="white",
                                tooltip=ft.Tooltip("Go Back"), bgcolor="black",icon_size=64,
                                on_click=lambda _: page.go("/")
                                )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            ]
        )
    )