import flet as ft
from Components.Empresa.empresaDropdown import empresa_dropdown
from Components.Upload.uploadSped import upload_sped
from Components.Periodo.periodoDropdown import periodo_dropdown
from Components.GeraFS.botaoGerarFS import botao_gerar_fs


def TelaPrincipal(page: ft.Page):
    page.title = "Gerador de Arquivo .FS"
    page.scroll = ft.ScrollMode.AUTO

    # Componentes da interface
    empresa_dd = empresa_dropdown()
    upload_box = upload_sped()
    periodo_dd = periodo_dropdown()
    botao_gerar = botao_gerar_fs()

    status_text = ft.Text("Status: aguardando ação...", color=ft.colors.GREY)

    # Layout da tela
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Selecione a Empresa", size=16),
                    empresa_dd,
                    ft.Divider(),

                    ft.Text("Envie os Arquivos SPED (.txt)", size=16),
                    upload_box,
                    ft.Divider(),

                    ft.Text("Selecione o Período (mês/ano)", size=16),
                    periodo_dd,
                    ft.Divider(),

                    botao_gerar,
                    status_text
                ],
                spacing=20
            ),
            padding=30,
            expand=True
        )
    )
