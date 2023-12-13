from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from PPlay.collision import*
from funcoes import*
from PPlay.sound import*


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
    vel_fundo = 800
    vel_obst = -800
    

    #setup do player
    player = Sprite('png/player.png', 8)
    player.set_total_duration(500)
    player.x = 40
    limite_inferior = janela.height - player.height - 70
    player.y = limite_inferior
    vel_y = 0    
    pulo = False
    
    
    ##### PONTUACAO, VIDA E OBSTACULOS #####
    obst1 = Sprite("png/cacto.png")
    obst2 = Sprite("png/pedra1.png")
    obst3 = Sprite("png/pedra2.png")
    pontuacao = 0
    vidas = []
    select_obst = [obst1, obst2, obst3]
    for _ in range(3):
        vidas = add_vida(vidas)
    obstaculos = []

    ####
    teste_obstaculo = 50
    ####

    
    ########## SOM ###########
    grito1 = Sound("audio/grito1.ogg")
    grito2 = Sound("audio/grito2.ogg")
    gritos = [grito1, grito2]
    #gamebg = Sound("audio/gamebg.ogg")
    #gamebg.set_volume(10)
    #Sound.play(gamebg)
    #gamebg.set_repeat(True)

    janela.update()
    while out_menu:

        ########## MOVIMENTO DO FUNDO ##########
        fundo.x -= vel_fundo * janela.delta_time()
        if fundo.x <= -fundo.width: fundo.x += fundo.width
        
        fundo2.x = fundo.x + fundo.width



        
        ########### PULO ############
        if(teclado.key_pressed("space") and not pulo):
            pulo = True
            vel_y = -2800
        
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
            obstaculos = add_obstaculo(obstaculos, select_obst)
            teste_obstaculo += 100
        
        fundo.draw()
        fundo2.draw()
        
        player.update()
        player.draw()


        ########### COLISAO E PERDA DE VIDA ############
        for obstaculo in obstaculos:

            obstaculo.move_x(-vel_fundo * janela.delta_time())
            obstaculo.draw()

            if colisao(obstaculo, player):
                obstaculos.remove(obstaculo)
                vidas.remove(vidas[0])
                grito_escolhido = random.choice(gritos)
                Sound.play(grito_escolhido)
                grito_escolhido.fadeout(1000)

        if len(vidas) == 0:
            gamebg.stop()

            nome = input("Qual seu nome?: ")
            arq = open("ranking.txt", 'a')

            arq.write(f"{nome}: {pontuacao}")
            arq.write("\n")
            break

        for vida in vidas: vida.draw()


        
        janela.draw_text(f"{int(pontuacao)}", 10, 10, size=28, color=[255,165,0], font_name='gemstoneregular')


        vel_fundo += 5 * janela.delta_time()

        out_menu = voltar_menu()
        janela.update()