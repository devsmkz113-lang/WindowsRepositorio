import flet as ft
import random

# função para adivinhar o número


def adivinhar(e, lbl_chute, lbl_resultado, page):
    numero_aleatorio = random.randint(1, 10)
    chute = int(lbl_chute.value)

    if chute == numero_aleatorio:
        lbl_resultado.value = "Parabéns! Você acertou!"
    else:
        lbl_resultado.value = f"Errado! O número era {numero_aleatorio}."
    page.update()
