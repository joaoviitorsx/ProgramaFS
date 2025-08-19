import flet as ft
from src.Config import theme
from src.Controllers.empresaController import obterEmpresas

def estado_inicial(controller):
    th = theme.get_theme()

    # Consulta empresas do banco
    empresas = obterEmpresas()

    dropdown_empresas = ft.Dropdown(
        label="Selecione a empresa",
        width=400,
        bgcolor=th["INPUT_BG"],
        border_radius=theme.STYLE["BORDER_RADIUS_INPUT"],
        options=[
            ft.dropdown.Option(text=e["razao_social"], key=e["id"]) for e in empresas
        ]
    )

    texto_erro = ft.Text("", color=th["ERROR"], size=12)

    def ao_seguir(e):
        if not dropdown_empresas.value:
            texto_erro.value = "Por favor, selecione uma empresa."
            controller.update()
            return

        # Buscar a empresa selecionada
        empresa_selecionada = next((emp for emp in empresas if str(emp["id"]) == dropdown_empresas.value), None)

        if empresa_selecionada:
            controller.set_empresa(
                id=empresa_selecionada["id"],
                nome=empresa_selecionada["razao_social"],
                cnpj=empresa_selecionada["cnpj"]
            )
            controller.atualizar_estado("processamento")
        else:
            texto_erro.value = "Empresa não encontrada."
            controller.update()

    btn_seguir = ft.ElevatedButton(
        "Seguir",
        bgcolor=th["PRIMARY_COLOR"],
        color=th["ON_PRIMARY"],
        on_click=ao_seguir
    )

    btn_cadastrar = ft.OutlinedButton(
        "Cadastrar nova empresa",
        on_click=lambda _: controller.atualizar_estado("cadastro"),
    )

    return ft.Column(
        controls=[
            ft.Text("Bem-vindo!", size=22, weight=ft.FontWeight.BOLD, color=th["TEXT"]),
            ft.Divider(),
            dropdown_empresas,
            texto_erro,
            ft.Row(controls=[btn_seguir, btn_cadastrar], alignment=ft.MainAxisAlignment.END)
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )
