# escolher ferramentas

o acervo foi feito no Figma, mas a linguagem não depende dele. uma limitação de ferramenta não vira regra estética: se uma ideia não cabe no Figma, a ideia muda de ferramenta, não de forma.

## critérios

| critério | pergunta |
|---|---|
| fidelidade visual | a interface e a tipografia saem exatamente como desenhadas? |
| controle temporal | dá para posicionar no milésimo e ver o tempo final? |
| áudio | mistura, nivela, sincroniza e exporta junto? |
| tipografia | usa a fonte certa no render, com acentos e kerning? |
| interfaces | reaproveita componentes reais ou exige redesenho? |
| render | qualidade, codec, duração sem falhas, tempo de render |
| inspeção | outra pessoa ou agente consegue ler o projeto sem abrir a ferramenta? |
| estabilidade | o mesmo projeto renderiza igual amanhã? |
| manutenção | mudar uma frase obriga a refazer quanto? |
| experimentação | testar variações é barato? |
| custo e limites | licença, máquina, tempo, limites de exportação |
| direitos | fontes e mídias podem ser usadas nesse pipeline? |

## comparação

| ferramenta | serve bem para | fraca em | no acervo |
|---|---|---|---|
| Figma (timeline nativa) | interface fiel, tipografia como layout, componentes de biblioteca, direção visual inspecionável | áudio, várias fontes de vídeo, renders longos, fontes proprietárias no render | todos os stages [EV-ENG-02] |
| FFmpeg | montar master, pausas, congelamentos, mix e nível de áudio, conversões, QA automatizado | qualquer coisa de layout | usado nesta investigação para QA [EV-R07-15] |
| editor de vídeo (DaVinci Resolve, Premiere, Final Cut) | montagem com cortes, cor, áudio, legenda, master final | interface fiel e tipografia de layout | o master do REELS/07 veio de fora do Figma [EV-R07-03] |
| After Effects | motion complexo, máscaras, rastreamento, expressões | inspeção por terceiros, custo, versionamento | não usado |
| código (Remotion, Motion Canvas) | motion programático, versões e formatos gerados, dados reais, testes | curva de entrada, tipografia proprietária precisa ser carregada | não usado |
| SVG, Canvas, WebGL | partes específicas: tipografia cinética, partículas, shaders | montar um vídeo inteiro sozinho | não usado |
| transcrição (whisper e similares) | tempo de palavra, conferência de sincronia | nomes próprios, marcas | usado nesta investigação [EV-IG-07] |

## combinações que fazem sentido

- **Figma + master externo**: layout e animação no Figma, tempo e áudio resolvidos num master de editor ou FFmpeg (o caminho do REELS/07) [EV-R07-03].
- **Figma para direção, código para render**: o Figma define quadros-chave e regras; um projeto em código gera as variações e formatos. bom quando há muitas versões ou formatos.
- **editor como montagem final**: exportar camadas do Figma com transparência e montar no editor, quando cor e áudio pedem controle fino.

## como decidir

1. listar o que o vídeo precisa que seja exato: interface? tipografia? sincronia com música? cor de pele?
2. para cada item, escolher a ferramenta que o faz melhor.
3. minimizar as passagens entre ferramentas; cada passagem é um lugar onde o tempo pode desalinhar.
4. decidir onde mora o **tempo final**: um só lugar. todo o resto se ajusta a ele.
5. definir como o resultado será validado ([qa de render](qa-de-render.md)) antes de construir.

registrar a escolha e o porquê no estudo do trabalho.
