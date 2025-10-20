Campo Minado em Python: Manual do Usuário

Este documento serve como um guia completo para a instalação, execução e jogabilidade do jogo Campo Minado desenvolvido em Python.

Índice

English Version

Requirements

Setup and Execution

Game Options

Game Interface

Final Notes

Versão em Português

Requisitos

Instalação e Execução

Opções do Jogo

Interface do Jogo

Notas Finais

<a name="english-version"></a>

English Version

Requirements

[!NOTE]
Before you begin, ensure you have Python 3 installed on your system. You can check this by running python --version or python3 --version in your terminal.

Python 3.x

A command-line terminal to run the game.

Setup and Execution

Starting the Game

Navigate via the terminal to the directory where the minesweeper_refactored.py file is located.

Run the following command:

python minesweeper_refactored.py


The game will start and prompt you for the initial board settings (rows, columns, and number of mines).

Ending the Game

You can end the game session in three ways:

Quitting: In the main menu, select option 0 and press Enter.

Winning: The game ends automatically when you correctly mark all mine locations.

Losing: The game ends automatically when you open a coordinate that contains a mine.

Game Options

The system provides the following options to the user:

1. Board Configuration

When starting, you will define the size of the battlefield:

Number of rows: A value between 3 and 10.

Number of columns: A value between 3 and 10.

Number of mines: The quantity of bombs to be hidden on the map.

2. In-Game Actions

During each turn, the following menu will be displayed:

1. Mark as mine: Allows the player to place an M marker on a coordinate where they suspect a mine exists.

2. Open coordinates: Reveals the content of a cell. If it's a bomb, the game ends. Otherwise, it will display a number indicating how many mines are in the 8 neighboring squares.

0. Exit: Ends the game immediately.

Game Interface

Initial Setup Screen

The first user interaction, where the board is configured.

Number of lines (min 3 and max 10): 5
Number of columns (min 3 and max 10): 5
Number of mines: 4
Bombs allocated!


Main Game Screen

The main screen, displayed each turn, showing the current state of the minesweeper field.

   1  2  3  4  5
1 [ ][1][ ][ ][ ]
2 [ ][1][ ][ ][ ]
3 [M][1][ ][ ][ ]
4 [1][1][ ][ ][ ]
5 [ ][ ][ ][ ][ ]


1. Mark as mine
2. Open coordinates
0. Exit
Option:


Defeat and Victory Screens

Upon losing or winning, the game displays the final state of the board, revealing all mine locations for review.

Final Notes

Final Thoughts

This project is a functional implementation of the classic Minesweeper game, developed entirely in Python for a terminal environment. It offers a solid experience of logical challenge and deduction.

Limitations and Known Issues

[!WARNING]
Input Validation: The program does not handle non-numeric inputs (like letters). Providing invalid input may cause a runtime error and terminate the execution.

Text Interface: The game does not have a graphical user interface (GUI).

Flood Fill: The game does not implement the "flood fill" feature, where clicking on a cell with the number 0 automatically reveals all surrounding safe cells.

<a name="versão-em-português"></a>

Versão em Português

Requisitos

[!NOTA]
Antes de começar, certifique-se de que você tem o Python 3 instalado em seu sistema. Você pode verificar isso executando python --version ou python3 --version no seu terminal.

Python 3.x

Um terminal de linha de comando para executar o jogo.

Instalação e Execução

Como Iniciar o Jogo

Navegue pelo terminal até o diretório onde o arquivo minesweeper_refactored.py está localizado.

Execute o seguinte comando:

python minesweeper_refactored.py


O jogo será iniciado e solicitará as configurações iniciais do tabuleiro (linhas, colunas e número de minas).

Como Terminar o Jogo

Você pode terminar a execução do jogo de três maneiras:

Saindo voluntariamente: No menu principal, digite a opção 0 e pressione Enter.

Vencendo: O jogo termina automaticamente quando você marca corretamente a localização de todas as minas.

Perdendo: O jogo termina automaticamente quando você abre uma coordenada que contém uma mina.

Opções do Jogo

O sistema oferece as seguintes opções ao usuário:

1. Configuração do Tabuleiro

Ao iniciar, você definirá o tamanho do campo de batalha:

Número de linhas: Um valor entre 3 e 10.

Número de colunas: Um valor entre 3 e 10.

Número de minas: A quantidade de bombas que serão escondidas no mapa.

2. Ações em Jogo

Durante a partida, o seguinte menu será exibido a cada jogada:

1. Marcar como mina: Permite que o jogador coloque um marcador M em uma coordenada onde ele suspeita que exista uma mina.

2. Abrir coordenadas: Revela o conteúdo de uma célula. Se for uma bomba, o jogo acaba. Caso contrário, exibirá um número que indica quantas minas existem nos 8 quadrados vizinhos.

0. Sair: Encerra o jogo imediatamente.

Interface do Jogo

Tela de Configuração Inicial

A primeira interação do usuário, onde o tabuleiro é configurado.

Number of lines (min 3 and max 10): 5
Number of columns (min 3 and max 10): 5
Number of mines: 4
Bombs allocated!


Tela Principal do Jogo

Esta é a tela principal, exibida a cada turno, mostrando o estado atual do campo minado.

   1  2  3  4  5
1 [ ][1][ ][ ][ ]
2 [ ][1][ ][ ][ ]
3 [M][1][ ][ ][ ]
4 [1][1][ ][ ][ ]
5 [ ][ ][ ][ ][ ]


1. Mark as mine
2. Open coordinates
0. Exit
Option:
