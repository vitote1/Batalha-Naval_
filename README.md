# Batalha-Naval_
Desenvolvimento de um jogo na linguagem python
No jogo utilizei H, X e ~ como variáveis  que demonstram o que ocorreu no mapa.
    H = hit, algum navio foi acertado;
    X = perdeu, não atingiu um navio;
    ~ = mar, simbolizando o mar

Para jogar basta rodar o main.py, nele está configurado todo o sistema do jogo, e o como ele deve se comportar

Cada jogador tem 12 vidas, 1 para cada parte dos barcos

Utilizado somente o terminal

Para posicionar os navios, escolhi deixar de livre-arbítrio para o player, em que ele digita a posicao inicial + sua direção
Por exemplo: posição inicial = A1, direção = baixo ===> A1, A2, A3, A4 (a depender do navio)

Cada player tem 4 navios, 2 encouraçados(com simbolo E no mapa) que ocupa 2 posições, e 2 porta-aviões(com simbolo P no mapa) que ocupa 4 posições

Utilizei nome para identificar jogadores, nas estatisticas, caso o jogador de outra partida possua o mesmo nome, seus dados se juntarão, 
atualizando os dados

O computador gera casas aleatórias + casas vizinhas à essa, e por probabilidade, define a posição de seus navios
Ao acertar um navio seu, o computador será direcionado à escolher uma casa vizinha à essa que você foi atingido, a fim de derrubar a outra
parte do navio

Caso o jogador acerte a casa em que esteja um navio, ele poderá jogar novamente até que ele erra, e isso não avança a rodada, já que as rodadas
são definidas quando ambos concluem suas jogadas, ou seja, quando ambos errarem ou algum morrer

Link do github: https://github.com/vitote1/Batalha-Naval_.git

Link do video no youtube: https://youtu.be/TEB6zbYxaQ0
Video ficou sem audio, além de que nao estava com meu Pc, pois ele queimou, então para gravar usei um note do meu colega,
