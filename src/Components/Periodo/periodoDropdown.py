import flet as ft

def periodo_dropdown():
    return ft.Dropdown(
        label="Período",
        options=[
            ft.dropdown.Option("202506", "Junho/2025"),
            ft.dropdown.Option("202507", "Julho/2025"),
        ],
        width=200
    )
