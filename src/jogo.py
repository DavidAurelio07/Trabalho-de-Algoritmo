import pygame
import random

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    recuperar_vida,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True



    # IMAGEM DA NAVE
    nave_image = pygame.image.load("assets/imagens/nave.png")
    nave_image = pygame.transform.scale(nave_image,(128, 128))

    # Kit de reparo
    kit_image    = pygame.image.load("assets/imagens/kit.png")
    kit_image    = pygame.transform.scale(kit_image,(64, 64))

    # IMAGEM DO METEORO
    meteoro_image  = pygame.image.load("assets/imagens/meteoro.png")
    meteoro_image  = pygame.transform.scale(meteoro_image,(128, 128))
    
    # imagens
    nave = {
        "imagem": nave_image,
        "rect": nave_image.get_rect(topleft=(350, 600))
    }
    nave["rect"].inflate_ip(-70,20)

    kit= {
        "imagem": kit_image,
        "rect": kit_image.get_rect(topleft=(500, 300))
    }
    

    #lugar para  criar meteoros- atualmente tem 5 meteoros na lista
    meteoros = []

    for i in range(5):
        novo_meteoro = { "imagem": meteoro_image,
                        "rect": meteoro_image.get_rect( topleft=( random.randint( 0, LARGURA_TELA - meteoro_image.get_width() ),
                        random.randint(-600, -50) 
                        ) 
                    )
            } 
        novo_meteoro["rect"].inflate_ip(-70, -70)
        meteoros.append(novo_meteoro)

    velocidade = 5
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo = 0
    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        #parte para fazer a pontuação do JOGO
        tempo += 1 / FPS

        if tempo < 30:
            pontos += 1 / FPS

        elif tempo < 60:
            pontos += 2 / FPS

        else:
            pontos += 3 / FPS

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()

        # Movimentação da nave para ESQUERDA E DIREITA
        if teclas[pygame.K_LEFT]:
            nave["rect"].x -= velocidade
        if teclas[pygame.K_RIGHT]:
            nave["rect"].x += velocidade

        #Parte para fazer os meteoros descer na tela


        for meteoro in meteoros:

            meteoro["rect"].y += 5

            if meteoro["rect"].y > ALTURA_TELA:
                meteoro["rect"].x = random.randint( 0, LARGURA_TELA - meteoro["rect"].width )
                meteoro["rect"].y = random.randint(-300, -50)


        #Parte para fazer os kit descer na tela

        kit["rect"].y += 5

        if kit["rect"].y > ALTURA_TELA:
            kit["rect"].x = random.randint(0,LARGURA_TELA - kit["rect"].width)    
            kit["rect"].y = random.randint(-300,-50)



        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
        nave["rect"].x = limitar_valor(nave["rect"].x, 0, LARGURA_TELA - nave["rect"].width)
        nave["rect"].y = limitar_valor(nave["rect"].y, 0, ALTURA_TELA - nave["rect"].height)

        

        #NAVE PEGAR O KIT DE REPARO
        if vidas < 3:
            if verificar_colisao(nave["rect"], kit["rect"]):
                vidas = recuperar_vida(vidas,1)

                kit["rect"].x = random.randint( 0, LARGURA_TELA - kit["rect"].width ) 
                kit["rect"].y = random.randint(-300, -50)
                

            


        for meteoro in meteoros:
            # CONTATO DA NAVE COM O METEORO
            if verificar_colisao(nave["rect"], meteoro["rect"]):
                vidas = tomar_dano(vidas, 1)

                meteoro["rect"].y = random.randint(-300, -50) 
                meteoro["rect"].x = random.randint( 0, LARGURA_TELA - meteoro["rect"].width )

        # Regras de fim de jogo e recorde
        if jogador_perdeu(vidas):
            rodando = False

        if int(pontos) > recorde:
            recorde = int(pontos)
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {int(pontos)} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(CINZA)

        # Desenhando os elementos na tela passando a imagem e o rect de cada dicionário
        tela.blit(kit["imagem"], kit["rect"])
        for meteoro in meteoros:
            tela.blit(meteoro["imagem"], meteoro["rect"])
        tela.blit(nave["imagem"], nave["rect"])

        pygame.display.flip()

    pygame.quit()