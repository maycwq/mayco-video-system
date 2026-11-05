# REELS/04 · o custo subiu, o preço não

## identificação

- **assunto**: na gestão da olue, um material ficou mais caro; o sistema recalcula custo e margem, mas o preço não muda sozinho, porque decidir o que fazer continua sendo humano.
- **formato publicado**: 4:3, 31,733 s, publicado em 25/08; o Instagram entregou 960x720 a partir de um master 1440x1080 [EV-IG-03].
- **stages no Figma**: horizontal `398:2964`, 4:3 `831:6017`, vertical `1428:10045`, mais treze frames TEMP de diagnóstico [EV-R04-01].
- **fonte**: take contínuo de 31,667 s com áudio [EV-R04-02].

## o argumento

> um aumento pequeno pode comer a sua margem antes de você sequer mexer no preço. e foi isso que aconteceu quando eu registrei uma compra nova na marca de objetos pra casa que eu tô construindo. o material subiu, o custo e a margem reagiram na hora e o preço continuou exatamente onde estava. eu deixei assim de propósito, porque o custo maior não responde se eu devo cobrar mais, mudar a peça, rever o processo ou simplesmente aceitar outra margem. e eu vou continuar mostrando essas decisões enquanto eu construo essa marca. talvez alguma dessas coisas também te ajude por aí.

a lógica que o vídeo precisa deixar: compra registrada, custo e margem reagem, preço parado, decisão humana. o relato preparatório chegou à mesma cadeia [EV-PREP-02]; as camadas do Figma confirmam, porque cada bloco de mídia tem nome de papel nessa cadeia [EV-R04-03].

## anatomia por beat

| tempo | estado do quadro | por quê | evidência |
|---|---|---|---|
| 0 a 4,45 s | talking head cheio com o argumento tipográfico empilhado ao lado; uma tela da gestão aparece como fantasma | o hook é a tese; a tela fantasma promete a prova | [EV-R04-02], [EV-R04-14] |
| 4,45 a 5,05 s | a pessoa encolhe para 0,66 e vira janela no desk | "foi isso que aconteceu": sai a tese, entra o lugar | [EV-R04-02] |
| 5,18 a 6,1 s | ponteiro real arrasta o Spotify para abrir espaço | arrumar a mesa antes de trabalhar | [EV-R04-09] |
| 5,7 a 9,39 s | modal de registrar compra da gestão | "registrei uma compra nova" | [EV-R04-03] |
| 9,39 a 9,86 s | o quadro mergulha no modal (zoom 2,12) e a tela cheia nasce de dentro dele | o registro leva ao efeito | [EV-R04-04] |
| 9,86 a 15,92 s | compra salva, novo custo, margem caindo, preço parado, com push-in lento | evidência principal | [EV-R04-03] |
| 15,92 a 18,55 s | ficha e precificação do produto | "o custo maior não responde..." | [EV-R04-03] |
| 18,55 a 25,1 s | tinta preta cobre tudo; quatro opções entram uma por vez no tempo da fala | a decisão é humana, então o software sai | [EV-R04-05], [EV-R04-06] |
| 25,22 a 28,62 s | catálogo com alerta | "vou continuar mostrando essas decisões" | [EV-R04-03] |
| 27 a 31,67 s | a pessoa volta cheia e faz um push-in lento até o fim | fechamento pessoal | [EV-R04-02] |

## a sequência de decisão

é o trecho mais estudável do vídeo. quatro opções, quatro entradas curtas e diferentes entre si: a primeira vem 42 px da esquerda, a segunda faz um pop curto, a terceira sobe 50 px, a quarta vem da direita com um leve encolhimento. quando a próxima entra, a anterior cai para opacidade 0,82, então a hierarquia muda sem nada sair do lugar [EV-R04-05]. no publicado, só a última opção fica em laranja [EV-R04-14].

cada opção entra no instante em que é dita, e a última entra meia palavra antes, já em "simplesmente", o que prepara o peso dela [EV-R04-06].

o fundo é preto sólido. o blackdetect marca o primeiro segundo dessa sequência como preto, porque só "cobrar mais" ocupa a tela. é intencional, e a ferramenta de QA aceita intervalos de preto previstos para não gerar alarme falso [EV-IG-06].

por que preto e não a ficha do produto atrás: a decisão é exatamente a parte que o sistema não faz. tirar o software do quadro é o argumento visual da frase "a decisão continua sendo com a gente".

