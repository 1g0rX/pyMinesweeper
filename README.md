# 🧩 Minesweeper (Campo Minado) — User Manual

This is a simple guide for the installation, execution, and gameplay of the **Minesweeper** - game developed in Python and terminal-based.

---

## 📁 Index

* [English Version](#english-version)

  * [Requirements](#requirements)
  * [Setup and Execution](#setup-and-execution)
  * [Game Options](#game-options)
  * [Game Interface](#game-interface)
  * [Final Notes](#final-notes)
* [Versão em Português](#versão-em-português)

  * [Requisitos](#requisitos)
  * [Instalação e Execução](#instalação-e-execução)
  * [Opções do Jogo](#opções-do-jogo)
  * [Interface do Jogo](#interface-do-jogo)
  * [Notas Finais](#notas-finais)

---

## 🇬🇧 English Version

### Requirements

> [!NOTE]
> Before you begin, ensure you have **Python 3** installed on your system.
> Check by running `python --version` or `python3 --version` in your terminal.

* **Python 3.x**
* A **command-line terminal** to run the game.

---

### Setup and Execution

#### Clone the repo

Clone the repo by running the following in the terminal:

```bash
git clone https://github.com/1g0rX/pyMinesweeper.git
cd pyMinesweeper
```

#### Starting the Game

1. Run the command:

   ```bash
   python3 pyMinesweeper.py
   ```
2. The game will prompt for the board settings:

   * Number of rows (3–10)
   * Number of columns (3–10)
   * Number of mines

#### Ending the Game

You can end the game session in three ways:

* **Quitting** — select option `0` in the main menu.
* **Winning** — when all mines are correctly marked.
* **Losing** — when opening a cell containing a mine.

---

### Game Options

1. **Board Configuration**
   Define the battlefield size:

   * Rows: 3–10
   * Columns: 3–10
   * Mines: number of hidden bombs

2. **In-Game Actions**

   * `1. Mark as mine` — places an **M** marker on a suspected mine.
   * `2. Open coordinates` — reveals a cell (if it’s a bomb, the game ends).
   * `0. Exit` — ends the game.

---

### Game Interface

#### Initial Setup Screen

```
Number of lines (min 3 and max 10): 5
Number of columns (min 3 and max 10): 5
Number of mines: 4
Bombs allocated!
```

#### Main Game Screen

```
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
```

#### Defeat and Victory Screens

At the end, the full board is revealed, showing all mine locations.

---

### Final Notes

#### Final Thoughts

This project is a **fully functional Minesweeper clone**, developed for a **terminal environment** in Python.
It provides a solid **logical challenge** and encourages **deductive reasoning**.

#### Limitations and Known Issues

> [!WARNING]
>
> ~~* **Input Validation:** The program does not handle non-numeric inputs. Invalid inputs (letters, symbols) may cause a runtime error.~~
> * **Text Interface:** No graphical user interface (GUI) is implemented.
> * **Flood Fill:** Cells with `0` do not trigger automatic opening of surrounding safe cells.

---

## 🇧🇷 Versão em Português

### Requisitos

> [!NOTE]
> Antes de começar, certifique-se de que você possui o **Python 3** instalado.
> Verifique executando `python --version` ou `python3 --version` no terminal.

* **Python 3.x**
* Um **terminal de linha de comando** para executar o jogo.

---

### Instalação e Execução

#### Clonando o repositório

Clone o repositório rodando os seguintes comandos:

```bash
git clone https://github.com/1g0rX/pyMinesweeper.git
cd pyMinesweeper
```

#### Como Iniciar o Jogo

1. Execute:

   ```bash
   python pyMinesweeper.py
   ```
2. O jogo pedirá as configurações iniciais:

   * Número de linhas (3–10)
   * Número de colunas (3–10)
   * Número de minas

#### Como Terminar o Jogo

O jogo pode ser encerrado de três formas:

* **Saindo voluntariamente:** opção `0` no menu principal.
* **Vencendo:** ao marcar corretamente todas as minas.
* **Perdendo:** ao abrir uma célula que contém uma mina.

---

### Opções do Jogo

1. **Configuração do Tabuleiro**

   * Linhas: 3–10
   * Colunas: 3–10
   * Minas: quantidade de bombas escondidas

2. **Ações em Jogo**

   * `1. Marcar como mina` — coloca um **M** onde o jogador suspeita haver uma mina.
   * `2. Abrir coordenadas` — revela o conteúdo da célula.
   * `0. Sair` — encerra a partida.

---

### Interface do Jogo

#### Tela de Configuração Inicial

```
Number of lines (min 3 and max 10): 5
Number of columns (min 3 and max 10): 5
Number of mines: 4
Bombs allocated!
```

#### Tela Principal do Jogo

```
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
```

#### Telas de Derrota e Vitória

Ao final, o jogo revela todas as minas no tabuleiro para conferência.

---

### Notas Finais

#### Considerações Finais

Este projeto é uma implementação funcional do **Campo Minado clássico**, totalmente em Python, para execução no terminal.
Oferece uma experiência sólida de **desafio lógico e dedução**.

#### Limitações e Problemas Conhecidos

> [!WARNING]
>
> ~~* **Validação de Entrada:** Entradas não numéricas podem causar erro e encerrar o programa.~~
> * **Interface de Texto:** Não há interface gráfica (GUI).
> * **Abertura em Massa (Flood Fill):** Não implementado — células com `0` não abrem as vizinhas automaticamente.

