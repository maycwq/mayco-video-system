# proveniência

toda afirmação técnica ou criativa importante desta base aponta para uma evidência. a evidência aponta para uma fonte. assim dá para saber de onde veio cada coisa, com que confiança, e o que muda se a fonte for revista.

## três registros

| arquivo | o que guarda | id |
|---|---|---|
| [data/fontes.toml](../../data/fontes.toml) | cada fonte consultada ou tentada: arquivos Figma, reels publicados, conversas, renders, medições, o pedido | `S-...` |
| [data/evidencias.toml](../../data/evidencias.toml) | cada observação, medição, relato ou interpretação, com classe, localizador e confiança | `EV-<escopo>-<n>` |
| [data/decisoes.toml](../../data/decisoes.toml) | decisões de direção e engenharia, com aprovação separada em direção, implementação e resultado | `DEC-<n>` |

os estudos de falha ficam em markdown, em [falhas](../diagnostico/falhas.md), com id `FAL-<n>`.

## classes de evidência

| classe | quer dizer | exemplo |
|---|---|---|
| fato-observado | visto diretamente na fonte | o nome de uma camada, um keyframe, um frame do vídeo publicado |
| resultado-verificado | confirmado por medição ou teste | o blackdetect, a transcrição, a duração medida |
| instrucao-explicita | pedido do usuário, implementado ou não | o pedido de não tornar Bootzy obrigatória |
| implementacao-relatada | dito numa conversa ou relato, sem verificação | os 47,600 s de BASE do REELS/07 |
| interpretacao | inferência sustentada por outras evidências, listadas em `relacionadas` | o master mixado como resposta ao preto |
| hipotese | ainda precisa de investigação | a causa dos 1916x1078 |
| decisao-nova | proposta desta reconstrução | a reformulação do princípio do ambiente |

confiança (alta, média, baixa) diz quanto a evidência sustenta a afirmação. confiança alta não substitui fonte.

## aprovação em três níveis

uma decisão pode ter a direção aprovada, a implementação aprovada e o resultado aprovado em momentos diferentes, ou só um deles. por isso `data/decisoes.toml` registra os três separados, com os valores `verificada`, `publicada`, `nao-verificavel`, `pendente` e `nao-se-aplica`. "publicada" quer dizer que foi ao ar; não quer dizer que cada detalhe foi aprovado.

nesta reconstrução quase toda aprovação de direção e implementação ficou `nao-verificavel`, porque as conversas não foram acessadas. isso é uma lacuna, não um julgamento.

## conflitos

quando duas fontes discordam, as duas ficam registradas, e a evidência mais recente aponta `contradiz` para a outra. a reconciliação é escrita no estudo correspondente. exemplo: o relato do REELS/07 descreve camadas de pausa que o arquivo atual não tem [EV-PREP-03], [EV-R07-01]; o [estudo](../estudos/reels-07.md) explica como as duas coisas se encaixam.

## como citar

- num documento, a citação vai entre colchetes no mesmo parágrafo, item ou linha de tabela da afirmação: `[EV-R02-03]`.
- decisões e falhas são citadas pelo id sem colchetes: DEC-02, FAL-03.
- nos estudos, na gramática e no capítulo do ambiente, todo bloco com medida (segundos, px, dB, LUFS) ou node id precisa citar evidência. o validador recusa o contrário.

## como acrescentar

1. registrar a fonte em `data/fontes.toml`, com o que dela pode ser publicado.
2. registrar cada observação em `data/evidencias.toml`, com localizador preciso (node id, timestamp, comando).
3. citar nos documentos.
4. rodar `python3 tools/validate.py`.

## o que pode ser publicado

o repositório pode ser público. ele guarda metadados, descrições, ids, tempos e trechos curtos; não guarda vídeos, imagens, áudios, fontes tipográficas, conversas, links temporários nem credenciais. o validador barra extensões de mídia e fonte, arquivos grandes, urls assinadas, tokens e e-mails. detalhes por fonte em [inventário](inventario.md).