há um resto curioso: a mídia da ficha continua fazendo pans e zoom sincronizados com as opções, por baixo da tinta, onde ninguém vê [EV-R04-07]. a leitura mais provável, com baixa confiança, é que um tratamento anterior mostrava as opções sobre o software e a tinta entrou depois [EV-R04-08]. ver FAL-10.

## ambiente e interfaces

é o caso mais literal do princípio do ambiente. gravações reais da gestão da olue, janelas e controles do macOS, ponteiro do sistema, Spotify montado com componentes reais da biblioteca de media players [EV-R04-03], [EV-R04-09], [EV-LIB-02]. o ponteiro arrasta a janela e a janela acompanha o ponteiro no mesmo caminho [EV-R04-09].

as transições são causais. a câmera não corta da lista para a ficha: ela entra no modal e a próxima tela sai de dentro dele [EV-R04-04].

## vocabulário do design system

os blocos de mídia carregam códigos do catálogo do design system: `MED-11/18`, `T04 TWO ACTIVITIES`, `T03 FULL SCREEN`, `MIC-04`, `MES-10` [EV-R04-03]. é o trabalho que mais usa o catálogo como vocabulário. nos trabalhos seguintes os códigos desaparecem dos nomes [EV-DS-03]. o catálogo é descrito no [inventário](../fontes/inventario.md).

## engenharia

- o stage 4:3 mantém o desk de 1920 de largura deslocado em -240 dentro do quadro de 1440: o ambiente é cortado, mas hook, legendas e decisão foram reposicionados para o 4:3 [EV-R04-02].
- o wallpaper tem um keyframe linear de 2 px na largura ao longo de 11,47 s, que parece correção de borda [EV-R04-10].
- cerca de 80 componentes locais, um por palavra de legenda, guardados num frame oculto `RENDER-SAFE`, e textos editáveis esperando troca para Bootzy [EV-R04-13]. ver FAL-04.
- treze frames TEMP isolam subárvores para descobrir o que quebrava na exportação: raiz nova, raiz redimensionada, só mídia, só desk, só Spotify, só wallpaper, e no vertical combinações de desk, mídia, wallpaper, Spotify e atmosfera [EV-R04-12]. o sintoma original não está registrado. ver FAL-05.

## duração

fonte de 31,667 s, MP4 citado de 31,744 s, publicado com 31,733 s de vídeo e 31,743 s de áudio [EV-ENG-03]. são cerca de 2 quadros. a hipótese mais simples é arredondamento de quadro e preenchimento do encoder de áudio. não aparece como defeito, e a [qa de render](../engenharia/qa-de-render.md) tem tolerância configurável para isso.

## versão vertical

o vertical repete a estrutura do horizontal com os deslocamentos da fonte multiplicados por 0,32 [EV-R04-11]. é adaptação por escala, não recomposição por beat. os seis frames `TEMP QA · 9:16` sugerem que essa versão deu trabalho para renderizar [EV-R04-12]. não foi publicada.

## aprovações e pendências

- **resultado**: publicado em 4:3 [EV-IG-03].
- **direção e implementação**: não verificáveis.
- **pendente**: sintoma que motivou os TEMP de exportação; se a ficha sob a tinta era intencional; vertical não publicado.

## o que transfere

- quando a frase sai do sistema e entra na decisão de alguém, o quadro pode sair do sistema também (DEC-06).
- opções faladas viram tipografia no tempo da fala, com hierarquia por atenuação das anteriores e um acento só na última (DEC-05).
- transição que nasce de dentro do elemento anterior conta a causalidade melhor que corte seco.
- diagnóstico de render por isolamento de camadas (ver [qa de render](../engenharia/qa-de-render.md)).

## o que não transfere

- fundo preto como superfície de decisão funciona porque o resto do vídeo é claro e cheio de interface. num vídeo já escuro, a mudança não seria percebida.
- quatro entradas diferentes para quatro opções funcionam porque são quatro caminhos distintos. numa lista de itens equivalentes, variar o gesto de cada um sugere diferença que não existe.
- o laranja da última opção marca a escolha mais desconfortável da lista. não é cor de destaque padrão.

## fontes

S-FIG-PRINCIPAL (página `370:12343`), S-IG-C, S-QA-LOCAL, S-PREP.
