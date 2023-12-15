from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.mouse import*
import jogo
import ranking


#Resolução da janela e background
janela = Window(1200,700)
janela.set_title('Rungry')
bg = GameImage('png/bg.png') 

#Botões e título do jogo que estão no menu            
play = GameImage('png/play.png')                      
play.set_position(janela.width/2-play.width/2 + 5, janela.height/2 + 130)
rank = GameImage('png/rank.png')
rank.set_position(janela.width/2-rank.width/2 + 5, janela.height/2 + 200)


# #Destaque nos botões
dplay = GameImage('png/dplay.png')
dplay.set_position(janela.width/2-play.width/2 + 5, janela.height/2+ 130)
drank = GameImage('png/drank.png')
drank.set_position(janela.width/2-rank.width/2 + 5, janela.height/2 + 200)

#Mouse e teclado
mouse = Window.get_mouse()
teclado = Window.get_keyboard()

#Sentinelas para definir as telas
i_menu = True


#Menuloop
while i_menu:

    bg.draw()
    play.draw()
    rank.draw()

    #Destaque e efeitos dos botões
    if mouse.is_over_object(play):
        dplay.draw()

        if mouse.is_button_pressed(1):
            jogo.jogo()
    
    if mouse.is_over_object(rank):
        drank.draw()

        if mouse.is_button_pressed(1):
            ranking.rank()



    janela.update()