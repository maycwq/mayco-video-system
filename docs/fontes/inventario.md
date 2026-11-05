# inventário de fontes

estado em 2026-11-05. o registro completo, com localizadores, está em [data/fontes.toml](../../data/fontes.toml).

## acessadas

| fonte | como | o que rendeu |
|---|---|---|
| arquivo Figma principal `mayco \| frame director` (S-FIG-PRINCIPAL) | Figma MCP, só leitura | estrutura de todos os stages, nomes, keyframes, fontes, mídia, versões |
| design system (S-FIG-DS) | Figma MCP, só leitura | catálogo de padrões e templates |
| ephemera kit, media players, social interfaces, apple legacy, windows 95, UI3 (S-FIG-EPHEMERA, S-FIG-MEDIA, S-FIG-SOCIAL, S-FIG-APPLE, S-FIG-WIN95, S-FIG-UI3) | Figma MCP, só leitura | inventário de componentes e cruzamento com o uso real |
| três reels publicados (S-IG-A, S-IG-B, S-IG-C) | yt-dlp anônimo, análise local | correspondência com o Figma, frames, áudio, medições |
| exports do Figma (S-FIG-EXPORT) | `export_video` | REEL 06, REELS/03 e o master do REELS/07 |
| manual de tom de voz (S-MANUAL-VOZ) | anexo da sessão | regras de escrita |
| pedido de reconstrução e relato preparatório (S-PEDIDO, S-PREP) | mensagem do usuário | instruções e hipóteses a testar |
| medições locais (S-QA-LOCAL) | ffprobe, ffmpeg, faster-whisper | qa, sincronia, níveis |

## inacessíveis

| fonte | o que foi tentado | o que fica sem confirmação |
|---|---|---|
| conversas 01 a 05 do ChatGPT (S-CHAT-01 a S-CHAT-05) e conversas complementares | acesso anônimo devolve página vazia; não há conector nem exportação; busca no Drive sem resultado | o texto das críticas, as aprovações explícitas, a ordem das tentativas, a autoria de cada mudança |
| render original do REELS/02 (S-MP4-R02) | anexos da sessão, Drive, ambiente | se o 1916x1078 do publicado vem do export ou da plataforma |
| render original do REELS/04 4:3 (S-MP4-R04) | idem | qualidade original do master; o publicado foi reduzido para 960x720 |
| composite dos stages longos | `export_video` estoura o limite em 35 a 60 s (EV-ENG-01) | se o stage do REELS/07 ainda tem preto; o render do REELS/09 |

## parcialmente acessadas

- **Google Drive** (S-DRIVE): nenhum render de reel nem exportação de conversa. existe um `demo-olue.mp4` de outubro e PDFs de telas da olue, não analisados porque não pertencem aos reels estudados.

## o que cada fonte pode publicar

| fonte | publicável |
|---|---|
| arquivos Figma | metadados: nomes de camada, node ids, tempos, valores. nenhuma imagem exportada. |
| reels publicados | metadados, descrição do que se vê, tempos, medições. os vídeos não entram. |
| conversas | nada. |
| manual de voz | resumo das regras aplicáveis; o manual não é copiado. |
| exports e medições | números e conclusões; os arquivos não entram. |

## direitos e privacidade

- **Bootzy TM** é fonte proprietária. o repositório só a nomeia.
- **músicas, clipes, capas, fotos de parcerias e memes** usados nos reels são de terceiros. o repositório só os nomeia quando necessário para explicar uma decisão.
- **efêmeras do kit** podem incluir imagens de terceiros. não redistribuir.
- **pessoas**: o repositório não nomeia pessoas privadas. os tweets satíricos do REELS/05 são personas inventadas; seus handles não são reproduzidos.
- **conteúdo político** do REELS/10: só o método é registrado.
- **arquivos Figma**: os links identificam arquivos privados; o acesso continua dependendo de permissão no Figma.

## design system e catálogo de padrões

o design system é uma tentativa anterior de sistematizar a linguagem para IA [EV-DS-01], [EV-DS-02]:

- **motion**: 55 padrões em quatro níveis (micro, meso, macro, timing), cada um com descrição `AI_MOTION_PATTERN v1`: intenção, gatilho, estados, tokens de duração e easing, contrato de camadas, templates compatíveis, âncora de voz, regras por formato, fallback, quando usar e quando evitar.
- **humor**: 20 padrões com mecanismo, intensidade, preparação e expectativa.
- **mídia**: 35 padrões de uso de foto, vídeo e gravação de tela.
- **templates**: 25 em 16:9 e 25 em 9:16.
- **componentes**: Narrative (texto em vários papéis), Media/Slot, Connector, Composition.
- páginas de foundations, tipografia, exemplos e documentação vazias.

o REELS/04 usa os códigos nos nomes de camada; os trabalhos seguintes não [EV-R04-03], [EV-DS-03]. esta base trata o catálogo como vocabulário histórico: os nomes ajudam a conversar sobre padrões, mas a direção de um vídeo novo começa pelo conteúdo, não pela escolha de um template [EV-REQ-01].

## bibliotecas: o que existe e o que foi usado

| biblioteca | conteúdo | uso verificado |
|---|---|---|
| macOS 26 (comunidade) | wallpaper, menu bar, dock, janelas, controles, ponteiros | REELS/02, 04, 07 [EV-LIB-02] |
| ephemera kit | 75 objetos em 6 famílias [EV-LIB-03] | REELS/02, 04, 03 (stickers); no 07 as efêmeras são imagens soltas [EV-LIB-04] |
| media players | 26 componentes de Spotify e 8 patterns | REELS/04, 07 [EV-LIB-02] |
| design system | Narrative, Media/Slot, catálogo | REELS/02, 04, 05, 07 [EV-LIB-02] |
| UI3 (comunidade) | interface do Figma | REELS/03; no 02 só o nome [EV-R02-14], [EV-R03-01] |
| social interfaces | 140 componentes de Instagram | nenhum uso encontrado [EV-LIB-02] |
| apple legacy | 249 componentes | nenhum uso encontrado [EV-LIB-02] |
| windows 95 | 120 componentes | nenhum uso encontrado [EV-LIB-02] |
| Material 3, Simple Design System, iOS 18 e 26, watchOS, visionOS (comunidade) | kits gerais | não verificado em detalhe; nenhuma instância nos stages checados |

o uso foi verificado nos stages principais (REELS/02 horizontal, 04 em 4:3, 05 em 4:3, 07 V05, 09). páginas de rascunho podem usar outras bibliotecas.

## estado do repositório antes da reconstrução

`main` no commit `990aa43`, com um único `README.md` contendo o título. o histórico está preservado; a reconstrução entra por pull request sem reescrever `main`.
