# formatos: 16:9, 4:3 e 9:16

## o que o acervo fez

| reel | formato de origem | derivados | método | evidência |
|---|---|---|---|---|
| REELS/02 | 16:9 | 9:16 | recomposição com trajetórias próprias, com uma efêmera esquecida fora do quadro | [EV-R02-17], [EV-R02-18] |
| REELS/03 | 16:9 | 9:16 | troca de sidebars pelo estado recolhido do próprio UI3 | [EV-R03-02] |
| REELS/04 | 16:9 | 4:3, 9:16 | 4:3 corta o ambiente e reposiciona texto; 9:16 multiplica deslocamentos por 0,32 | [EV-R04-02], [EV-R04-11] |
| REELS/05 | 16:9 | 4:3, 9:16 | adaptação; 4:3 publicado | [EV-R05-01] |
| REELS/07 | 4:3 | 9:16 | recomposição com janelas na metade de baixo | [EV-R07-13] |
| REELS/09 | 9:16 | nenhum | nativo | [EV-R09-01] |

dois dos três publicados saíram em 4:3, e o 02 em 16:9 [EV-IG-01], [EV-IG-02], [EV-IG-03]. nenhum vertical aparece entre os publicados encontrados.

## a regra: recompor por beat

escalar a timeline inteira para outro formato quase nunca funciona, porque o que cabe ao lado num quadro largo precisa caber embaixo num quadro alto, e o que sangra num quadro some no outro. o caminho que o acervo sugere (DEC-12):

1. pegar o mapa de beats e, para cada beat, perguntar o que é protagonista e o que é apoio.
2. no vertical, o protagonista ocupa a largura toda; o apoio vai para cima ou para baixo.
3. a pessoa, quando é janela, fica alta e estreita; o conteúdo entra na metade de baixo, largo o bastante para sangrar [EV-R07-13].
4. usar estados compactos do próprio ambiente antes de cortar: painéis recolhidos, janelas empilhadas, listas em vez de grades [EV-R03-02].
5. reescrever trajetórias: o que ia para o lado passa a descer ou subir [EV-R02-17].
6. reposicionar legenda e texto para a área segura do formato (no vertical, acima da interface da plataforma).
7. rodar a checagem de limites: nenhum elemento ativo fora do quadro em nenhum beat (DEC-15) [EV-NOVA-02].

## checagem de limites

o REELS/02 vertical tem uma câmera rosa com a coordenada x do horizontal, fora de um quadro de 1080 de largura [EV-R02-18]. isso passa despercebido no editor quando o frame recorta o conteúdo. a checagem é mecânica: para cada nó visível com opacidade maior que zero em algum keyframe, comparar a caixa (com translação e escala dos keyframes) com o quadro. um script de leitura no Figma, no mesmo estilo de [inspect-stage.js](../../tools/figma/inspect-stage.js), resolve. a checagem pega elemento perdido; não pega composição ruim.

## escala proporcional: quando serve

multiplicar deslocamentos por uma razão (como o 0,32 do REELS/04) [EV-R04-11] serve para movimentos pequenos e simétricos, em que a direção não importa. não serve para movimentos que dependem da geometria do quadro (ir até a borda, sair do quadro, entrar do dock).

## 4:3

o 4:3 é o meio-termo: mantém leitura de interface horizontal e ocupa mais tela no feed. no REELS/04 o ambiente de 1920 de largura foi mantido e deslocado, cortando as bordas, enquanto hook, legenda e decisão foram reposicionados para o quadro de 1440 [EV-R04-02]. funciona quando o ambiente tem margem lateral sem informação.

ver também: [ambiente](../metodo/ambiente.md), FAL-07.
