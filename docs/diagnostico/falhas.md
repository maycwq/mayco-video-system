# estudos de falha

cada estudo registra um problema real do acervo como mecanismo: o que se tentava, o que aconteceu, por quê, o que mudou e o que dá para levar para outros trabalhos. as críticas originais estavam nas conversas, que não foram acessadas; quando a crítica é conhecida só pelo relato preparatório, isso está dito. causa técnica sem verificação fica como hipótese.

o índice por sintoma está em [diagnóstico](README.md).

### FAL-01 · interface genérica no lugar do objeto

- **intenção**: mostrar que play, nota e foto, juntos numa tela, não bastam [EV-R02-12].
- **implementação**: um ícone de play autoral, estrelas de nota e uma foto placeholder no beat S07 do REELS/02 [EV-R02-12].
- **resultado observado**: as camadas estão ocultas e se chamam `AUTHORIAL GENERIC · no library equivalent`, `SYMBOLIC NO VALUE` e `PLACEHOLDER` [EV-R02-12].
- **crítica**: não acessível. os próprios nomes de camada registram o diagnóstico: genérico, simbólico, sem valor.
- **hipótese de causa**: ícones de interface sem dono não pertencem a nenhum ambiente real e parecem wireframe.
- **evidência da causa**: os substitutos são objetos do kit de efêmeras com rótulo de uma palavra, coerentes com o resto do vídeo [EV-R02-12], [EV-LIB-03].
- **correção proposta**: trocar símbolo genérico por objeto que carregue o significado (cd para música, botão estrela para nota, câmera para foto).
- **alteração realizada**: feita no arquivo; os genéricos ficaram ocultos [EV-R02-12].
- **resultado depois**: no publicado, "play nota foto" aparece com os objetos e rótulos [EV-IG-01].
- **aprovação**: resultado publicado; aprovação explícita não verificável.
- **princípio**: quando um conceito precisa de imagem, usar um objeto real ou uma interface real, nunca um ícone de interface que não existe.
- **limites**: ícone de interface real dentro da interface real é legítimo. o problema é o ícone solto, sem sistema.

### FAL-02 · coreografia de efeito em vez de composição

- **intenção**: dar presença e energia à letra de bass persuades [EV-R08-01].
- **implementação**: versão cinética em Boogaloo, uma palavra por vez, quase todas girando até 35°, vindo de até 760 px e crescendo até 2,35x [EV-R08-01].
- **resultado observado**: o mesmo gesto em toda palavra; o movimento domina e a composição de cada trecho não muda de lógica [EV-R08-01].
- **crítica**: pelo relato, duas críticas em momentos diferentes: falta de presença, variedade, inteligência compositiva e relação com a música; depois excesso de movimento, rotação e recursos arbitrários [EV-PREP-04]. qual artefato recebeu qual crítica não está verificado.
- **hipótese de causa**: a pergunta de partida era "como cada palavra entra" em vez de "que lugar cada palavra ocupa neste trecho da música".
- **evidência da causa**: a V3 e o rebuild nomeiam camadas por função compositiva (pin, mass, crop, spine, counterweight, slab) e escondem elementos [EV-R08-02], [EV-R08-03], [EV-R08-04].
- **correção proposta**: cenas por trecho da letra; escala, recorte, borda, contrapeso e vazio como recursos; rotação só quando vira eixo ou peso.
- **alteração realizada**: V3 e rebuild vertical no arquivo [EV-R08-02], [EV-R08-03].
- **resultado depois**: snapshots mostram composições com palavra gigante recortada, linha de leitura pequena, colunas de letras e campos de cor [EV-R08-07]. nenhum render publicado.
- **aprovação**: pendente; não há publicação nem registro acessível.
- **princípio**: coreografia é composição no tempo. cada elemento precisa de função espacial ligada a um momento da música (DEC-10).
- **limites**: não é proibição de rotação ou spring. no REELS/09 um gesto elástico curto combina com o assunto [EV-R09-03].

### FAL-03 · preto depois de ~47,7 s

