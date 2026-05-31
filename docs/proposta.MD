# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

> Fuja  da Tempestade de Meteoros

---

## 2. Integrantes do grupo

- David Aurélio Pedrosa
- Saul de Castro Macedo
- Tiago Belico de Oliveira e Silva


---

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Nave desviando de meteoros.

---

## 4. Descrição geral do jogo

Descrição:

> O jogo será um jogo 2D em que o jogador controla uma nave espacial enquanto meteoros caem pela tela. O objetivo será desviar dos meteoros pelo maior tempo possível. Durante a partida, a velocidade dos meteoros poderá aumentar gradualmente, aumentando a dificuldade do jogo. Além disso, o jogador poderá coletar kits de reparo ao longo da partida, permitindo recuperar vida após colisões. O jogador controlará a nave utilizando o teclado e deverá evitar colisões para continuar sobrevivendo.


---

## 5. Objetivo do jogador

Objetivo:

> Sobreviver pelo maior tempo possível desviando dos meteoros e alcançar a maior pontuação possível.

---

## 6. Regras principais

Regras do grupo:

- O jogador controla uma nave que pode se mover horizontalmente.

- Meteoros aparecem aleatoriamente. 

- Cada colisão com um meteoro remove uma vida do jogador.

- O jogador começa com 3 vidas.

- O jogo termina quando todas as vidas acabam.

---

## 7. Condição de vitória

O jogador vence ao sobreviver por um determinado tempo.

---

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> O jogo irá acabar no momento em que o jogador perder as suas 3 vidas.

---

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

Descrição:

> Uma nave espacial controlada pelas teclas do teclado.

### Obstáculos, inimigos ou desafios

Descrição:

> Meteoros aparecem aleatoriamente e caem em direção ao jogador, exigindo reflexos do jogador para que ele não perca vida batendo nos meteoros.

### Itens, alvos ou objetos de interação

Descrição:

> Ao longo do jogo irá aparecer alguns kit  de reparo, que serão responsáveis por restaurar a vida da nave.

### Pontuação, vidas, tempo ou progresso

Descrição:

> O jogador inicia com 3 vidas e ganha pontos conforme sobrevive durante a partida. A dificuldade poderá aumentar com o tempo.

---

## 10. Controles previstos

Controles do grupo:

- Seta para esquerda: mover nave para esquerda
- Seta para direita: mover nave para direita
- ESC: sair do jogo

---

## 11. Organização inicial do código

Organização planejada:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: configurações gerais do jogo;
- `src/player.py`: controle da nave do jogador;
- `src/meteoro.py`:  movimentação dos meteoros.

---

## 12. Recursos externos previstos

Recursos previstos:

- imagens para nave e meteoros gratuitos;
- efeitos sonoros gratuitos;
- tutoriais utilizados apenas como referência.

---

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- fazer a movimentação da nave;
- relizar a colisão entre nave e meteoros;
- aumentar a dificuldade do jogo.

---

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá uma nave controlada pela setas do teclado, meteoros caindo aleatoriamente, sistema de colisão que terá quando a nave bater no meteoro, sistema de vidas, pontuação e tela de fim de jogo.

---

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- tela inicial;
- sons e música de fundo;
- aumento gradual da velocidade dos meteoros;
- tipos diferentes de meteoros
- animações de explosão;
- menu de pausa;
- rank no jogo.
