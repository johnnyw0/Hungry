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

    

    #setup do player
    player = Sprite('png/player.png', 8)
    player.set_total_duration(500)
    posicao_meio = 160
    player.x = posicao_meio - player.width/2
    limite_inferior = janela.height - player.height - 70
    player.y = limite_inferior
    vel_y = 0    
    pulo = False
    inv = False
    
    
    ##### PONTUACAO, VIDA E OBSTACULOS #####
    obst1 = GameImage("png/cacto.png")
    obst2 = GameImage("png/pedra1.png")
    obst3 = GameImage("png/pedra2.png")
    pontuacao = 0
    comecou = False
    
    vidas = []
    for _ in range(3):
        vidas = add_vida(vidas)
    
    select_obst = [obst1, obst2, obst3]
    obstaculos = []

    coletaveis = []
    cont_inv = 0

    ####
    novo_obstaculo = 50

    novo_coletavel = 325
    ####

    
    ########## SOM ###########
    grito1 = Sound("audio/grito1.ogg")
    grito2 = Sound("audio/grito2.ogg")
    gritos = [grito1, grito2]
    gamebg = Sound("audio/gamebg.ogg")
    gamebg.set_volume(50)
    Sound.play(gamebg)
    gamebg.set_repeat(True)
    collect = Sound("audio/Untitled.ogg")

    janela.update()


    ############ GAMELOOP ##############
    while out_menu:

        if teclado.key_pressed("esc"):
            parar(gamebg)
        ########## MOVIMENTO DO FUNDO ##########
        fundo.x -= vel_fundo * janela.delta_time()
        if fundo.x <= -fundo.width: fundo.x += fundo.width
        
        fundo2.x = fundo.x + fundo.width



        
        ########### PULO ############
        if(teclado.key_pressed("space") and not pulo):
            player = GameImage('png/player_pulo.png')
            player.x = posicao_meio - player.width/2
            player.y = limite_inferior

            pulo = True
            vel_y = -3 * vel_fundo
        
        if pulo:
            player.y += vel_y * janela.delta_time()
            vel_y += janela.delta_time() * vel_fundo * 10
        
        if player.y > limite_inferior:
            
            player = Sprite('png/player.png', 8)
            player.set_total_duration(500)
            player.x = posicao_meio - player.width/2
            player.y = limite_inferior
            vel_y = 0
            pulo = False

        if player.y < 0:
            player.y = 0
        

        ########## PONTUACAO E OBSTACULO ############
        pontuacao += vel_fundo * janela.delta_time()/100
        
        if(pontuacao >= novo_obstaculo):
            obstaculos = add_obstaculo(obstaculos, select_obst)
            novo_obstaculo += 50

        if(pontuacao >= novo_coletavel):
            coletaveis = add_coletavel(coletaveis)
            novo_coletavel += 500
        
        fundo.draw()
        fundo2.draw()
        
        if not pulo: player.update()
        player.draw()


        ########### COLISAO E PERDA DE VIDA ############
        for obstaculo in obstaculos:

            obstaculo.x += (-vel_fundo * janela.delta_time())
            if obstaculo.x + obstaculo.width <= 0:
                obstaculos.remove(obstaculo)
                continue
            
            obstaculo.draw()

            if colisao(obstaculo, player, pulo) and not inv:
                obstaculos.remove(obstaculo)
                vidas.remove(vidas[0])
                grito_escolhido = random.choice(gritos)
                Sound.play(grito_escolhido)
                grito_escolhido.fadeout(1000)

                inv = True
                vel_fundo = 800

        for coletavel in coletaveis:
            coletavel.x += (-vel_fundo * janela.delta_time())
            if coletavel.x + coletavel.width <= 0:
                coletaveis.remove(coletavel)
                continue

            coletavel.draw()

            if Collision.collided(player, coletavel) and len(vidas) < 3:
                collect.play()
                coletaveis.remove(coletavel)
                vidas = add_vida(vidas)
        
            

        if inv:
            cont_inv += janela.delta_time()
            if cont_inv >= 2:
                cont_inv = 0
                inv = False

        if len(vidas) == 0:
            print(type(pontuacao))
            gamebg.stop()
            nome = input("Qual seu nome?: ")
            arq = open("ranking.txt", 'a')
            arq.write(f"{nome}: {pontuacao:.2f}")
            arq.write("\n")
            break

        for vida in vidas: vida.draw()
    
        if (not comecou and pontuacao > 0):
            pontuacao = 0
            vel_fundo = 800
        comecou = True
        
        janela.draw_text(f"{int(pontuacao)}", 45, 25, size=72, color=[255,165,0], font_name='gemstoneregular')


        vel_fundo += 5 * janela.delta_time()

        out_menu = voltar_menu()
        janela.update()