# testes das funcionalidades do container, como background, bordas, etc.
# teste de funcionamento no mobile e reutilização de compoentes

import flet as ft
from Logica_Container import adivinhar


def main(page: ft.Page):

    # predefinições da página para mobile
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
#

# componentes da tela
    texto = ft.Text("Adivinhe o número entre 1 e 10!")

    lbl_chute = ft.TextField("")

    lbl_resultado = ft.Text("resultado...")

    btn_chute = ft.ElevatedButton(
        "enviar",
        on_click=lambda e: adivinhar(e, lbl_chute, lbl_resultado, page)
    )

    # container de fundo
    container_chute = ft.Container(
        content=(ft.Column([texto, lbl_chute, btn_chute, lbl_resultado])),
        expand=True,
        bgcolor="#3919F7",
        border_radius=20,
        padding=20,
    )
    page.add(container_chute)


ft.app(target=main)
