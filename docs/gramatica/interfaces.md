# interfaces e ambientes digitais

quando o ambiente é software, a interface é ao mesmo tempo cenário e prova. esta seção trata de como reconstruir e transformar sem perder a coerência. a escolha de usar ou não uma interface está em [ambiente](../metodo/ambiente.md).

## fidelidade

o acervo trata fidelidade em três camadas:

1. **sistema**: componentes reais do macOS 26 da biblioteca comunitária para wallpaper, menu bar, dock, janelas, botões e ponteiro [EV-LIB-02]. comportamentos do sistema funcionam: indicador de app aberto acende, minimizar vai para o dock [EV-R02-06], [EV-R02-05].
2. **aplicativo**: conteúdo real dentro da janela. gravações de tela da gestão e da comunidade em video fill [EV-R04-03], [EV-R02-13]; Spotify com sidebar e barra superior reais e capas reais [EV-R07-08]; canvas real do Figma como imagem [EV-R02-14].
3. **proporção**: a gravação entra na proporção dela; os nomes repetem `source-proportional` e `timing preserved` [EV-R02-07], [EV-R07-08].

o que fica fora: interface que imita um tipo de app sem ser nenhum. o REELS/02 esconde um play "autoral genérico", uma nota "simbólica sem valor" e uma foto placeholder [EV-R02-12]. ver FAL-01.

uma nuance sobre bibliotecas: o teaser do REELS/02 se chama `REAL FIGMA UI3`, mas não usa o kit UI3; usa uma imagem do canvas real [EV-R02-14]. o kit UI3 entra de verdade só no REELS/03, onde a réplica do Figma precisava ser editável [EV-R03-01]. disponibilidade de componente não é uso.

## janelas

- entram de onde viriam: do dock, de fora do quadro, do lado de onde foram arrastadas [EV-R02-07].
- foco por opacidade e escala, não por troca brusca [EV-R02-07].
- empilhamento conta prioridade: a janela em foco fica na frente, as outras recuam.
- a janela da pessoa é uma janela como as outras: pode encolher, ser minimizada, crescer, mudar de proporção [EV-R02-05], [EV-R07-07].
- push-in lento numa janela é "olhe isso" [EV-R07-08].

## cursor

- só aparece para agir: clicar, arrastar, minimizar [EV-R02-07], [EV-R07-09].
- o clique é visível (compressão de escala curta) [EV-R02-05].
- o que é arrastado acompanha o cursor no mesmo caminho e nos mesmos tempos [EV-R04-09].
- some quando a ação termina.

cursor que passeia, que aponta sem clicar ou que se move separado do que ele supostamente arrasta quebra a leitura de causalidade (DEC-04).

## scroll e navegação

as gravações reais mostram scroll e navegação feitos de verdade. quando é preciso acelerar, acelerar a gravação ou cortar entre estados reais; não animar um scroll falso por cima de um print.

## preservar ou transformar

| situação | caminho | exemplo |
|---|---|---|
| a interface é a prova | preservar, recortar no essencial, segurar | evidência de custo e margem [EV-R04-03] |
| a interface é contexto | reduzir opacidade e escala, deixar na periferia | Spotify ambiente no REELS/04 [EV-R04-09] |
| a próxima tela nasce de um elemento | transformar com zoom para dentro | mergulho no modal [EV-R04-04] |
| a fala sai do software | tirar a interface do quadro | tinta preta na decisão [EV-R04-05] |
| a interface é referência cultural, não ferramenta | clonar e recolorir, nunca redesenhar | TV do REELS/05 [EV-R05-03] |
| conteúdo fictício num template real | marcar como ficção no arquivo e deixar a sátira legível | tweets do REELS/05 [EV-R05-04] |

## janelas sem continuidade

uma janela que aparece num lugar e no beat seguinte está em outro, sem movimento nem causa, parece erro de montagem. se ela precisa mudar de lugar, alguém a arrasta, ou ela sai e volta. se ela some, sai pelo caminho de onde veio.

## bibliotecas

o acervo tem catorze bibliotecas vinculadas, e só algumas aparecem nas edições [EV-LIB-01], [EV-LIB-02]. o [inventário](../fontes/inventario.md) lista o que cada uma tem e onde foi usada. nenhuma é obrigatória: biblioteca é estoque, não direção.

ver também: [ambiente](../metodo/ambiente.md), [motion](motion.md).
