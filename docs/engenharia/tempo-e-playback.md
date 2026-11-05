# tempo e playback

## três tempos que não podem ser confundidos

- **tempo da fonte**: o instante dentro da gravação original. a fala "Last.fm" acontece em 7,86 s da fonte do REELS/02 [EV-R02-08].
- **tempo final**: o instante que quem assiste vê. sem pausas inseridas, é igual ao da fonte. com pausas, é maior.
- **duração do arquivo**: o que o container diz. pode diferir da timeline por arredondamento de quadro e preenchimento do encoder de áudio, na casa de um ou dois quadros [EV-ENG-03].

o relato do REELS/07 mostra a confusão clássica: uma fonte BASE de 47,600 s, um FINAL projetado de 60,650 s e um render que ficava preto depois de ~47,7 s [EV-PREP-03]. 47,7 s é exatamente onde a fonte acabaria se alguma camada fosse posicionada pelo tempo da fonte em vez do tempo final. a causa real não foi verificada, mas é a hipótese que mais explica o sintoma (ver FAL-03).

## pausas, overlays e áudio

| tipo | o que acontece com a fonte | o que acontece com o tempo final | áudio |
|---|---|---|---|
| overlay | continua | não muda | fonte |
| pausa com quadro congelado | congela no último quadro | cresce pela duração da pausa | música, silêncio ou som da inserção |
| pausa com inserção | sai do quadro | cresce | da inserção |
| corte | pula | encolhe | fonte cortada |

no master atual do REELS/07, as pausas são quadro congelado da fonte com música por cima: a imagem para nos mesmos trechos em que a fala para e a música toca [EV-R07-15].

## o mapa de tempo

para qualquer vídeo com pausas, escrever um plano antes de montar e usar [tools/timeline_map.py](../../tools/timeline_map.py):

```toml
duracao_fonte = 47.6

[[insercao]]
rotulo = "river"
na_fonte = 8.95
duracao = 1.8
audio = "musica"
tipo = "pausa"
```

```bash
python3 tools/timeline_map.py plano.toml --tabela
python3 tools/timeline_map.py plano.toml --fonte 20.0
python3 tools/timeline_map.py plano.toml --legendas fonte.srt > final.srt
```

o mapa responde: em que tempo final cai cada palavra da fonte, e o que está na tela em cada tempo final. legendas e keyframes ancorados na fala precisam ser convertidos para tempo final antes de entrar na timeline. o arquivo [tools/exemplos/plano-insercoes.toml](../../tools/exemplos/plano-insercoes.toml) é um exemplo ilustrativo, com as durações do relato e posições inventadas para o exemplo.

## o master mixado

o REELS/07 resolveu o tempo final fora do Figma [EV-R07-03] (DEC-08):

1. montar fala, pausas e inserções num editor de áudio e vídeo (ou com FFmpeg), gerando um master único com imagem e som contínuos do começo ao fim;
2. testar o master sozinho, num frame que só tem ele (`QA · FINAL MIX ONLY`) [EV-R07-02];
3. usar o master como única fonte no stage e animar tudo no tempo final;
4. medir o master antes de seguir: duração, preto, congelamentos esperados, nível de fala e de música [EV-R07-11], [EV-R07-12].

vantagem: o Figma deixa de ser responsável por playback de várias fontes e por áudio. limite: o master fixa o tempo; mudar uma pausa obriga a regenerar o master e reposicionar o que depende dele.

## playback incompleto: como diagnosticar

1. exportar o master sozinho. se ele tem preto ou silêncio, o problema está antes do Figma.
2. exportar o stage só com a fonte. se aparece preto, é a fonte no stage (opacidade, recorte, duração do fill).
3. ligar as camadas por grupo, como nos frames TEMP do REELS/04 [EV-R04-12], até o defeito aparecer.
4. rodar a [qa de render](qa-de-render.md) em cada export, com os intervalos de preto intencionais declarados.
5. converter o instante do defeito para tempo da fonte com o mapa. se o defeito começa onde a fonte acabaria, alguma camada está no tempo errado.

## cobertura sem perda

a fonte coberta continua tocando (DEC-02). no Figma isso foi feito com opacidade 0 na própria fonte durante o trecho coberto, e o publicado do REELS/02 confirma fala contínua [EV-R02-03], [EV-IG-10]. quando a ferramenta não garante áudio de camada invisível, testar no render antes de confiar.
