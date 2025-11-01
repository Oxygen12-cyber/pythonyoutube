import flet as ft 

from screens import splash


if __name__ == '__main__':
    ft.app(target=splash.main, assets_dir="src/assets")