from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.mouse import*
import funcoes

def rank():


    #Resolução da janela e background
    janela = Window(1200,700)
    janela.set_title('Space Invaders')
    janela.set_background_color([255, 165, 0])
    mouse = Window.get_mouse()



    #Sentinela que verifica se está no menu principal ou não
    out_menu = True

    lista_ord = funcoes.ordena_arq("ranking.txt")


    while out_menu:

        janela.draw_text("RANKING", janela.width/2 - 100, 50, size=48, color=(255, 0, 0), font_name='gemstoneregular', bold=False, italic=False)
        for i in range(len(lista_ord)):
            if i == 5: break
            janela.draw_text(f"{lista_ord[i][0]}: {lista_ord[i][1]}", janela.width/2 - 100, 200 + (i * 100), size=36, color=(255, 0, 0), font_name='gemstoneregular', bold=False, italic=False)

        janela.update()