from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from funcoes import*

def jogo():

    #criando janela do jogo
    janela = Window(540,720)
    janela.set_title('Hungry')
    #bg = GameImage("png/.png")
    out_menu = True
    teclado = Window.get_keyboard()

    while out_menu:

        out_menu = voltar_menu()
        janela.update()