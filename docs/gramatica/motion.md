# motion

## a pergunta que decide

todo movimento responde a uma de quatro perguntas. se não responde a nenhuma, sai.

| tipo | pergunta | exemplos no acervo |
|---|---|---|
| semântico | que ação está acontecendo? | clicar no botão amarelo e a janela minimizar [EV-R02-05]; arrastar uma janela com o cursor [EV-R07-09]; mergulhar no modal [EV-R04-04] |
| funcional | para onde olhar agora? | foco entre janelas por opacidade e escala [EV-R02-07]; atenuar a opção anterior [EV-R04-05] |
| editorial | que mudança de ideia está acontecendo? | o desktop quebra e o teal assume [EV-R02-11]; a tinta preta entra na decisão [EV-R04-05] |
| expressivo | qual é a energia deste momento? | o carimbo elástico das palavras do jogo [EV-R09-03]; a palavra gigante que vira corpo do grave [EV-R08-03] |

um mesmo gesto pode ser de tipos diferentes conforme o contexto. um zoom lento numa tela de dados é funcional (olhe isso); o mesmo zoom num rosto no fim do vídeo é editorial (estamos fechando) [EV-R04-02].

## vocabulário observado

- **entrada curta**: deslocamento pequeno, opacidade, assentamento. 18 px em 0,18 s no hook do REELS/02; 10 a 18 px com escala 0,96 para 1 no PUNCH do REELS/07; 18 a 22 px com pequeno overshoot no REELS/10 [EV-R02-09], [EV-R07-04], [EV-R10-01].
- **hold**: o estado padrão. os keyframes usam HOLD o tempo todo, e boa parte do vídeo é coisa parada sendo lida [EV-ENG-02].
- **corte seco por HOLD**: troca instantânea de opacidade para cortes de cor e entrada de imagens em sequência [EV-R09-04], [EV-R07-10].
- **ease out padrão**: curva (0, 0, 0.58, 1) nas entradas; ease in and out nas derivas ambientes [EV-ENG-02].
- **clique**: compressão rápida de escala (0,84 a 0,92) no cursor [EV-R02-05], [EV-R07-09].
- **origem e destino coerentes**: a janela sai do dock e volta para ele; a tela seguinte nasce de dentro do modal [EV-R02-07], [EV-R04-04].
- **push-in lento**: 1 para 1,03 numa prova, 1 para 1,065 no rosto do fim [EV-R04-02].
- **respiração ambiente**: efêmeras derivam poucos pixels e pouco mais de um grau em ciclos de alguns segundos; luzes do wallpaper em ciclos de mais de 20 s [EV-R02-16], [EV-R07-04].
- **responsivo**: a janela da pessoa muda de proporção para acompanhar o conteúdo [EV-R07-07].
- **squash e stretch curto**: deformação não uniforme que passa do ponto e assenta, só no REELS/09, onde o assunto é jogo [EV-R09-03].

## quando o movimento mais simples ganhou

dois casos no próprio arquivo:

1. **hook do REELS/02**. o tratamento anterior trazia palavras de até 650 px de distância, com escala e espalhamento. o refinado só sobe 18 px. o refinado ficou, e a sincronia com a fala ficou exata [EV-R02-09], [EV-R02-10]. ver FAL-13.
2. **bass persuades**. a versão cinética fazia toda palavra entrar girando até 35°, voar até 760 px e crescer até 2,35x. a V3 e o rebuild trocaram efeito por função compositiva e esconderam elementos [EV-R08-01], [EV-R08-03]. ver FAL-02.

nos dois, o problema não era "muito movimento" em abstrato. era movimento igual para tudo e sem relação com o que estava sendo dito ou tocado.

## rotação, bounce, spring e fade

nenhum desses está proibido. o acervo usa:

- rotação de 83 a 90 graus em colunas de letras, que viram eixo da composição [EV-R08-02];
- rotação pequena (3 a 12 graus) para dar peso a palavras nos estudos musicais [EV-R08-03];
- rotação de 3 a 5 graus que se endireita na entrada do carimbo do REELS/09 [EV-R09-03];
- spring na versão cinética, onde virou vício, e no carimbo do jogo, onde combina [EV-R08-01], [EV-R09-03].

o critério é o mesmo para todos: o gesto precisa de um motivo no conteúdo e não pode se repetir igual em tudo.

## movimento e causalidade

- o cursor só aparece para executar uma ação, e o objeto acompanha o cursor no mesmo caminho [EV-R04-09], [EV-R07-09] (DEC-04).
- o objeto entra de onde faria sentido vir: do dock, da borda mais próxima, de dentro do elemento anterior.
- movimento que acontece por baixo de uma cobertura é invisível; se não serve para o render, sai do arquivo [EV-R04-07]. ver FAL-10.

## sinais de motion sem intenção

- toda palavra entra do mesmo jeito, com o mesmo exagero;
- rotação em tudo;
- elementos que flutuam no centro do quadro chamando atenção;
- transições iguais entre beats de natureza diferente;
- cursor que passeia sem clicar;
- o movimento continua quando a fala parou para respirar.

ver também: [tipografia](tipografia.md), [interfaces](interfaces.md), [áudio e tempo](audio-e-tempo.md).
