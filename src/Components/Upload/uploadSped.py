import flet as ft

def upload_sped():
    return ft.FilePicker(
        on_result=lambda e: print("Arquivo selecionado:", e.files[0].name) if e.files else None
    )
