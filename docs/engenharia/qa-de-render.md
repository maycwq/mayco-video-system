# qa de render

o que o editor mostra não é o vídeo. o vídeo é o arquivo exportado, tocado com som, do começo ao fim. este documento é o checklist e o uso das ferramentas.

## checklist

1. **especificação**: tamanho, fps, duração do vídeo e do áudio batem com o planejado. diferença de um ou dois quadros é normal [EV-ENG-03].
2. **preto e congelamento**: todo preto e todo congelamento estão previstos. placa preta de decisão é intencional [EV-IG-06]; congelamento de pausa inserida é intencional [EV-R07-15]; preto depois de um ponto da timeline não é.
3. **áudio**: fala do começo ao fim, sem buraco, sem silêncio que não estava na gravação [EV-IG-10].
4. **nível**: loudness integrado registrado; se houver música inserida, diferença de nível entre fala e música medida e decidida [EV-R07-12] (DEC-14).
5. **sincronia**: eventos e legendas caem nas palavras. conferir com transcrição de tempo de palavra e com os olhos [EV-R02-10].
6. **leitura**: cada texto fica tempo suficiente na tela e tem contraste no frame mais claro e no mais escuro do trecho.
7. **formatos**: cada formato derivado assistido inteiro; nenhum elemento ativo fora do quadro (DEC-15).
8. **folha de contato**: uma imagem com um frame por segundo para revisar composição sem o player.
9. **amostragem de composição**: frames em intervalos iguais, como os `__QA SNAPSHOTS__` dos estudos musicais [EV-R08-06].
10. **resolução cheia para afirmar defeito**: miniatura engana [EV-R08-08].

## ferramenta

```bash
python3 tools/render_qa.py render.mp4 \
  --expect-size 1440x1080 --expect-fps 30 \
  --expect-duration 31.667 --duration-tolerance 0.1 --expect-audio \
  --allow-black 18.9-19.9 \
  --sheet folha.png --sheet-fps 1
```

```bash
python3 tools/render_qa.py master.mp4 \
  --segment fala:0.2-4.8 --segment fala:27.2-31.8 \
  --segment musica:9.0-10.8 --segment musica:12.2-14.7 \
  --max-level-gap 6
```

o script usa ffprobe e ffmpeg (blackdetect, freezedetect, silencedetect, ebur128, astats), devolve um relatório legível ou JSON e sai com código 1 se algo fora do previsto aparecer.

rodado sobre os materiais desta investigação:

- REELS/04 publicado: passa com o preto da decisão declarado como intencional [EV-IG-06];
- master do REELS/07: acusa música 13,4 dB acima da fala em RMS médio, com limite de 6 dB [EV-R07-12];
- master do REELS/07: congelamentos nos trechos de música, que são as pausas [EV-R07-15].

## falsos alarmes conhecidos

- **preto intencional**: placas pretas e fades marcam preto. declarar com `--allow-black` [EV-IG-06].
- **congelamento intencional**: telas estáticas e pausas congeladas marcam congelamento. registrar no mapa de beats.
- **transcrição**: tempo confiável, palavra não. nome de app, música ou marca sai errado [EV-IG-07].
- **miniatura**: letras estreitas parecem faltar em imagem reduzida [EV-R08-08].
- **export de baixa taxa**: a trilha de vídeo pode passar alguns décimos do áudio por arredondamento de quadro [EV-ENG-05].

## quando não dá para exportar

o `export_video` do Figma MCP estoura o limite em stages longos [EV-ENG-01]. alternativas, nesta ordem:

1. exportar pelo próprio Figma (aplicativo) e rodar a qa no arquivo;
2. exportar trechos curtos (frames de QA com uma parte da timeline);
3. exportar só o master e conferir composição por snapshots estáticos;
4. registrar como pendência; não declarar o playback como verificado.
