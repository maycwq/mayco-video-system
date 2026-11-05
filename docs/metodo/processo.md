# do roteiro ao render

este é o caminho que o acervo sugere quando lido de trás pra frente: o que os vídeos que funcionaram têm em comum, e onde os que deram trabalho travaram. não é uma receita de layout. é a ordem das perguntas.

a regra geral: entender antes de compor, compor antes de animar, animar antes de embelezar, e validar no render, não no editor.

## 1. ouvir e transcrever

antes de qualquer imagem, a fala (ou a música) vira um mapa de tempo.

- gerar transcrição com tempo por palavra e **revisar à mão**. transcrição automática erra justamente o que mais importa: nomes de app, de música, de marca (DEC-01). no acervo, Last.fm virou "leis de FM" e margem virou "imagem" [EV-IG-07].
- marcar pausas, respirações, risos, mudanças de tom. pausa é material de edição.
- se houver música, marcar seções, entradas de voz, batidas fortes e silêncios da faixa.
- o resultado é o SRT revisado, que vira a fonte de verdade do tempo. no acervo, cada legenda carrega no nome o tempo em milésimos [EV-R02-15].

## 2. entender o assunto

- **o que é** a coisa de que se fala? um produto, uma música, uma ideia, um evento.
- **onde acontece**? essa resposta define o ambiente ([ambiente](ambiente.md)).
- **que evidência existe**? gravações de tela, fotos, a própria faixa, prints, objetos. evidência real vale mais que ilustração.
- **que referência cultural já está na fala**? uma artista, um meme, uma série. referência que já está na fala pode virar imagem; referência que não está precisa de motivo para entrar.

## 3. interpretar

- **a única coisa que precisa ficar**. uma frase. se a pessoa esquecer o resto, isso fica. no REELS/04 era "o sistema avisa, mas a decisão é humana".
- **a estrutura do argumento em beats**. cada beat tem um começo marcado na fala. um beat muda quando muda o assunto, o nível (concreto para abstrato) ou o tom.
- **o tom**: explicação, confissão, piada, provocação. o tom decide a temperatura do motion e da cor.
- **onde está a graça**, se houver. humor nasce de uma relação concreta (ver [narrativa e humor](../gramatica/narrativa-e-humor.md)).

## 4. decidir

decisões, nesta ordem:

1. **ambiente** e quando ele entra e sai.
2. **estados espaciais**: quantos estados o quadro tem e o que causa cada passagem. um vídeo curto com uma ideia precisa de poucos estados.
3. **papel do texto**: hook escrito, legenda, texto editorial, rótulo, decisão. cada papel tem regras diferentes ([tipografia](../gramatica/tipografia.md)).
4. **vocabulário de motion**: que gestos este vídeo usa e quais não usa. escolher pouco ([motion](../gramatica/motion.md)).
5. **áudio**: fonte contínua? pausas com música? silêncio? ([áudio e tempo](../gramatica/audio-e-tempo.md)).
6. **formato principal e derivados**: em que formato o vídeo é pensado, e como cada derivado é recomposto ([formatos](../engenharia/formatos.md)).
7. **ferramenta**: onde cada parte é construída ([ferramentas](../engenharia/ferramentas.md)).

registrar alternativas consideradas e por que foram descartadas. isso evita repetir a discussão depois.

## 5. mapa de beats

antes de abrir o editor, uma tabela:

| beat | tempo final | fala ou trecho da música | estado do quadro | causa da mudança | texto | áudio |
|---|---|---|---|---|---|---|
| hook | 0 a 3,4 | ... | pessoa + tese | início | hook escrito | fonte |
| prova | 3,4 a 9,8 | ... | ambiente real | "foi isso que aconteceu" | legenda | fonte |

"tempo final" é o tempo de quem assiste. se houver pausas inseridas, o mapa precisa das duas colunas, tempo final e tempo da fonte ([tempo e playback](../engenharia/tempo-e-playback.md)).

## 6. construir

- camadas nomeadas por função e por intervalo de tempo. no acervo os nomes dizem o papel (`PRIMARY EVIDENCE`, `transition survivor`, `SYSTEM ACTIONS ONLY`) e servem de documentação para quem abre o arquivo depois [EV-R02-02], [EV-R04-03].
- fonte falada contínua, coberta por opacidade quando o ambiente ocupa o quadro (DEC-02).
- texto com fonte proprietária convertido para forma render-safe (DEC-07).
- versões variam uma coisa só (DEC-09). guardar a anterior oculta ao lado da nova ajuda a comparar [EV-R02-09].

## 7. validar no render

o editor mente por omissão: mostra keyframes, não mostra o vídeo como ele sai.

- renderizar o vídeo inteiro e assistir com som, do começo ao fim, em tela de celular.
- rodar a [qa de render](../engenharia/qa-de-render.md): duração, tamanho, fps, preto, congelamento, silêncio, loudness, nível fala x música.
- conferir sincronia de legendas e eventos com a fala.
- conferir cada formato derivado beat por beat: nada ativo fora do quadro.
- só então revisar estética.

## 8. revisar

perguntas para a revisão, nesta ordem:

1. a única coisa que precisava ficar ficou?
2. cada mudança de quadro tem causa na fala ou na música?
3. existe algum elemento que só está ali porque estava disponível? tirar.
4. existe algum movimento que só está ali para mostrar animação? tirar ou dar função.
5. o texto disputa leitura com alguma coisa?
6. se fosse outro assunto, esse vídeo teria ficado igual? se sim, a edição não está falando deste assunto.

"FINAL" no nome não é aprovação (DEC-13). aprovado é o que o mayco disse que está aprovado, ou o que foi publicado, e mesmo publicado pode ter detalhe a corrigir.

## como registrar o trabalho novo

ao terminar uma edição, acrescentar ao repositório:

- um estudo em `docs/estudos/` com o formato dos existentes;
- evidências novas em `data/evidencias.toml` (camada, tempo, medição, publicação);
- decisões recuperadas ou novas em `data/decisoes.toml`, com os três níveis de aprovação;
- falhas encontradas em [falhas](../diagnostico/falhas.md);
- rodar `python3 tools/validate.py`.
