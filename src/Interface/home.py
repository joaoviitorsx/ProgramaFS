import flet as ft
from src.Components.Empresa.cardCentral import CardCentral

def HomePage(page: ft.Page) -> ft.View:
    return ft.View(
        route="/home",
        controls=[
            ft.Container(
                content=CardCentral(page),
                alignment=ft.alignment.center,
                padding=20,
                expand=True,
            )
        ],
    )
