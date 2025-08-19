import flet as ft
from src.Config import theme
from src.Controllers.empresaController import cadastrarEmpresa

def estado_cadastro(controller):
    th = theme.get_theme()

    input_cnpj = ft.TextField(
        label="CNPJ da empresa",
        width=400,
        border_radius=theme.STYLE["BORDER_RADIUS_INPUT"],
        bgcolor=th["INPUT_BG"],
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    razao_social = ft.Text(
        value="Razão social aparecerá aqui...",
        size=14,
        color=th["TEXT_SECONDARY"]
    )

    texto_erro = ft.Text("", color=th["ERROR"], size=12)

    resultado_api = {}

    def ao_inserir_cnpj(e):
        cnpj = input_cnpj.value.strip()

        if len(cnpj) < 14:
            razao_social.value = "CNPJ inválido"
            texto_erro.value = ""
            controller.update()
            return

        nonlocal resultado_api
        resultado_api = cadastrarEmpresa(cnpj)

        if resultado_api.get("status") == "ok":
            razao_social.value = resultado_api["razao_social"]
            texto_erro.value = ""
        else:
            razao_social.value = ""
            texto_erro.value = resultado_api.get("mensagem", "Erro ao buscar empresa")

        controller.update()

    def ao_cadastrar(e):
        if resultado_api.get("status") == "ok":
            controller.set_empresa(
                id=resultado_api["empresa_id"],
                nome=resultado_api["razao_social"],
                cnpj=resultado_api["cnpj"]
            )
            controller.atualizar_estado("processamento")
        else:
            texto_erro.value = "Consulte um CNPJ válido antes de cadastrar."
            controller.update()

    input_cnpj.on_change = ao_inserir_cnpj

    btn_cadastrar = ft.ElevatedButton(
        "Cadastrar",
        bgcolor=th["PRIMARY_COLOR"],
        color=th["ON_PRIMARY"],
        on_click=ao_cadastrar,
    )

    btn_voltar = ft.OutlinedButton(
        "Voltar",
        on_click=lambda _: controller.atualizar_estado("inicial")
    )

    return ft.Column(
        controls=[
            ft.Text("Cadastro de Empresa", size=22, weight=ft.FontWeight.BOLD, color=th["TEXT"]),
            ft.Divider(),
            input_cnpj,
            razao_social,
            texto_erro,
            ft.Row(controls=[btn_voltar, btn_cadastrar], alignment=ft.MainAxisAlignment.END)
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )
