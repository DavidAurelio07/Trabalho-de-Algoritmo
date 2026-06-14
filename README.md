# Space Escape

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- David Aurélio Pedrosa
- Saul de Castro Macedo
- Tiago Belico de Oliveira e Silva


## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Space Escape é um jogo 2D em que o jogador controla uma nave espacial e deve desviar dos meteoros que caem pela tela. Durante a partida, kits de reparo aparecem aleatoriamente e podem ser coletados para recuperar a vida da nave durante a partida. O objetivo é sobreviver pelo maior tempo possível e alcançar a maior pontuação.


## Objetivo do jogador

Sobreviver pelo maior tempo possível, desviando dos meteoros e coletando kits de reparo para manter suas vidas. Quanto mais tempo o jogador permanecer vivo, maior será sua pontuação. A partir de um certo tempo sua pontuação cresce mais rápido.


## Regras do jogo

- O jogador controla uma nave espacial.
- A nave pode se mover horizontalmente pela tela.
- Meteoros caem continuamente do topo da tela.
- Colidir com um meteoro reduz uma vida.
- O jogador começa com 3 vidas.
- Kits de reparo aparecem periodicamente e recuperam uma vida quando coletados
- O jogo terminar quando as vidas acabarem

## Controles

- Seta para esquerda: Move a nave para a esquerda
- Seta para direita: Move a nave para a direita

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/DavidAurelio07/Trabalho-de-Algoritmo.git
cd Trabalho-de-Algoritmo
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
