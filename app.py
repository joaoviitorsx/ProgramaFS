import flet as ft
from src.Config import theme
from src.Interface.home import HomePage
from src.Utils.path import resourcePath

def main(page: ft.Page):
    th = theme.aplicar_theme(page)

    page.title = "ProgramaFS"
    page.window.height = 800
    page.window.width = 650
    page.window.max_height = 800
    page.window.max_width = 650
    page.window.icon = resourcePath("src/assets/icone.ico")

    def trocaRota(e):
        page.views.clear()

        if page.route in ["/", "/home"]:
            page.views.append(HomePage(page))
        else:
            page.views.append(ft.View("/", controls=[ft.Text("Página não encontrada!")]))

        page.update()

    page.on_route_change = trocaRota
    page.go("/home")

ft.app(target=main, assets_dir="assets", view=ft.AppView.FLET_APP)
