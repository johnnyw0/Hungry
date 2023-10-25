from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.mouse import*
import jogo


#Resolução da janela e background
janela = Window(1280,720)
janela.set_title('Hungry')
bg = GameImage('png/bg.png')

#Botões e título do jogo que estão no menu            
title = GameImage('png/logo.png')
title.set_position(janela.width/2-title.width/2, 100)   #O título é espaçado de 100 pixels do começo da janela, o botão de jogar é espaçado 150 pixels do título
play = GameImage('png/play.png')                        #e os botões tem espaçamento de 100 pixels entre si
play.set_position(janela.width/2-play.width/2, janela.height-200)
exit = GameImage('png/exit.png')
exit.set_position(janela.width-exit.width, 0)


# #Destaque nos botões
dexit = GameImage('png/dexit.png')
dexit.set_position(janela.width-dexit.width, 0)
dplay = GameImage('png/dplay.png')
dplay.set_position(janela.width/2-play.width/2, janela.height-200)



#Mouse e teclado
mouse = Window.get_mouse()
teclado = Window.get_keyboard()

#Sentinelas para definir as telas
i_menu = True


#Gameloop
while i_menu:

    bg.draw()
    title.draw()
    exit.draw()
    play.draw()


    #Destaque e efeitos dos botões
    if mouse.is_over_object(exit):
        dexit.draw()

        if mouse.is_button_pressed(1):
            janela.close()




    if mouse.is_over_object(play):
        dplay.draw()

        if mouse.is_button_pressed(1):
            jogo.jogo()


    janela.update()