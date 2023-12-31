from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from PPlay.collision import*
from funcoes import*
import random

janela = Window(540,720)
janela.set_title('Hungry')
teclado = Window.get_keyboard()



def voltar_menu():
    return False if teclado.key_pressed("esc") else True

def parar(musica):
    musica.stop()



def ordena_arq(arquivo):
    arq = open(arquivo, 'r')

    linhas = arq.readlines()
    pessoas = []
    for linha in linhas:
        pessoa = linha.split()
        pessoas.append((pessoa[0], float(pessoa[1])))

    pessoas.sort(key=lambda pessoa: pessoa[1], reverse=True)

    return pessoas



def add_vida(vidas):
    vida = GameImage("png/heart.png")
    if(vidas):
        vida.x = vidas[-1].x - 80
    else:
        vida.x = 1100

    vida.y = 25

    vidas.append(vida)
    return vidas

def add_obstaculo(obstaculos, select_obst):
    obstaculo = random.choice(select_obst)
    obstaculo.x = 1200
    obstaculo.y = 630 - obstaculo.height

    obstaculos.append(obstaculo)

    return obstaculos
        
def colisao(obstaculo, player, pulo):
    if pulo:
        if (obstaculo.x < player.x + player.width) and (player.x <obstaculo.x + obstaculo.width):
            if Collision.collided_perfect(player, obstaculo): return True
        else: return False
    else:
        if (obstaculo.x < player.x + player.width) and (player.x <obstaculo.x + obstaculo.width): return True
        else: return False

def add_coletavel(coletaveis):
    coletavel = GameImage("png/heart.png")
    coletavel.x = 1200
    coletavel.y = 500

    coletaveis.append(coletavel)
    return coletaveis



#187
#214
