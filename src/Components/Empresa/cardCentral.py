import flet as ft
from src.Components.Empresa.estadoInicial import estado_inicial
from src.Components.Empresa.estadoCadastro import estado_cadastro
from src.Components.Empresa.estadoProcessamento import estado_processamento
from src.Components.Empresa.estadoBaixar import estado_baixar
from src.Config import theme

class CardCentral(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.theme = theme.get_theme()
        self.estado_atual = "inicial"

        # Dados compartilhados entre os estados
        self.empresa_id = None
        self.nome_empresa = ""
        self.cnpj = ""
        self.arquivo_sped = ""
        self.arquivo_fs = ""
        self.periodo = "062025"  # fixo por enquanto

        self.card = ft.Container(
            padding=30,
            width=500,
            bgcolor=self.theme["CARD"],
            border_radius=theme.STYLE["CARD_RADIUS"],
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=self.theme["TEXT_SECONDARY"],
                offset=ft.Offset(2, 2),
            ),
        )

        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.controls = [self.card]

    def did_mount(self):
        self.atualizar_estado(self.estado_atual)

    # Métodos para estados setarem dados
    def set_empresa(self, id: int, nome: str, cnpj: str):
        self.empresa_id = id
        self.nome_empresa = nome
        self.cnpj = cnpj

    def set_arquivo_sped(self, caminho: str):
        self.arquivo_sped = caminho

    def set_arquivo_fs(self, caminho: str):
        self.arquivo_fs = caminho

    def get_periodo(self):
        return self.periodo

    # Método principal de troca de estado
    def atualizar_estado(self, estado: str):
        self.estado_atual = estado

        if estado == "inicial":
            self.card.content = estado_inicial(self)

        elif estado == "cadastro":
            self.card.content = estado_cadastro(self)

        elif estado == "processamento":
            self.card.content = estado_processamento(self)

        elif estado == "baixar":
            self.card.content = estado_baixar(self)

        self.update()
