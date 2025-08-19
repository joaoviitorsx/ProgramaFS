import flet as ft
from src.Config import theme
from src.Controllers.spedReaderController import inserirDadosSped
import threading

def estado_processamento(controller):
    th = theme.get_theme()

    texto_status = ft.Text("Selecione o arquivo SPED para processar", color=th["TEXT"])
    nome_arquivo = ft.Text("", color=th["TEXT_SECONDARY"])
    barra_progresso = ft.ProgressBar(width=400, visible=False)
    mensagem_erro = ft.Text("", color=th["ERROR"], size=12)

    botao_selecionar = ft.ElevatedButton(
        "Selecionar Arquivo",
        bgcolor=th["PRIMARY_COLOR"],
        color=th["ON_PRIMARY"]
    )

    botao_voltar = ft.OutlinedButton(
        "Voltar para Início",
        icon=ft.Icons.ARROW_BACK,
        on_click=lambda _: controller.atualizar_estado("inicial")
    )

    def processar_arquivo(caminho_arquivo):
        texto_status.value = "Processando arquivo..."
        mensagem_erro.value = ""
        barra_progresso.visible = True
        controller.update()

        resultado = inserirDadosSped(
            empresa_id=controller.empresa_id,
            periodo=controller.get_periodo(),
            arquivos=[caminho_arquivo]
        )

        if resultado["success"]:
            texto_status.value = resultado["mensagem"]
            controller.set_arquivo_sped(caminho_arquivo)
            controller.update()
            controller.atualizar_estado("baixar")
        else:
            texto_status.value = ""
            mensagem_erro.value = resultado["mensagem"]
            barra_progresso.visible = False
            controller.update()

    def ao_escolher_arquivo(e: ft.FilePickerResultEvent):
        if e.files:
            caminho_arquivo = e.files[0].path
            nome_arquivo.value = e.files[0].name
            controller.update()

            threading.Thread(target=processar_arquivo, args=(caminho_arquivo,)).start()

    file_picker = ft.FilePicker(on_result=ao_escolher_arquivo)
    controller.page.overlay.append(file_picker)
    controller.page.update()

    botao_selecionar.on_click = lambda _: file_picker.pick_files(allow_multiple=False)

    return ft.Column(
        controls=[
            ft.Text("Processamento do Arquivo", size=22, weight=ft.FontWeight.BOLD, color=th["TEXT"]),
            ft.Divider(),
            texto_status,
            nome_arquivo,
            mensagem_erro,
            barra_progresso,
            ft.Row(
                controls=[botao_voltar, botao_selecionar],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )
