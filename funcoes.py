from PPlay.window import*
from PPlay.sprite import*

janela = Window(540,720)
janela.set_title('Hungry')
teclado = Window.get_keyboard()

def voltar_menu():
    return False if teclado.key_pressed("esc") else True