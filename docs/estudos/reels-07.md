# REELS/07 · vocês conhecem o catálogo da miley?

## identificação

- **assunto**: com a nova era da miley chegando, mayco revisita o catálogo dela e cita música por música o que as pessoas esquecem, até chegar em bass persuades.
- **publicado**: não encontrado entre os reels acessíveis.
- **stages no Figma**: V01 `926:3698` (ORIGINAL), V02 `1194:2964`, V03 `1194:5604`, V04 `1194:8244`, V05 `1194:10884`, todos 1440x1080, e o vertical `1395:5529` [EV-R07-01].
- **duração atual**: 59,307 s em todas as versões [EV-R07-01].

## o que o relato dizia e o que o arquivo mostra

o relato preparatório descreve uma timeline com fonte BASE de 47,600 s, FINAL projetado de 60,650 s, inserções somando 13,050 s, camadas de PAUSE INSERTS e OVERLAYS, legendas com offset, e um render que continuava preto depois de ~47,7 s [EV-PREP-03].

o arquivo de hoje não tem nenhuma dessas camadas. todas as versões usam como fonte um único vídeo chamado `SOURCE · TALKING HEAD · FINAL PLAYBACK MASTER MIX · 1080×1920 · SUBJECT-AWARE FILL`, e esse mesmo vídeo aparece solto na página e isolado num frame `QA · FINAL MIX ONLY · TEMP` [EV-R07-02].

reconciliação: o relato descreve uma etapa anterior. em algum momento as pausas e inserções deixaram de ser montadas no Figma e passaram a vir resolvidas num master mixado, que o Figma só acompanha [EV-R07-03]. as medições sustentam isso de dois jeitos:

- o master tem 59,307 s de imagem e som contínuos, com rosto visível depois de 47,7 s e nenhum preto [EV-R07-11];
- a imagem do master congela exatamente nos trechos em que a fala para e entra música; as pausas viraram quadro congelado da fonte com a música por cima, dentro do próprio master [EV-R07-15].

a duração atual (59,307 s) não bate com a projeção do relato (60,650 s). a diferença de 1,343 s pode ser inserção encurtada ou fonte aparada; não há como saber sem a conversa. o preto depois de 47,7 s **não foi reproduzido no master**, mas o composite do stage não pôde ser renderizado aqui porque a exportação estoura o tempo limite [EV-ENG-01]. ver FAL-03.

## as cinco versões

as cinco versões 4:3 são iguais em tudo, menos em duas coisas [EV-R07-04]:

| versão | hook |
|---|---|
| V01 | vocês / conhecem / os hits da / miley. / olha o / resto. |
| V02 | acho que / vocês nunca / escutaram / a miley / direito. |
| V03 | vocês não / fazem ideia / do tamanho / do catálogo / da miley. |
| V04 | miley tem / muito mais / música boa / do que vocês / conhecem. |
| V05 | vocês / realmente / conhecem / o catálogo / da miley? |

a outra diferença é o tempo e a amplitude das luzes do wallpaper, gradientes desfocados em modo de mesclagem SCREEN que respiram em ciclos de 21 a 28 s [EV-R07-04].

ou seja: as versões foram um teste de hook escrito, com o resto congelado (DEC-09). o vertical, criado depois, usa o texto da V01 [EV-R07-05], o que sugere com pouca confiança que a V01 foi a escolhida [EV-R07-06].

o hook não repete a fala. a fala começa contando que mayco foi mexer no catálogo; o hook é uma manchete que provoca quem assiste [EV-R07-14]. é o mesmo papel do hook editorial do REELS/04.

## anatomia

a estrutura é uma lista falada de músicas, então a coreografia é uma lista visual com uma regra fixa e variações [EV-R07-08]:

- cada música entra no instante em que o nome é dito;
- cada uma traz um objeto efêmero próprio (microfone de glitter, estrela prata, coração vermelho, disco iridescente, chapéu de cowboy verde, sol dourado, globo espelhado, selo de cera);
- cada uma aparece numa superfície real: janela de vídeo com proporção da fonte ou o Spotify montado com sidebar e barra superior reais;
- a janela entra pequena, cresce devagar enquanto a música toca e sai encolhendo pro lado.

a pessoa nunca some. a janela do talking head muda de largura e altura a cada beat para abrir espaço, e o fill acompanha para manter o rosto no lugar [EV-R07-07]. em "gente, pelo amor de deus" a janela cresce para 1100x820: a pessoa ganha tamanho quando a fala ganha ênfase [EV-R07-07].

o cursor existe em quatro momentos e sempre arrastando uma janela que segue o mesmo caminho [EV-R07-09].

a piada mais clara é literal: enquanto a fala diz "isso sem eu nem entrar no assunto de com quem essa mulher já trabalhou", doze fotos de parcerias entram em corte seco, uma a cada ~0,15 s [EV-R07-10]. ele diz que não vai falar e o vídeo fala por ele.

## áudio

o master mistura fala e trechos das músicas. medido no export do frame de QA, a música fica 10 a 13 dB acima da voz [EV-R07-12]. num vídeo que vive de citar música isso pode ser intencional, mas a diferença é grande o bastante para a voz parecer baixa ao lado das inserções. não há registro de que isso tenha sido avaliado. ver FAL-08 e DEC-14.

## vertical

o vertical é recomposição: talking head alto, com trajetórias próprias, e as janelas de música na metade de baixo, largas o bastante para sangrar a borda [EV-R07-13].

## aprovações e pendências

- **resultado**: sem publicação encontrada.
- **pendente**: qual hook foi escolhido; se o composite ainda tem preto; se o nível da música foi intencional; por que a duração mudou.

## o que transfere

- quando a fala é uma lista, a edição pode ser uma regra repetida com variação; a variação vem do conteúdo (cada música tem seu objeto), não do movimento.
- versões úteis variam uma coisa só. aqui, o hook.
- pausas e inserções resolvidas num master mixado e testado isolado reduzem o que pode quebrar no composite (DEC-08). ver [tempo e playback](../engenharia/tempo-e-playback.md).
- a pessoa pode continuar no quadro durante toda a lista se a janela dela responder ao que está acontecendo.

## o que não transfere

- o kit de objetos por música só funciona porque cada objeto conversa com a música. objetos aleatórios por item viram decoração.
- a avalanche de fotos é uma piada sobre uma frase específica. repetida em outro vídeo, perde a razão.

## fontes

S-FIG-PRINCIPAL (página `926:2964`), S-FIG-EXPORT, S-QA-LOCAL, S-PREP.
