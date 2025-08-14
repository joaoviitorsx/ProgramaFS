import flet as ft

def botao_gerar_fs():
    return ft.ElevatedButton(
        text="Baixar Arquivo .FS",
        icon=ft.icons.DOWNLOAD,
        on_click=lambda _: print("Geração solicitada."),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE
    )
