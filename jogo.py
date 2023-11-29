from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from PPlay.collision import*
from funcoes import*


def jogo():

    #criando janela do jogo
    janela = Window(1200,700)
    janela.set_title('Hungry')
    out_menu = True

    teclado = janela.get_keyboard()
    


    #setup do fundo
    fundo = GameImage("png/fundo.png")
    fundo.x = janela.width/2 - fundo.width/2
    fundo.y = janela.height/2 - fundo.height/2
    fundo2 = GameImage("png/fundo.png")
    fundo2.x = fundo.x + fundo.width
    fundo2.y = fundo.y
    vel_fundo = 500
    

    #setup do player
    player = Sprite('png/player.png', 8)
    player.set_total_duration(500)
    player.x = 40
    limite_inferior = janela.height - player.height - 70
    player.y = limite_inferior
    vel_y = 0    
    pulo = False
    
    
    pontuacao = 0

    vidas = []

    for _ in range(3):
        vidas = add_vida(vidas)

    obstaculos = []

    ####
    teste_obstaculo = 50
    ####

    
    while out_menu:


        ########## MOVIMENTO DO FUNDO ##########
        vel_fundo += 20 * janela.delta_time()
        
        fundo.x -= vel_fundo * janela.delta_time()
        if fundo.x <= -fundo.width: fundo.x += fundo.width
        
        fundo2.x = fundo.x + fundo.width


        
        ########### PULO ############
        if(teclado.key_pressed("space") and not pulo):
            pulo = True
            vel_y = -2200
        
        if pulo:
            player.move_y(vel_y * janela.delta_time())
            vel_y += 10000 * janela.delta_time()
        
        if player.y > limite_inferior:
            player.y = limite_inferior
            vel_y = 0
            pulo = False

        

        ########## PONTUACAO E OBSTACULO ############
        pontuacao += vel_fundo * janela.delta_time()/100
        
        if(pontuacao >= teste_obstaculo):
            obstaculos = add_obstaculo(obstaculos)
            teste_obstaculo += 100
        
        fundo.draw()
        fundo2.draw()
        
        player.update()
        player.draw()

        for obstaculo in obstaculos:

            obstaculo.x -= vel_fundo * janela.delta_time()
            obstaculo.draw()

            if colisao(obstaculo, player):
                obstaculos.remove(obstaculo)
                vidas.remove(vidas[0])

        if len(vidas) == 0:
            break

        for vida in vidas: vida.draw()

        ########### COLISAO E PERDA DE VIDA ############

        
        janela.draw_text(f"{int(pontuacao)}", 10, 10, size=20, color=[255,255,255], font_name="Arial")



        out_menu = voltar_menu()
        janela.update()