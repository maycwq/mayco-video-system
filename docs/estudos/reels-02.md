# REELS/02 · a vida inteira em apps diferentes

## identificação

- **assunto**: mayco está construindo um app (a olue) pra quem registra a vida em vários apps; a música fica num lugar, os filmes em outro, as fotos em outro.
- **formato publicado**: 16:9, 35,933 s, publicado em 15/08 [EV-IG-01].
- **stages no Figma**: V0 `239:6876`, horizontal `188:2964`, vertical `1638:3389` [EV-R02-01].
- **fonte**: um take contínuo de talking head de 35,9 s [EV-R02-03].
- **render original citado no pedido**: não acessível. o relato fala em 1920x1080 e ~35,947 s [EV-PREP-01]; o publicado tem 1916x1078 e 35,933 s, e a causa dos 4 px a menos não foi identificada [EV-ENG-04].

## o argumento

a fala inteira, reconstruída pelos nomes das legendas e pela transcrição:

> estou construindo um app pra garotas e gays que registram a vida inteira em apps diferentes. pra lembrar quem eu fui em março, eu precisei abrir o last.fm, o letterboxd e minhas fotos. a música lembrava o clima, os filmes lembravam o que ocupava a minha cabeça e as fotos lembravam o que de fato estava acontecendo. cada lugar tinha uma parte, mas nenhum tinha o mês inteiro. e eu não quero só colocar play, nota e foto na mesma tela. quero aproximar essas coisas do contexto em que elas fizeram sentido. e é esse o problema que eu estou tentando resolver. se parece um app que você também gostaria de ter, eu vou mostrando por aqui enquanto ele ganha forma.

a única coisa que precisa ficar: a memória de um mês está espalhada, e juntar não é empilhar. o vídeo inteiro serve a essa frase.

## anatomia por beat

| tempo | estado do quadro | o que move a mudança | evidência |
|---|---|---|---|
| 0 a 0,88 s | talking head em tela cheia | começo da fala | [EV-R02-03] |
| 0,88 a 5,4 s | a pessoa vira janela de macOS sobre um desktop real; hook em Bootzy entra palavra por palavra; teaser do Figma com a tela real da comunidade ao lado | a fala anuncia o app | [EV-R02-09], [EV-R02-14] |
| 5,12 a 6,02 s | um ponteiro real clica no botão amarelo e a janela da pessoa minimiza pro dock | "pra lembrar quem eu fui" muda de assunto: sai a pessoa, entra o lugar onde a memória está | [EV-R02-05] |
| 6,02 a 16,92 s | desktop com Last.fm, Letterboxd e Photos abrindo no tempo dos nomes; foco alterna entre janelas; indicadores do dock acendem | cada app entra quando é dito | [EV-R02-06], [EV-R02-07], [EV-R02-08] |
| 17,24 a 20,14 s | superfície teal toma o quadro; fragmentos das janelas afundam; "cada lugar tinha uma parte / mas nenhum tinha o mês inteiro" | a fala sai do concreto e vira abstração | [EV-R02-11] |
| 20,6 a 23,3 s | cd holográfico, botão estrela e câmera rosa com rótulos "play", "nota", "foto" | "não quero só colocar play, nota e foto na mesma tela" | [EV-R02-12] |
| 23,6 a 27,08 s | três gravações reais do app entram escalonadas sobre o teal | "aproximar essas coisas do contexto" | [EV-R02-13] |
| 27,08 a 33,05 s | as telas encolhem e saem; a pessoa volta como janela e cresce até a tela cheia | "é esse o problema que eu estou tentando resolver" | [EV-R02-03], [EV-R02-13] |
| 33 a 35,9 s | talking head em tela cheia, legenda branca | convite | [EV-IG-04] |

o desenho espacial acompanha a ideia em cinco estados: pessoa, lugar, abstração, produto, pessoa. cada passagem tem uma causa visível no quadro (um clique, um nome dito, uma frase que muda de nível).

## o ambiente

o vídeo fala de apps, então o quadro é o computador onde esses apps vivem. o desk usa wallpaper, menu bar, dock e controles do macOS 26 da biblioteca comunitária; Last.fm, Letterboxd e Photos entram como janelas com conteúdo real; o teaser do Figma mostra a tela real da comunidade, com uma camada que diz literalmente `NO INVENTED UI` [EV-R02-06], [EV-R02-14].

dois detalhes mostram o nível de fidelidade pedido. os indicadores de app aberto no dock acendem quando o Safari e o Photos entram em cena, como no sistema de verdade [EV-R02-06]. a minimização da pessoa acontece por um clique no botão amarelo, não por um zoom solto [EV-R02-05].

o ambiente também sabe sair. quando a fala vira abstração em 17,24 s, o desktop quebra e uma superfície autoral teal assume [EV-R02-11]. o desktop não volta: o resto do argumento não é mais sobre os apps antigos, é sobre o que mayco está construindo. ver [ambiente](../metodo/ambiente.md).

## tipografia

