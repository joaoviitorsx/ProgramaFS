import flet as ft
from src.Config import theme
from src.Controllers.fsExportController import exportarFS
import os

def estado_baixar(controller):
    th = theme.get_theme()

    texto_status = ft.Text("Gerando arquivo .fs...", color=th["TEXT"])
    nome_arquivo = ft.Text("", color=th["TEXT_SECONDARY"])
    erro = ft.Text("", color=th["ERROR"], size=12)

    def gerar_arquivo():
        resultado = exportarFS(
            empresa_id=controller.empresa_id,
            periodo=controller.get_periodo(),
            nome_empresa=controller.nome_empresa
        )

        if resultado["success"]:
            controller.set_arquivo_fs(resultado["caminho"])
            nome = os.path.basename(resultado["caminho"])
            texto_status.value = "Arquivo gerado com sucesso!"
            nome_arquivo.value = f"• {nome}"
        else:
            texto_status.value = ""
            erro.value = resultado["mensagem"]

        controller.update()

    def ao_baixar(e):
        if controller.arquivo_fs and os.path.exists(controller.arquivo_fs):
            os.startfile(controller.arquivo_fs)  # abre o arquivo no sistema operacional
        else:
            erro.value = "Arquivo não encontrado."
            controller.update()

    botao_baixar = ft.ElevatedButton(
        "Baixar",
        icon=ft.Icons.DOWNLOAD,
        bgcolor=th["PRIMARY_COLOR"],
        color=th["ON_PRIMARY"],
        on_click=ao_baixar
    )

    botao_voltar = ft.OutlinedButton(
        "Processar novamente",
        icon=ft.Icons.RESTART_ALT,
        on_click=lambda _: controller.atualizar_estado("processamento")
    )

    gerar_arquivo()

    return ft.Column(
        controls=[
            ft.Text("Arquivo Gerado", size=22, weight=ft.FontWeight.BOLD, color=th["TEXT"]),
            ft.Divider(),
            texto_status,
            nome_arquivo,
            erro,
            ft.Row(
                controls=[botao_voltar, botao_baixar],
                alignment=ft.MainAxisAlignment.END
            )
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )
