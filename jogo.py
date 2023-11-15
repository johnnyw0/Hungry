from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from funcoes import*


def jogo():

    #criando janela do jogo
    janela = Window(800,400)
    janela.set_title('Hungry')
    out_menu = True

    teclado = janela.get_keyboard()
    
    fundo = GameImage("png/fundo.png")
    fundo.x = janela.width/2 - fundo.width/2
    fundo.y = janela.height/2 - fundo.height/2
    
    fundo2 = GameImage("png/fundo.png")
    fundo2.x = fundo.x + fundo.width
    fundo2.y = fundo.y
    
    vel_fundo = 300
    
    player = Sprite('png/player.png', 8)
    player.set_total_duration(500)
    
    player.x = 40
    
    limite_inferior = janela.height - player.height - 40
    player.y = limite_inferior
    
        
    vel_y = 0    
    
    pulo = False
    
    
    pontuacao = 0


    while out_menu:

        fundo.x -= vel_fundo * janela.delta_time()
        if fundo.x <= -fundo.width: fundo.x += fundo.width
        
        fundo2.x = fundo.x + fundo.width
        
        
        if(teclado.key_pressed("space") and not pulo):
            pulo = True
            vel_y = -2000
        
        if pulo:
            player.move_y(vel_y * janela.delta_time())
            vel_y += 100
        
        if player.y > limite_inferior:
            player.y = limite_inferior
            vel_y = 0
            pulo = False
        
        pontuacao += janela.delta_time()/10
        
        
        fundo.draw()
        fundo2.draw()
        
        player.update()
        player.draw()
        
        janela.draw_text(f"{int(pontuacao*1000)}", 10, 10, size=20, color=[255,255,255], font_name="Arial")



        out_menu = voltar_menu()
        janela.update()