- **intenção**: um vídeo de ~60 s com pausas musicais inseridas sobre uma fala de 47,6 s [EV-PREP-03].
- **implementação**: pelo relato, camadas de PAUSE INSERTS, overlays e legendas com offset dentro do Figma [EV-PREP-03].
- **resultado observado**: pelo relato, o render ficava preto depois de ~47,7 s, mesmo após correções [EV-PREP-03].
- **crítica**: o usuário relatou o preto persistente (conhecido só pelo relato).
- **hipótese de causa**: alguma camada de fonte ficou posicionada ou com duração no tempo da fonte (47,6 s) em vez do tempo final; quando a fonte acaba, sobra preto. não verificado.
- **evidência da causa**: indireta: o instante do preto coincide com a duração da fonte [EV-PREP-03]; o arquivo atual abandonou a montagem por camadas e usa um master único [EV-R07-02].
- **correção proposta**: resolver pausas e áudio num master mixado fora do Figma, testado isolado; usar o master como fonte única (DEC-08).
- **alteração realizada**: o arquivo atual tem o master como fonte de todas as versões e um frame de QA só com ele [EV-R07-02].
- **resultado depois**: o master tem imagem e som contínuos até 59,307 s, sem preto [EV-R07-11]. o composite do stage não pôde ser renderizado aqui [EV-ENG-01].
- **aprovação**: pendente. o problema relatado não pode ser declarado resolvido.
- **princípio**: tempo final mora num lugar só; tudo o mais se ajusta a ele. ver [tempo e playback](../engenharia/tempo-e-playback.md).
- **limites**: o master fixa o tempo; mudar uma pausa obriga a regenerar e reposicionar.

### FAL-04 · fonte proprietária que não sobrevive ao render

- **intenção**: usar Bootzy TM em legendas, hooks e textos [EV-R02-15].
- **implementação**: texto em Bootzy em vários reels [EV-R04-13].
- **resultado observado**: o arquivo acumula soluções de contorno: glifos vetoriais, componentes `RENDER-SAFE` por palavra, bancos de acentos e pontuação, camadas `TROCAR PARA BOOTZY TM` pendentes [EV-R02-15], [EV-R04-13], [EV-R08-09], [EV-R05-06].
- **crítica**: não acessível.
- **hipótese de causa**: o pipeline de render ou exportação não usa a fonte instalada localmente, ou substitui glifos sem acento. não verificado.
- **evidência da causa**: a existência de bancos específicos para acentos e pontuação indica que esses glifos falhavam na vetorização automática [EV-R08-09].
- **correção proposta**: converter texto final em forma com glifos conferidos, manter versão editável oculta, conferir acentos em resolução cheia (DEC-07).
- **alteração realizada**: feita caso a caso nos stages [EV-R02-15], [EV-R04-13].
- **resultado depois**: os publicados mostram Bootzy com acentos [EV-IG-01], [EV-IG-03].
- **aprovação**: resultado publicado.
- **princípio**: texto que precisa sair igual em qualquer render vira forma; a versão editável fica guardada.
- **limites**: vetorizar tira a edição rápida e pode errar espaçamento; conferir antes de publicar.

### FAL-05 · exportação do 4:3 diagnosticada por isolamento

- **intenção**: publicar o REELS/04 em 4:3 [EV-IG-03].
- **implementação**: stage 4:3 com o ambiente de 1920 de largura dentro de um quadro de 1440 [EV-R04-02].
- **resultado observado**: treze frames TEMP de teste de exportação, isolando raiz, geometria, mídia, desk, Spotify, wallpaper e atmosfera [EV-R04-12].
- **crítica**: não acessível; o sintoma que motivou os testes não está registrado.
- **hipótese de causa**: alguma camada fora do quadro, mais larga que a raiz, ou com fill pesado travava ou corrompia a exportação. não verificado.
- **evidência da causa**: o desenho dos testes isola exatamente as camadas mais largas que a raiz e as de fill mais pesado [EV-R04-12], [EV-R04-10].
- **correção proposta**: bisseção por camadas até o defeito aparecer, como os frames TEMP fazem.
- **alteração realizada**: desconhecida; o 4:3 foi publicado [EV-IG-03].
- **resultado depois**: publicado sem defeito visível; o preto de 1 s é intencional [EV-IG-06].
- **aprovação**: resultado publicado.
- **princípio**: defeito de render se acha isolando camadas e exportando, não olhando o editor.
- **limites**: bisseção custa exports; começar pelo que é mais largo que o quadro e pelo que tem vídeo.

### FAL-06 · esconder a pessoa sem perder a fala

