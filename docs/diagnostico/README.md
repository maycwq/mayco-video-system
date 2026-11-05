# diagnóstico por sintoma

comece pelo que você está vendo ou ouvindo. cada linha leva a uma pergunta que separa causas parecidas e aos estudos de falha relacionados.

## imagem e composição

| sintoma | primeira pergunta | ver |
|---|---|---|
| parece wireframe ou template | os elementos vêm de um ambiente real ou da ideia, ou de uma grade decidida antes do conteúdo? | FAL-01, [composição](../gramatica/composicao.md) |
| caixas e cartões em tudo | o objeto real tem caixa? | FAL-01, [interfaces](../gramatica/interfaces.md) |
| ícones genéricos de interface | existe um objeto real ou uma interface real que diga isso? | FAL-01 |
| interface que não existe em nenhum sistema | qual é o ambiente real do assunto? | [ambiente](../metodo/ambiente.md) |
| efeito competindo com o assunto | o efeito responde a alguma das quatro perguntas do motion? | FAL-02, [motion](../gramatica/motion.md) |
| tudo do mesmo tamanho | qual é a prova deste beat? | [composição](../gramatica/composicao.md) |
| cor sem motivo | que estado essa cor marca? | [cor e matéria](../gramatica/cor-e-materia.md) |

## texto

| sintoma | primeira pergunta | ver |
|---|---|---|
| tipografia genérica | a família vem de quem fala no quadro? cada papel de texto tem código próprio? | [tipografia](../gramatica/tipografia.md) |
| legenda brigando com texto editorial | os dois papéis usam o mesmo código no mesmo instante? | FAL-09 |
| texto difícil de ler | ele se move enquanto deveria ser lido? tem contraste no frame mais claro do trecho? | FAL-13 |
| acento ou pontuação errados no render | o texto está como forma conferida em resolução cheia? | FAL-04 |
| fonte trocada no render | a fonte é proprietária? o texto final foi convertido? | FAL-04 |

## motion

| sintoma | primeira pergunta | ver |
|---|---|---|
| animação genérica | toda palavra entra do mesmo jeito? | FAL-02, FAL-13 |
| rotação sem propósito | a rotação vira eixo, peso ou ação? | FAL-02, [motion](../gramatica/motion.md) |
| cursor desacoplado | o objeto acompanha o cursor no mesmo caminho e tempo? o cursor está executando uma ação? | [interfaces](../gramatica/interfaces.md) |
| janela pula de lugar | alguém arrastou? ela saiu e voltou? | [interfaces](../gramatica/interfaces.md) |
| movimento que ninguém vê | está sob alguma cobertura? | FAL-10 |

## tempo, áudio e playback

| sintoma | primeira pergunta | ver |
|---|---|---|
| preto a partir de um instante | o instante coincide com a duração da fonte? alguma camada está em tempo da fonte? | FAL-03, [tempo e playback](../engenharia/tempo-e-playback.md) |
| playback incompleto | o master sozinho está completo? | FAL-03 |
| legenda adiantada ou atrasada depois de um ponto | há pausa inserida antes desse ponto? a legenda foi convertida para tempo final? | [tempo e playback](../engenharia/tempo-e-playback.md) |
| fala some quando o ambiente cobre a pessoa | a fonte foi removida ou só coberta? | FAL-06 |
| música alta demais | quanto acima da fala, medido? | FAL-08 |
| duração diferente do planejado | a diferença é de um ou dois quadros? | [qa de render](../engenharia/qa-de-render.md) |

## render e formato

| sintoma | primeira pergunta | ver |
|---|---|---|
| render diferente do editor | o defeito aparece no export? em qual grupo de camadas? | FAL-05 |
| exportação falha ou trava | quais camadas são maiores que o quadro ou têm vídeo? | FAL-05 |
| elemento sumiu no vertical | a coordenada veio do horizontal? | FAL-07 |
| vertical parece um crop | cada beat foi recomposto? o ambiente tem estado compacto próprio? | FAL-07, [formatos](../engenharia/formatos.md) |
| proporção errada | o quadro raiz e o export têm o tamanho certo? | [qa de render](../engenharia/qa-de-render.md) |

## processo

| sintoma | primeira pergunta | ver |
|---|---|---|
| "FINAL" que ninguém aprovou | onde está a evidência de aprovação? | FAL-11 |
| alarme de QA que não é defeito | o intervalo está previsto no mapa de beats? | FAL-12 |
| referência mal interpretada | a referência está na fala? quem assiste entende sem conhecer? | [narrativa e humor](../gramatica/narrativa-e-humor.md) |

os estudos completos estão em [falhas](falhas.md).
