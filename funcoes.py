from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from PPlay.collision import*
from funcoes import*

janela = Window(540,720)
janela.set_title('Hungry')
teclado = Window.get_keyboard()

def voltar_menu():
    return False if teclado.key_pressed("esc") else True


def add_vida(vidas):
    vida = GameImage("png/heart.png")
    if(vidas):
        vida.x = vidas[-1].x - 80
    else:
        vida.x = 1050

    vida.y = 25

    vidas.append(vida)
    return vidas

def add_obstaculo(obstaculos):
    obstaculo = Sprite("png/pedra1.png")
    obstaculo.x = 1200
    obstaculo.y = 630 - obstaculo.height

    obstaculos.append(obstaculo)

    return obstaculos
        
def colisao(obstaculo, player):
    return True if Collision.collided(obstaculo, player) else False