- **intenção**: o ambiente ocupar o quadro enquanto a pessoa continua falando [EV-R02-04].
- **implementação**: a V0 cobria a pessoa com um retângulo opaco chamado `TALKING HEAD MUST NEVER LEAK` [EV-R02-04].
- **resultado observado**: a cobertura opaca protege a imagem, mas cria uma camada extra que precisa acompanhar todos os tempos.
- **crítica**: não acessível.
- **hipótese de causa**: o problema de vazamento vinha de a fonte ficar visível sob elementos semitransparentes.
- **evidência da causa**: o stage atual troca a cobertura opaca por gate de opacidade na própria fonte [EV-R02-04], [EV-R02-19].
- **correção proposta**: deixar a fonte contínua com opacidade 0 no trecho coberto; a cobertura vira transparente (DEC-02).
- **alteração realizada**: feita no stage horizontal [EV-R02-03].
- **resultado depois**: no publicado, a pessoa não vaza e a fala segue contínua [EV-IG-10].
- **aprovação**: resultado publicado.
- **princípio**: cobrir não é remover; a fonte some da imagem e fica no som.
- **limites**: depende de a ferramenta tocar o áudio de camada invisível; testar no render.

### FAL-07 · adaptação de formato que perde elementos

- **intenção**: ter versões verticais dos reels horizontais [EV-R02-17], [EV-R04-11].
- **implementação**: no REELS/02, recomposição com trajetórias novas; no REELS/04, deslocamentos multiplicados por 0,32 [EV-R02-17], [EV-R04-11].
- **resultado observado**: no REELS/02 vertical a câmera rosa ficou fora do quadro [EV-R02-18]; no REELS/04 vertical, seis frames de QA isolando camadas sugerem problemas de render [EV-R04-12].
- **crítica**: não acessível.
- **hipótese de causa**: elementos que não foram revisados beat a beat herdaram coordenadas do horizontal; escala proporcional não respeita a geometria do novo quadro.
- **evidência da causa**: a coordenada x=1115 num quadro de 1080 é a mesma do horizontal [EV-R02-18].
- **correção proposta**: recompor por beat e rodar checagem de limites em todos os nós visíveis (DEC-12, DEC-15).
- **alteração realizada**: nenhuma no arquivo.
- **resultado depois**: verticais não publicados.
- **aprovação**: pendente.
- **princípio**: formato derivado é uma composição nova com o mesmo tempo, não uma escala.
- **limites**: a checagem pega elemento perdido, não composição fraca.

### FAL-08 · música inserida muito acima da fala

- **intenção**: tocar trechos das músicas citadas nas pausas da fala [EV-R07-15].
- **implementação**: master mixado com quadro congelado e música nas pausas [EV-R07-15].
- **resultado observado**: música 10 a 13 dB acima da voz em RMS [EV-R07-12].
- **crítica**: nenhuma registrada; encontrada nesta investigação.
- **hipótese de causa**: os trechos musicais entraram com nível de master comercial e a voz com nível de gravação.
- **evidência da causa**: picos da música entre -8,8 e -12,7 dB contra picos da fala entre -15 e -20 dB no mesmo arquivo [EV-R07-12].
- **correção proposta**: nivelar a voz para cima ou a música para baixo, medir de novo, anotar a diferença escolhida (DEC-14).
- **alteração realizada**: nenhuma.
- **resultado depois**: não se aplica.
- **aprovação**: pendente.
- **princípio**: mix se decide com medida e se registra; ouvido acostumado engana.
- **limites**: medido num export de baixa qualidade; a diferença relativa vale, o nível absoluto não.

### FAL-09 · legenda disputando com texto editorial

- **intenção**: legenda palavra por palavra durante todo o vídeo [EV-R02-15].
- **implementação**: legenda grande, centralizada, mesma família do texto editorial [EV-IG-04].
- **resultado observado**: em ~18,6 s a legenda "o" fica sobre o bloco editorial na mesma cor e família [EV-IG-05].
- **crítica**: nenhuma registrada; observação desta investigação, com confiança média.
- **hipótese de causa**: as duas camadas foram desenhadas separadamente, sem regra de convivência.
- **evidência da causa**: no mesmo vídeo, a cor da legenda muda por fundo, mas não muda quando há texto editorial [EV-IG-04], [EV-IG-05].
- **correção proposta**: quando há texto editorial, a legenda muda de lugar, de escala ou some naquele trecho.
- **alteração realizada**: nenhuma.
- **resultado depois**: não se aplica.
- **aprovação**: resultado publicado com o problema.
- **princípio**: cada papel de texto tem lugar e aparência próprios; dois papéis não usam o mesmo código visual no mesmo instante.
- **limites**: em instantes muito curtos a disputa pode ser tolerável; decidir olhando o frame.

### FAL-10 · movimento invisível sob cobertura

