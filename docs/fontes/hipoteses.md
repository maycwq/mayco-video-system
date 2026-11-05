# revisão das hipóteses preparatórias

o pedido trouxe seis hipóteses da investigação anterior, para testar e não para obedecer. abaixo, a classificação de cada uma, a evidência que decidiu e o que mudou no repositório por causa disso. depois, o que apareceu sem estar previsto.

## A · o ambiente faz parte do argumento

**classificação: reformulada.**

confirmado nos vídeos sobre software: desktop, apps e gravações reais, com nomes de camada exigindo fidelidade [EV-R02-06], [EV-R04-03], [EV-R07-08]. mas o acervo também tem vídeos sem nenhum desktop, que seguem a mesma lógica com outro ambiente: o REELS/05 cria placas editoriais para uma ideia [EV-IG-08], o REELS/09 usa o jogo [EV-R09-02], os estudos musicais usam a música [EV-R08-06].

e o ambiente sai do quadro quando o argumento sai dele: teal no REELS/02, tinta no REELS/04 [EV-R02-11], [EV-R04-05].

formulação adotada: o ambiente é o lugar onde o assunto acontece; quando o argumento sai desse lugar, o quadro sai junto [EV-NOVA-01] (DEC-16). capítulo completo em [ambiente](../metodo/ambiente.md).

## B · a composição evolui com a ideia

**classificação: confirmada, com um acréscimo.**

o REELS/02 passa por pessoa, lugar, abstração, produto e pessoa; o REELS/04 por tese, lugar, prova, decisão e pessoa; o REELS/09 troca de estado a cada rodada [EV-R02-02], [EV-R04-03], [EV-R09-04]. o acréscimo: cada passagem tem uma causa visível no quadro (um clique, um nome dito, um mergulho no modal) [EV-R02-05], [EV-R04-04]. a evolução não é progressão estética; é causalidade.

## C · tipografia é direção, não decoração

**classificação: confirmada; a parte sobre Bootzy, reformulada.**

texto faz cinco papéis distintos (hook, legenda, editorial, rótulo, decisão), com hierarquia, tempo e cor próprios [EV-R02-09], [EV-R04-05], [EV-R02-12]. Bootzy domina os vídeos em que o mayco fala de si e do que faz, sempre convertida para forma render-safe [EV-R02-15], [EV-R04-13]. mas o REELS/09 não usa Bootzy, usa a tipografia do jogo [EV-R09-02], e os tweets do REELS/05 usam SF Pro por fidelidade [EV-R05-06]. a família vem de quem fala no quadro (DEC-11). falhas de glifo e acento existiram e foram contornadas [EV-R08-09] (FAL-04).

## D · movimento precisa de causalidade

**classificação: confirmada, com limites explícitos.**

cursor só para ações, objeto acompanhando o cursor, janelas entrando de onde viriam [EV-R02-05], [EV-R04-09], [EV-R07-09]. símbolos genéricos e movimento de efeito foram substituídos [EV-R02-12], [EV-R08-03]. os limites: há movimento expressivo legítimo (o carimbo elástico do jogo) [EV-R09-03] e movimento ambiente sem causa, mas tão discreto que não pede atenção (efêmeras e luzes) [EV-R02-16], [EV-R07-04]. o critério virou as quatro perguntas de [motion](../gramatica/motion.md).

## E · refinamento depende de validação real

**classificação: confirmada.**

o arquivo está cheio de instrumentos de validação: frames TEMP que isolam camadas para exportar [EV-R04-12], frame de QA só com o master [EV-R07-02], snapshots de QA em intervalos iguais [EV-R08-06]. e a validação desta investigação achou coisas que o editor não mostra: a efêmera fora do quadro no vertical [EV-R02-18], a música acima da fala no master [EV-R07-12], o movimento escondido sob a tinta [EV-R04-07]. ganhou ferramenta própria: [qa de render](../engenharia/qa-de-render.md).

## F · humor nasce da relação entre elementos

**classificação: parcialmente confirmada.**

os casos verificáveis são relacionais: deadpan no Figma [EV-R03-01], literalidade na avalanche de collabs [EV-R07-10], acúmulo nos tweets [EV-R05-04]. não dá para confirmar o que foi criticado ou aprovado em termos de humor, porque isso estava nas conversas. o design system tinha um catálogo de padrões de humor [EV-DS-01], e os vídeos usam pouco humor, sempre preso a uma frase.

## o que apareceu sem estar previsto

1. **os publicados são 02, 05 e 04**, não 07 e 09 [EV-IG-01], [EV-IG-02], [EV-IG-03]. o REELS/05, fora da lista do pedido, é o contraexemplo mais forte à leitura "o mayco usa desktop" e ganhou estudo próprio.
2. **havia um sistema anterior de padrões para IA** no design system, com códigos usados no REELS/04 [EV-DS-02], [EV-R04-03]. o próprio arquivo mostra a passagem para direção individual [EV-R10-02], [EV-DS-03]. esta base registra o catálogo como vocabulário, não como roteiro.
3. **as versões do REELS/07 são variantes de hook escrito**, não de edição [EV-R07-04].
4. **o tempo do REELS/07 foi resolvido num master mixado**, e as pausas viraram quadro congelado dentro dele [EV-R07-02], [EV-R07-15]. o relato de BASE 47,600 s e FINAL 60,650 s descreve uma etapa anterior; a duração atual é 59,307 s [EV-R07-01].
5. **música 10 a 13 dB acima da fala** no master do REELS/07 [EV-R07-12].
6. **o REELS/09 não tem camada de legenda nem Bootzy** [EV-R09-01], [EV-R09-02].
7. **as adaptações verticais usam métodos diferentes**: recomposição no 02, 03 e 07, escala proporcional no 04, e um elemento perdido no 02 [EV-R02-17], [EV-R03-02], [EV-R04-11], [EV-R02-18].
8. **a placa preta do REELS/04 dispara detector de preto** [EV-IG-06], e a transcrição automática erra nomes [EV-IG-07]: QA automático precisa de declaração de intenção.
9. **a cronologia pelos ids** mostra o 4:3 virando formato de publicação entre 15 e 23 de agosto [EV-CRONO-01].
10. **o publicado do REELS/02 tem 1916x1078** [EV-IG-01], com causa não identificada [EV-ENG-04].

## correções feitas no repositório por causa desta revisão

- o princípio do ambiente foi reescrito em vez de copiado (DEC-16).
- Bootzy aparece como voz do mayco, não como regra (DEC-11, DEC-07).
- a gramática de motion trocou proibições por quatro perguntas.
- o tempo ganhou documento técnico próprio e ferramenta de mapa ([tempo e playback](../engenharia/tempo-e-playback.md)).
- aprovação ganhou três níveis em `data/decisoes.toml`.
