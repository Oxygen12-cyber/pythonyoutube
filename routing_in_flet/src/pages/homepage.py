import flet as ft


def homepage(page):
    page.bgcolor="white"
    page.views.clear()
    page.views.append(
        ft.View(
            "/",
            spacing=0,
            padding=0,
            bgcolor="white",
            appbar= ft.AppBar(
                color="yellow", 
                bgcolor="yellow", elevation=0, elevation_on_scroll=1, 
                shadow_color="transparent", title_spacing=1.2
            ),
            controls=[
                ft.Container(
                            # width=float('inf'),height=float('inf'),
                            expand=1,
                            expand_loose = True,
                            bgcolor="yellow",
                            content=ft.Container(ft.Image(src="../assets/police_bg.png", fit=ft.ImageFit.COVER), width=200, height=200),
                            alignment=ft.alignment.center
                ),
                ft.Container(
                            # height=float('inf'), width=float('inf'),
                            expand=1,
                            bgcolor="white",
                            padding=ft.padding.symmetric(horizontal=14, vertical=10),
                            content= ft.Column(
                                [
                                    ft.Container(height=15),
                                    ft.Text("Save Up To $250 Over\n 12 Months With It", color="black", weight=ft.FontWeight.BOLD, size=32, text_align=ft.TextAlign.CENTER),
                                    ft.Container(height=15),
                                    ft.Text("You'll also save 10$/mth for 12 months + an additional ongoing 10$/mth", text_align=ft.TextAlign.CENTER,color=ft.Colors.BLACK38, size=16, weight=ft.FontWeight.W_400),
                                    ft.Container(height=60),
                                    ft.GestureDetector(ft.Container(alignment=ft.alignment.center,width=300, content=ft.Text("Login ", color="white", size=18, weight=ft.FontWeight.BOLD), border_radius=32, padding=18, bgcolor="black"), on_tap=lambda _: page.go("/profile"))
                                ],
                                tight=True,
                                spacing=10,
                                alignment=ft.MainAxisAlignment.START,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                )
            ]
        )
    )