- **intenção**: provavelmente, mostrar partes da ficha do produto em sincronia com as opções de decisão [EV-R04-07].
- **implementação**: pans e zoom na mídia da ficha nos tempos das quatro opções [EV-R04-07].
- **resultado observado**: tudo acontece sob a tinta preta sólida; ninguém vê [EV-R04-07].
- **crítica**: nenhuma registrada.
- **hipótese de causa**: a tinta entrou depois, num tratamento novo da decisão, e a animação antiga ficou [EV-R04-08].
- **evidência da causa**: fraca: a sincronia dos pans com as opções indica que eles foram pensados para ser vistos [EV-R04-08].
- **correção proposta**: remover animação que não aparece no render, ou guardar como versão oculta nomeada.
- **alteração realizada**: nenhuma.
- **resultado depois**: não se aplica; sem efeito no publicado.
- **aprovação**: não se aplica.
- **princípio**: o arquivo deve dizer o que o vídeo faz; restos de tratamento confundem quem herda o projeto.
- **limites**: animar por baixo pode ser preparação útil para um corte; nesse caso, nomear.

### FAL-11 · FINAL no nome, sem aprovação

- **intenção**: marcar a versão a usar.
- **implementação**: `BASS PERSUADES · REEL · 7.68s · FINAL` e `REELS/09 · FINAL` [EV-R08-05], [EV-R09-01].
- **resultado observado**: o primeiro está na página de descartados; o segundo não tem publicação nem render encontrados [EV-R08-05], [EV-R09-01].
- **crítica**: não se aplica.
- **hipótese de causa**: o nome foi dado no momento da entrega, antes da revisão do usuário.
- **evidência da causa**: a página descartado guarda um FINAL [EV-R08-05].
- **correção proposta**: estado de aprovação fica no registro (`data/decisoes.toml`) com três níveis, não no nome da camada (DEC-13).
- **alteração realizada**: adotada nesta base.
- **resultado depois**: não se aplica.
- **aprovação**: não se aplica.
- **princípio**: aprovação tem evidência; nome de arquivo não é evidência.
- **limites**: publicado também não prova aprovação de todo detalhe.

### FAL-12 · alarmes falsos de QA

- **intenção**: verificar renders de forma automática.
- **implementação**: blackdetect, transcrição automática, inspeção de miniaturas [EV-IG-06], [EV-IG-07], [EV-R08-08].
- **resultado observado**: o blackdetect marca a placa preta de decisão do REELS/04; a transcrição troca Last.fm por "leis de FM"; numa miniatura a letra i parecia faltar [EV-IG-06], [EV-IG-07], [EV-R08-08].
- **crítica**: não se aplica; aconteceu nesta investigação.
- **hipótese de causa**: ferramentas medem sinal, não intenção; miniatura perde detalhe.
- **evidência da causa**: os três casos foram conferidos manualmente e eram falsos [EV-IG-06], [EV-R08-08].
- **correção proposta**: declarar intervalos intencionais na ferramenta, usar transcrição só para tempo e conferir defeitos em resolução cheia.
- **alteração realizada**: `tools/render_qa.py` aceita `--allow-black`; a qa de render lista falsos alarmes conhecidos.
- **resultado depois**: o REELS/04 passa na qa com o preto declarado.
- **aprovação**: não se aplica.
- **princípio**: medição automática acusa; olho humano decide.
- **limites**: declarar intencional demais esconde defeito; cada intervalo permitido precisa estar no mapa de beats.

### FAL-13 · texto que viaja em vez de ser lido

- **intenção**: hook com energia no começo do REELS/02 [EV-R02-09].
- **implementação**: palavras vindo de até 650 px, com escala e espalhamento depois [EV-R02-09].
- **resultado observado**: a versão ficou oculta como tratamento anterior [EV-R02-09].
- **crítica**: não acessível.
- **hipótese de causa**: deslocamento longo atrasa a leitura e compete com a fala.
- **evidência da causa**: a versão refinada reduz o deslocamento para 18 px e sincroniza cada palavra com a fala [EV-R02-09], [EV-R02-10].
- **correção proposta**: entrada curta, no tempo da palavra, bloco recua junto no fim (DEC-05).
- **alteração realizada**: feita; a refinada está no stage.
- **resultado depois**: publicado com o hook refinado [EV-IG-01].
- **aprovação**: resultado publicado.
- **princípio**: texto que se move é olhado; texto que assenta é lido.
- **limites**: em edição musical ou de jogo, gesto maior pode ser a ideia (ver FAL-02, limites).
