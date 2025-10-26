import flet as ft


def main(page: ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.padding=0
    page.spacing=0


    page.add(
        ft.Container(
            bgcolor="#111921",
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Container(
                bgcolor="#1a232b",
                width=700,
                height=300,
                border_radius=12,
                border=ft.border.all(width=1,color="#27323c")
            )
        )
    )









if __name__ == "__main__":
    ft.app(target=main)