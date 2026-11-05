# Figma como motor de edição

todo o acervo foi montado no Figma, usando a timeline de animação nativa. este documento registra como os stages são construídos, o que funcionou, os limites encontrados e como inspecionar um arquivo sem alterá-lo. a escolha de ferramenta para trabalhos novos está em [ferramentas](ferramentas.md).

## anatomia de um stage

- **frame raiz** no tamanho do formato (1920x1080, 1440x1080, 1080x1920), nomeado com reel, formato, tamanho e a palavra `TEMPORAL STAGE` [EV-R02-01].
- **camadas por função e por intervalo**: cada grupo de beat leva no nome o intervalo em segundos e a função (`B2 · 06.020–16.920 · WORKSPACE · MUSIC → FILMS → PHOTOS`) [EV-R02-02].
- **fonte em video fill** num retângulo, contínua, com o nome dizendo a duração e se tem áudio [EV-R02-03], [EV-R04-02].
- **mídia de prova** em `Media/Slot` com video fill (gravações) ou image fill (prints, capas) [EV-R02-13].
- **ambiente** com componentes de biblioteca (macOS 26, Spotify, efêmeras) [EV-LIB-02].
- **texto** em glifos vetoriais ou componentes render-safe quando a fonte é Bootzy [EV-R02-15], [EV-R04-13].
- **mestres ocultos** dentro do stage, marcados `do not export` (banco de glifos, timing source de legendas, versões anteriores) [EV-R02-15], [EV-R02-09].

## animação

- keyframes manuais por propriedade: opacidade, translação, escala, rotação, largura e altura [EV-ENG-02];
- HOLD como corte seco; ease out (0, 0, 0.58, 1) como entrada padrão; ease in and out nas derivas; cúbica customizada (0.5, 0, 0.5, 1) em alguns preparos; spring em casos específicos [EV-ENG-02];
- a duração da timeline aparece em `node.animations[*].timelineDuration` de qualquer nó animado; o `get_motion_context` do frame raiz pode devolver duração nula, então não confiar nele para isso.

## convenções que valem a pena manter

- **nome diz papel e tempo**. quem abre o arquivo sem contexto entende o que cada camada faz. os nomes também carregam regras (`NO INVENTED UI`, `SYSTEM ACTIONS ONLY`, `RECOLOR ONLY`) [EV-R02-14], [EV-R05-03].
- **versão anterior fica oculta ao lado da nova**, com `previous treatment · hidden` [EV-R02-09]. permite comparar e voltar.
- **frames de QA e de teste** com prefixo `TEMP` ou `QA` e instrução de apagar [EV-R04-12], [EV-R07-02].
- **assets brutos fora do stage**, soltos na página com prefixo `ASSET ·` (REELS/09).

## limites encontrados

- **fontes proprietárias**: Bootzy precisou virar vetor ou componente render-safe, com bancos próprios de acentos e pontuação [EV-R08-09]. ver FAL-04.
- **tempo com pausas**: montar pausas e inserções com várias fontes no Figma deu problema de playback; o caminho adotado foi um master mixado fora [EV-R07-03]. ver FAL-03.
- **exportação**: o 4:3 do REELS/04 precisou de treze frames de teste isolando subárvores para descobrir o que quebrava [EV-R04-12]. ver FAL-05.
- **exportação pelo MCP**: stages de 35 a 60 s estouram o limite de 60 s da chamada `export_video`, mesmo em 5 fps e 0,25x; frames curtos exportam [EV-ENG-01].
- **adaptação de formato**: elementos podem ficar fora do quadro quando o vertical herda coordenadas do horizontal [EV-R02-18]. ver FAL-07.
- **custo de vetorização**: gravações vetorizadas viram milhares de nós por frame (página descartado) [EV-R08-05].

## inspecionar sem alterar

o script [tools/figma/inspect-stage.js](../../tools/figma/inspect-stage.js) lista um stage com nomes, geometria, fills de vídeo e imagem, texto e keyframes compactados. foi a ferramenta de coleta desta base. ele só lê.

regras de segurança para qualquer agente:

- arquivos de origem não são editados durante investigação. experimento acontece numa cópia ou num arquivo novo.
- `use_figma` só com scripts de leitura: nada de criar, mover, renomear, apagar, `setPluginData`.
- `export_video` é leitura: gera um MP4 no servidor e devolve um link temporário. o link não vai para o repositório.

## quando o Figma é a ferramenta certa

- edição com interface e tipografia como protagonistas, em que a precisão de layout importa mais que efeitos de vídeo;
- quando a pessoa que dirige precisa abrir, ver e mexer no mesmo lugar;
- quando os componentes de biblioteca economizam reconstrução.

quando não é: mix de áudio, montagem com muitas fontes de vídeo e cortes, tratamento de cor de vídeo, efeitos de partícula ou 3D, renders longos repetidos. ver [ferramentas](ferramentas.md).
