# mayco-video-system

memória criativa, técnica e operacional das edições de vídeo do mayco. serve para que qualquer pessoa ou agente de IA receba um roteiro novo e chegue a uma edição com identidade, intenção e acabamento, sem procurar um template anterior para copiar.

não é design system, biblioteca de templates nem catálogo de efeitos. é uma base que ensina a investigar o assunto, decidir o ambiente, compor no tempo da fala, construir, validar no render e revisar. o que funcionou antes está aqui como evidência e raciocínio, com o que transfere e o que não transfere.

## o que a base defende

1. **o conteúdo vem antes da forma.** a primeira pergunta é sobre o que se fala e onde isso acontece, não qual layout usar.
2. **o ambiente é o lugar onde o assunto acontece.** software pede o software real; uma música pede a música; um jogo pede o jogo; uma confissão pede o rosto. quando o argumento sai desse lugar, o quadro sai junto. ([ambiente](docs/metodo/ambiente.md))
3. **a fala é o relógio.** eventos visuais caem em palavras; a fonte falada não é cortada, é coberta. em música, a faixa é o relógio. ([áudio e tempo](docs/gramatica/audio-e-tempo.md))
4. **texto é direção.** cada papel de texto tem regra própria, e a família vem de quem fala no quadro. ([tipografia](docs/gramatica/tipografia.md))
5. **todo movimento responde a uma pergunta**: que ação, para onde olhar, que ideia mudou, que energia. se não responde, sai. ([motion](docs/gramatica/motion.md))
6. **o vídeo é o arquivo exportado.** keyframe certo não prova nada; prova é o render medido e assistido. ([qa de render](docs/engenharia/qa-de-render.md))
7. **decisões comprovadas se preservam; escolhas passadas não viram obrigação.**

## como consultar

### por assunto

| assunto | onde |
|---|---|
| processo do roteiro ao render | [docs/metodo/processo.md](docs/metodo/processo.md) |
| escolher o ambiente | [docs/metodo/ambiente.md](docs/metodo/ambiente.md) |
| escrita em tela e da documentação | [docs/metodo/escrita.md](docs/metodo/escrita.md) |
| composição | [docs/gramatica/composicao.md](docs/gramatica/composicao.md) |
| tipografia | [docs/gramatica/tipografia.md](docs/gramatica/tipografia.md) |
| motion | [docs/gramatica/motion.md](docs/gramatica/motion.md) |
| áudio, tempo e edição | [docs/gramatica/audio-e-tempo.md](docs/gramatica/audio-e-tempo.md) |
| interfaces | [docs/gramatica/interfaces.md](docs/gramatica/interfaces.md) |
| cor, superfície e efêmeras | [docs/gramatica/cor-e-materia.md](docs/gramatica/cor-e-materia.md) |
| narrativa e humor | [docs/gramatica/narrativa-e-humor.md](docs/gramatica/narrativa-e-humor.md) |
| Figma como motor | [docs/engenharia/figma-como-motor.md](docs/engenharia/figma-como-motor.md) |
| tempo da fonte x tempo final, playback | [docs/engenharia/tempo-e-playback.md](docs/engenharia/tempo-e-playback.md) |
| 16:9, 4:3 e 9:16 | [docs/engenharia/formatos.md](docs/engenharia/formatos.md) |
| escolher ferramentas | [docs/engenharia/ferramentas.md](docs/engenharia/ferramentas.md) |
| validar render | [docs/engenharia/qa-de-render.md](docs/engenharia/qa-de-render.md) |

### por problema ou decisão

| pergunta | comece por |
|---|---|
| que ambiente usar neste roteiro? | [ambiente, "como decidir"](docs/metodo/ambiente.md#como-decidir) |
| como fazer o hook? | [tipografia, hook escrito](docs/gramatica/tipografia.md#hook-escrito) e [escrita](docs/metodo/escrita.md) |
| a animação ficou genérica, e agora? | [diagnóstico](docs/diagnostico/README.md), FAL-02 e FAL-13 |
| o render ficou preto em algum ponto | [tempo e playback](docs/engenharia/tempo-e-playback.md#playback-incompleto-como-diagnosticar), FAL-03 |
| como colocar música nas pausas da fala? | [tempo e playback](docs/engenharia/tempo-e-playback.md), FAL-08 |
| como adaptar para vertical? | [formatos](docs/engenharia/formatos.md), FAL-07 |
| a fonte saiu errada no render | FAL-04 em [falhas](docs/diagnostico/falhas.md) |
| uso Bootzy? | [tipografia](docs/gramatica/tipografia.md#famílias-usadas-e-por-quê) |
| uso uma biblioteca de interface? | [interfaces](docs/gramatica/interfaces.md#bibliotecas) |
| isso foi aprovado? | [proveniência](docs/fontes/README.md#aprovação-em-três-níveis) |
| qualquer sintoma | [diagnóstico por sintoma](docs/diagnostico/README.md) |

### por trabalho

[estudos](docs/estudos/README.md): REELS/02, 04, 05, 07, 08, 09 e outros, com cronologia, anatomia por beat, engenharia, aprovações, pendências e o que transfere.

## de onde veio o conhecimento

a reconstrução leu o arquivo Figma principal e as bibliotecas sem alterá-los, analisou os três reels publicados, exportou e mediu o que foi possível, e confrontou tudo com o relato da investigação anterior. as conversas originais não estavam acessíveis; o que depende delas está marcado.

- [proveniência](docs/fontes/README.md): como citar e as classes de evidência;
- [inventário](docs/fontes/inventario.md): fontes acessadas, inacessíveis, direitos;
- [revisão das hipóteses](docs/fontes/hipoteses.md): o que foi confirmado, reformulado e descoberto;
- [lacunas](docs/fontes/lacunas.md): o que falta e o que destravaria;
- registros: [data/fontes.toml](data/fontes.toml), [data/evidencias.toml](data/evidencias.toml), [data/decisoes.toml](data/decisoes.toml).

## testes de uso

a base foi testada com cinco roteiros novos (software real, pessoal sem software, musical, inserções temporais, horizontal para vertical), com propostas feitas por um agente que só leu o repositório e auditadas por outro. resultados e correções em [cenários](docs/cenarios/README.md).

## ferramentas

```bash
python3 tools/validate.py              # integridade da base, citações, links, escrita, publicação
python3 -m unittest discover -s tests  # testes das ferramentas
python3 tools/render_qa.py render.mp4 --expect-duration 31.667 --expect-audio
python3 tools/timeline_map.py plano.toml --tabela
```

detalhes em [tools/README.md](tools/README.md). requer python 3.11+; `render_qa` requer ffmpeg.

## para agentes de IA

leia [AGENTS.md](AGENTS.md) antes de qualquer trabalho. [CLAUDE.md](CLAUDE.md) aponta para o mesmo lugar.

## estado anterior

antes da reconstrução, `main` tinha só este arquivo com o título (commit `990aa43`). o histórico está preservado.
