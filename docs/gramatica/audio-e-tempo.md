# áudio, tempo e edição

esta seção trata do que o áudio decide na edição. a parte técnica de mapa de tempo, master e playback está em [tempo e playback](../engenharia/tempo-e-playback.md).

## o relógio

- **vídeo falado**: a fala é o relógio. cada evento visual relevante cai numa palavra ou numa pausa (DEC-01).
  - janela do Last.fm abre na palavra "Last.fm" [EV-R02-08];
  - opções de decisão entram quando são ditas [EV-R04-06];
  - cada música do catálogo entra no nome dela [EV-R07-08].
- **vídeo musical**: a faixa é o relógio. trechos da letra organizam cenas, e a gravação oficial fica referenciada pelo tempo da faixa [EV-R08-06].
- **vídeo sem fala e sem música**: o ritmo vem da imagem (REEL 06 acumula em 8,8 s) [EV-R06-01].

antecipar um pouco funciona. a quarta opção do REELS/04 entra meia palavra antes de ser dita, e por isso chega com peso [EV-R04-06]. atrasar só funciona como piada, e precisa ser legível como atraso.

## fala contínua

o talking head nunca é cortado no meio do argumento. quando o ambiente ocupa o quadro, a fonte continua por baixo, coberta por opacidade, e a fala segue (DEC-02). no REELS/02 a pessoa sai do quadro por 21 s e a fala nunca falha no publicado [EV-R02-03], [EV-IG-10].

## pausa e silêncio

- pausa natural da fala é tempo de edição: entra uma imagem, um texto assenta, um estado muda. o REELS/02 tem silêncios curtos em 20,13 e 23,27 s que coincidem com as passagens para "play, nota, foto" e para o produto [EV-IG-10].
- pausa inserida (a fonte para, entra outra coisa) muda o tempo final e exige mapa de tempo (REELS/07) [EV-R07-15].
- silêncio visual: reduzir a atividade quando a fala precisa pousar. o fim do REELS/09 é rosto e poucas palavras [EV-R09-06].

## música dentro de vídeo falado

no REELS/07 os trechos das músicas entram nas pausas da fala, com a imagem da pessoa congelada por baixo [EV-R07-15]. medido no master, a música fica 10 a 13 dB acima da voz [EV-R07-12]. num vídeo sobre música, a música pode ser protagonista; ainda assim, uma diferença desse tamanho faz a voz parecer baixa e o espectador mexer no volume. a regra adotada: medir, decidir e anotar (DEC-14) [EV-NOVA-03]. ver FAL-08.

## loudness

os três publicados ficaram em -14,4, -16,0 e -14,2 LUFS integrados [EV-IG-01], [EV-IG-02], [EV-IG-03]. o repositório não fixa um alvo; registra que os publicados estão nessa faixa.

## sincronia: como conferir

- conferir no render, não no editor.
- transcrição automática com tempo de palavra serve para checar sincronia, não para gerar legenda: ela acerta tempo e erra nome próprio [EV-IG-07], [EV-R02-10].
- a [qa de render](../engenharia/qa-de-render.md) mede preto, congelamento, silêncio e nível por trecho.
- keyframe no lugar certo não prova sincronia. a prova é ver e ouvir o arquivo exportado.

## cortes e overlays

- **overlay**: algo entra sobre a fonte sem pará-la. o tempo final não muda.
- **pausa**: a fonte para; o tempo final cresce. a legenda precisa ser deslocada.
- **corte**: a fonte pula. os reels estudados praticamente não cortam a fala; preferem cobrir.

ver também: [tempo e playback](../engenharia/tempo-e-playback.md), [motion](motion.md).
