# lacunas

o que não foi possível confirmar, por que, e o que destravaria. as seções do repositório que dependem destas lacunas estão marcadas como relato ou leitura nos próprios textos.

## críticas e aprovações

- **o que falta**: o texto das cinco conversas e das complementares (S-CHAT-01 a S-CHAT-05).
- **o que fica em aberto**: quem pediu cada mudança; o que foi aprovado como direção, como implementação e como resultado; a ordem das críticas no REELS/08; se a versão atual do REELS/09 foi aprovada; qual hook do REELS/07 foi escolhido.
- **o que destravaria**: exportação das conversas (o ChatGPT permite exportar dados da conta) colocada num lugar acessível, ou trechos colados numa sessão. com isso, preencher os níveis de aprovação em `data/decisoes.toml` e as críticas em [falhas](../diagnostico/falhas.md).

## renders originais

- **o que falta**: os MP4 de REELS/02 e REELS/04 4:3 citados no pedido (S-MP4-R02, S-MP4-R04).
- **o que fica em aberto**: se o 1916x1078 do REELS/02 publicado vem do export (EV-ENG-04); a qualidade original do 4:3 do REELS/04.
- **o que destravaria**: os arquivos numa pasta do Drive conectado ou no ambiente. rodar `tools/render_qa.py` neles.

## composite dos stages longos

- **o que falta**: renderizar REELS/02, 07 e 09 inteiros a partir do Figma (EV-ENG-01).
- **o que fica em aberto**: se o stage do REELS/07 ainda tem preto depois de 47,7 s (FAL-03); a câmera fora do quadro no vertical do REELS/02 (FAL-07); qualquer QA do REELS/09.
- **o que destravaria**: exportar pelo aplicativo do Figma e rodar `tools/render_qa.py`.

## causas técnicas não verificadas

- por que Bootzy falhava no render (FAL-04);
- o sintoma que motivou os frames TEMP do REELS/04 (FAL-05);
- o que era o "mask hack" do REELS/05 ([estudo](../estudos/reels-05.md));
- por que a duração do REELS/07 mudou de 60,650 s para 59,307 s ([estudo](../estudos/reels-07.md)).

## fora do escopo, registrado

- `demo-olue.mp4` e as telas web da olue no Drive: material de produto, possivelmente para reels futuros.
- REELS/10 e REEL 06: estudados só no método.
- bibliotecas comunitárias de iOS, watchOS, visionOS, Material e Simple Design System: vinculadas, uso não verificado fora dos stages principais.

## o que já foi feito para reduzir as lacunas

- toda afirmação que depende de relato está marcada como `implementacao-relatada` ou `hipotese` no registro.
- conflitos entre relato e arquivo ficaram registrados com `contradiz`.
- as ferramentas de QA e de mapa de tempo permitem fechar várias lacunas assim que os arquivos chegarem.
