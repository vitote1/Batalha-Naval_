Batalha Naval

Desenvolvimento de um jogo de Batalha Naval utilizando a linguagem Python.

O jogo foi desenvolvido para ser executado exclusivamente pelo terminal. Para iniciar, basta executar o arquivo "main.py", que contém o fluxo principal da aplicação e controla o funcionamento do jogo.

Representação do mapa

Durante o jogo, são utilizados os símbolos "H", "X" e "~" para representar o estado das casas do tabuleiro:

- "H" (Hit) — indica que um navio foi atingido.
- "X" — indica que o jogador realizou um ataque, mas não atingiu nenhum navio.
- "~" — representa o mar e uma posição que ainda não foi atingida.

Os navios também possuem símbolos próprios:

- "E" — Encouraçado.
- "P" — Porta-Aviões.

Vidas

Cada jogador começa com 12 vidas, correspondentes à quantidade total de posições ocupadas pelos seus navios.

Posicionamento dos navios

O posicionamento dos navios é realizado livremente pelo jogador. Para posicionar uma embarcação, o jogador informa:

1. A posição inicial.
2. A direção na qual o navio será colocado.

Por exemplo:

Posição inicial: A1
Direção: baixo

Dependendo do tamanho do navio, ele poderá ocupar:

A1
A2
A3
A4

O sistema também verifica se o navio está dentro dos limites do tabuleiro e se não ocupa uma posição que já esteja sendo utilizada por outra embarcação.

Frota

Cada jogador possui quatro navios:

- 2 Encouraçados ("E") — cada um ocupa 2 posições.
- 2 Porta-Aviões ("P") — cada um ocupa 4 posições.

Assim:

2 × 2 = 4 posições
2 × 4 = 8 posições

Total = 12 posições

Por esse motivo, cada jogador começa com 12 vidas.

Jogadores e estatísticas

Cada jogador é identificado por seu nome.

As estatísticas são armazenadas entre as partidas. Caso um jogador participe de outra partida utilizando o mesmo nome, seus novos dados são somados aos dados anteriores.

Dessa forma, o sistema mantém um histórico acumulado de informações como:

- número de partidas;
- número de jogadas;
- número de acertos;
- aproveitamento.

Os dados são persistidos em arquivos JSON, permitindo que sejam mantidos mesmo depois que o programa seja encerrado.

Computador

O jogo também possui um adversário controlado pelo computador.

Para realizar seus ataques, o computador utiliza uma estratégia que combina escolha aleatória e busca por posições vizinhas.

Inicialmente, o computador escolhe casas aleatórias do tabuleiro. Quando consegue acertar um navio, ele passa a priorizar as casas vizinhas à posição atingida, tentando encontrar as outras partes da embarcação.

Por exemplo:

      C4
       |
B5 — C5 — D5
       |
      C6

Caso o computador acerte "C5", ele passa a considerar as posições próximas como possíveis partes do mesmo navio.

Quando consegue identificar a direção do navio através de acertos consecutivos, ele pode continuar os ataques naquela direção para tentar destruí-lo.

Os navios do computador também são posicionados automaticamente no início da partida, utilizando posições e direções geradas aleatoriamente, respeitando os limites e as posições já ocupadas no tabuleiro.

Sistema de turnos

O jogador que consegue acertar um navio recebe o direito de realizar outro ataque.

Esse comportamento continua até que o jogador erre.

Por exemplo:

Jogador 1 → acerta
Jogador 1 → acerta
Jogador 1 → acerta
Jogador 1 → erra

Jogador 2 → começa sua vez

O erro encerra a sequência de ataques daquele jogador.

As rodadas são consideradas concluídas quando ambos os jogadores terminam suas respectivas sequências de ataques, ou quando um dos jogadores perde todas as suas vidas.

Replay

O sistema possui um mecanismo de Replay, que registra as jogadas realizadas durante a partida.

São armazenadas informações como:

- rodada;
- jogador que realizou o ataque;
- jogador alvo;
- coordenada atacada;
- resultado do ataque.

O replay é salvo em formato JSON e pode ser consultado posteriormente pelo menu do jogo.

Menu

O jogo possui um menu principal pelo qual o jogador pode acessar as funcionalidades disponíveis, incluindo:

- iniciar uma partida;
- escolher entre Jogador x Jogador e Jogador x Computador;
- visualizar o replay da última partida;
- visualizar as estatísticas;
- encerrar o programa.

Execução

Para executar o jogo, basta clonar o repositório e executar:

python main.py

O projeto utiliza somente recursos da linguagem Python e funciona através do terminal, não sendo necessário utilizar uma interface gráfica.

Repositório

GitHub:

https://github.com/vitote1/Batalha-Naval_.git

Vídeo demonstrativo

Vídeo demonstrativo temporário:

https://youtu.be/TEB6zbYxaQ0

O vídeo foi gravado temporariamente no computador de um colega devido à indisponibilidade do meu computador no momento da gravação.