- **hook**: Bootzy em amarelo sobre a janela do Figma, uma palavra por vez no tempo da fala, com "app" maior [EV-R02-09], [EV-R02-10].
- **legendas**: uma palavra por vez, centralizadas embaixo, em glifos vetoriais de Bootzy; a cor muda conforme o fundo: preta no desktop claro, branca no rosto e no teal, amarela sobre as telas do app [EV-R02-15], [EV-IG-04].
- **texto editorial**: "cada lugar tinha uma parte / mas nenhum tinha o mês inteiro" em Bootzy branco sobre teal, com versão anterior guardada oculta [EV-R02-11].
- **rótulos**: "play", "nota", "foto" presos aos objetos, não soltos [EV-R02-12].

um ponto de atenção visto no publicado: em ~18,6 s a legenda "o", grande e branca, cai em cima do bloco editorial na mesma família e cor, e por um instante as duas camadas disputam leitura [EV-IG-05]. não há registro de crítica sobre isso. vale como lembrete de que legenda e texto editorial precisam de regra de convivência (ver [tipografia](../gramatica/tipografia.md)).

## motion

o melhor exemplo do vídeo está no hook. o arquivo guarda as duas versões lado a lado. a anterior fazia cada palavra viajar até 650 px, crescer e depois se espalhar. a refinada faz cada palavra subir 18 px e aparecer em 0,18 s, no instante em que é dita, e o bloco inteiro recua junto quando a frase termina [EV-R02-09]. a transcrição confirma a sincronia, com diferenças de no máximo 0,07 s [EV-R02-10]. menos deslocamento, mais leitura, e a fala comanda.

outros padrões do vídeo:

- janelas entram de onde vêm. o Last.fm sai do dock (posição baixa, escala 0,58) e o Photos de fora do quadro [EV-R02-07].
- foco entre janelas por opacidade e escala, não por movimento grande [EV-R02-07].
- o ponteiro aparece só para executar ações do sistema e clica com uma compressão curta de escala [EV-R02-05], [EV-R02-07].
- efêmeras respiram devagar, poucos pixels e pouco mais de um grau, e as que atravessam a transição recebem o nome de sobreviventes [EV-R02-16].

## áudio e tempo

a fonte nunca é cortada. ela some do quadro entre 6,02 e 27,08 s por opacidade, não por remoção, e a fala segue contínua no publicado [EV-R02-03], [EV-IG-10]. a V0 cobria a pessoa com um retângulo opaco cujo nome dizia que o talking head nunca podia vazar; o stage atual troca isso por uma cobertura transparente e um gate de opacidade na própria fonte [EV-R02-04]. a leitura mais provável é o princípio que o relato chama de `COVERED ≠ REMOVED`: cobrir a imagem sem perder a camada nem o áudio [EV-R02-19], [EV-PREP-01].

as legendas carregam no nome o tempo de cada palavra em milésimos e o grupo se chama `SRT SOURCE OF TRUTH` [EV-R02-15]. a timeline inteira se organiza a partir desses tempos.

## engenharia

- stage é um frame de 1920x1080 com camadas por beat nomeadas com o intervalo em segundos [EV-R02-02].
- fonte em video fill, gravações do produto em video fill dentro de `Media/Slot` do design system [EV-R02-13].
- legendas e hook em glifos vetoriais Bootzy, com mestres guardados num frame oculto marcado `do not export` [EV-R02-15].
- keyframes manuais por propriedade, com HOLD para cortes [EV-ENG-02].

## versão vertical

o vertical não é um crop. a fonte desce em vez de ir pro lado, as janelas do workspace ficam empilhadas, o ponteiro tem outro caminho e o hook ganha outro layout [EV-R02-17]. mesmo assim, a câmera rosa ficou com a coordenada do horizontal e está fora do quadro de 1080 de largura [EV-R02-18]. é o tipo de erro que só uma checagem de limites por beat pega (ver [formatos](../engenharia/formatos.md) e FAL-07).

## aprovações e pendências

- **resultado**: publicado em 16:9 [EV-IG-01]. isso confirma uso, não confirma que todo detalhe foi aprovado.
- **direção e implementação**: não verificáveis sem as conversas.
- **pendente**: o vertical não foi publicado; a câmera fora do quadro não foi corrigida no arquivo; a causa do 1916x1078 é desconhecida.

## o que transfere

- quando o assunto é software, o quadro é o software de verdade, com os comportamentos reconhecíveis do sistema (DEC-03).
- o ambiente sai quando o argumento sai dele, e a saída tem cara de decisão, não de transição genérica (DEC-06).
- palavra dita e evento visual coincidem; a fala é o relógio (DEC-01).
- texto editorial entra pequeno e no tempo da fala (DEC-05).
- a fonte falada fica contínua por baixo do que a cobre (DEC-02).

## o que não transfere

- o teal, o amarelo do hook e as efêmeras holográficas são escolhas deste vídeo. não são paleta nem kit obrigatório.
- o desktop do macOS faz sentido porque a fala cita apps. um vídeo pessoal sobre outra coisa não deveria abrir janela nenhuma.
- cinco estados espaciais funcionaram para 36 s de argumento em três tempos. um vídeo de 8 s com uma ideia só precisa de um ou dois.

## fontes

S-FIG-PRINCIPAL (página `182:2964`), S-IG-A, S-QA-LOCAL, S-PREP.
