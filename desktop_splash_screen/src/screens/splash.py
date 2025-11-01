import flet as ft



def main(page: ft.Page):
    page.window.height=600
    page.window.width=800
    page.window.resizable=False

    page.window.title_bar_hidden=True
    page.window.alignment=ft.alignment.center
    
    page.padding=0
    page.spacing=0

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            bgcolor="white",
            content=ft.Stack(
                [
                    ft.Container(
                        expand=True,
                        content=ft.Image(
                            width=800,
                            height=600,
                            src="images/night_bg.jpg",
                            fit=ft.ImageFit.COVER
                        )
                    ),
                    ft.Container(
                        bgcolor=ft.Colors.with_opacity(0.6, "black"),
                        alignment=ft.alignment.bottom_center,
                        content=
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Text("Loading...", color="white", weight="bold", style=ft.TextTheme.body_small),
                                    ft.Container(
                                        width=100,
                                        content=
                                        ft.ProgressBar(
                                            width=100,
                                            height=8,
                                            color="white",
                                            bgcolor="#565b66",
                                            border_radius=14
                                        )

                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            margin=ft.margin.only(bottom=50)
                        )
                    )
                ]
            )
        )
    )





if __name__ == '__main__':
    ft.app(main, assets_dir="src/assets")