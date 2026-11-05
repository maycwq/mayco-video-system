# tipografia

texto, nos reels, é direção. ele decide o que fica, em que ordem e com que peso. esta seção cobre famílias, papéis, comportamento no tempo e os cuidados técnicos que a escolha de família traz.

## famílias usadas, e por quê

| família | onde | papel | evidência |
|---|---|---|---|
| Bootzy TM | REELS/02, 04, 05, 07, estudos do 08 | hook, legenda, texto editorial, rótulo, decisão | [EV-R02-15], [EV-R04-13], [EV-R05-06], [EV-R07-04], [EV-R08-07] |
| Boogaloo | versão cinética do bass persuades | rascunho, substituída por Bootzy na V3 | [EV-R08-01], [EV-R08-02] |
| SF Pro | tweets do REELS/05 | fidelidade ao template de interface | [EV-R05-06] |
| Bricolage Grotesque e Instrument Sans | REELS/09 | identidade do jogo | [EV-R09-02] |
| Barlow Condensed Black | REELS/10 | série tipográfica própria | [EV-R10-02] |

Bootzy é a voz do mayco quando ele fala em primeira pessoa sobre o que faz, e é a família mais presente. mas o acervo já usa outras quando o objeto tem identidade própria (o jogo) ou quando a interface exige a fonte do sistema (tweets). a regra que isso sugere: a família vem de quem está falando no quadro. o mayco fala em Bootzy; o jogo fala na fonte do jogo; o Twitter fala em SF Pro [EV-REQ-03] (DEC-11).

## os papéis do texto

### hook escrito

- aparece nos primeiros segundos, junto da fala ou no lugar da legenda [EV-R04-03].
- pode reescrever a fala como manchete [EV-R07-14].
- empilhado, com quebras pelo sentido, e uma palavra maior ou em cor quando ela é o argumento: "app" no REELS/02, "margem" e "preço." no REELS/04 [EV-R02-09], [EV-R04-14].
- palavra por palavra no tempo em que é dita [EV-R02-10].

### legenda

- palavra por palavra, centralizada embaixo, com o tempo do SRT revisado [EV-R02-15].
- cor ajustada ao fundo de cada beat, não fixa: preta no claro, branca no escuro, cor quando o fundo é tela de produto [EV-IG-04].
- termos compostos ficam inteiros num caption ("walk of fame", "bass persuades") [EV-R07-08].
- some quando outro texto já carrega a fala. no REELS/04 a decisão em tela substitui a legenda; no REELS/09 o texto editorial faz esse papel o vídeo inteiro [EV-R04-05], [EV-R09-01].

### texto editorial

- uma frase-tese que fica enquanto a fala desenvolve [EV-R02-11].
- vive numa superfície própria (o teal do REELS/02), longe da legenda.

### rótulo

- uma palavra presa a um objeto, como etiqueta [EV-R02-12].

### decisão ou lista

- um item por vez, no tempo da fala, cada um com um gesto curto [EV-R04-05].
- hierarquia por atenuação: o item anterior cai para 0,82 de opacidade quando o próximo entra; um acento de cor só no item que pesa [EV-R04-05], [EV-R04-14].

## convivência entre papéis

o REELS/02 mostra o problema: em ~18,6 s a legenda grande e branca cai sobre o texto editorial na mesma família e cor [EV-IG-05]. regras para evitar:

- quando há texto editorial na tela, a legenda muda de lugar, de tamanho ou some naquele trecho;
- legenda e texto editorial não usam a mesma combinação de cor e tamanho no mesmo beat;
- se o texto editorial diz a frase que está sendo falada, ele é a legenda daquele trecho.

ver FAL-09.

## comportamento no tempo

- **entrar**: pequeno deslocamento (18 px no hook refinado do REELS/02), opacidade, assentamento curto. a série do REELS/10 escreve a mesma coisa como regra: entradas de 18 a 22 px, pequeno overshoot, assentamento [EV-R02-09], [EV-R10-01] (DEC-05).
- **permanecer**: hold. o texto parado é lido; o texto que se mexe é olhado.
- **transformar**: recuo do bloco inteiro quando a frase termina (escala 0,82 no hook do REELS/02), atenuação quando outro item entra [EV-R02-09], [EV-R04-05].
- **sair**: corte ou recuo curto. sair voando chama atenção para a saída.
- **música**: na edição musical o texto pode ser o corpo da música, com escala extrema e recorte, porque não há fala para competir [EV-R08-07].

a versão anterior do hook do REELS/02 fazia o contrário: cada palavra viajava até 650 px e se espalhava depois [EV-R02-09]. a refinada é mais simples e mais legível. ver FAL-13.

## medidas

o acervo não tem tabela de tamanhos fixos, e este repositório não cria uma. valores observados servem de referência de escala, não de regra:

- PUNCH do REELS/07 em Bootzy entre 72 e 92 px num quadro de 1440x1080 [EV-R07-04];
- legendas do REELS/07 em Bootzy 48 px no 4:3 e 53 px no 9:16 [EV-R07-08];
- palavras do REELS/09 em torno de 120 a 130 px num quadro de 1080x1920 [EV-R09-03];
- palavras dos estudos musicais de 105 a 430 px na versão cinética [EV-R08-01].

o critério real: legível na tela do celular durante o tempo em que a palavra fica no quadro.

## Bootzy no render

Bootzy é proprietária e não sobrevive bem a todo pipeline de render. o acervo resolveu de três jeitos: glifos vetoriais com mestres ocultos marcados `do not export`, componentes locais por palavra num frame `RENDER-SAFE`, e bancos próprios de acentos e pontuação [EV-R02-15], [EV-R04-13], [EV-R08-09] (DEC-07). ainda sobram camadas pedindo troca para Bootzy [EV-R04-13], [EV-R05-06]. ver FAL-04.

consequências práticas:

- texto em Bootzy no render final vira forma, não fonte viva;
- acento e pontuação precisam ser conferidos em resolução cheia;
- a fonte não pode ir para o repositório nem para qualquer lugar público [EV-REQ-04].

## sinais de tipografia genérica

- a mesma família, tamanho e cor para hook, legenda e texto editorial;
- texto centralizado em caixa com fundo translúcido em todo beat;
- animação de entrada igual para toda palavra, independente do peso;
- frase longa em tela repetindo a fala inteira;
- destaque em várias palavras da mesma frase.

ver também: [escrita](../metodo/escrita.md), [motion](motion.md).
