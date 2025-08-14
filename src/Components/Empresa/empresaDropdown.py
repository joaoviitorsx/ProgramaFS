import flet as ft

def empresa_dropdown():
    return ft.Dropdown(
        label="Empresa",
        options=[
            ft.dropdown.Option("1", "ATACADO 25 LTDA"),
            ft.dropdown.Option("2", "DISTRIBUIDORA VALE NORTE"),
        ],
        width=400
    )
