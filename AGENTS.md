# instruções para agentes

vale para qualquer agente de IA que trabalhe com este repositório ou com edições do mayco. é curto de propósito: o conhecimento está em `docs/`, aqui está como usá-lo.

## antes de propor qualquer edição

1. leia o roteiro inteiro e, se houver, ouça a fala ou a música. monte o mapa de tempo com SRT revisado à mão ([processo](docs/metodo/processo.md)).
2. responda por escrito: o que é o assunto, onde ele acontece, que evidência real existe, qual a única coisa que precisa ficar.
3. escolha o ambiente com as perguntas de [ambiente](docs/metodo/ambiente.md). justifique. não abra janela de software se o assunto não vive em software.
4. só então leia os [estudos](docs/estudos/README.md) que tenham problema parecido, para aprender a decisão, não para copiar a forma.

## ao propor

entregue, nesta ordem:

- compreensão do assunto e a frase que precisa ficar;
- ambiente escolhido e por quê, com o que fica real, o que simplifica e quando o ambiente sai;
- mapa de beats com tempo final (e tempo da fonte, se houver pausas), estado do quadro e causa de cada mudança;
- papéis de texto e regra de convivência entre eles;
- vocabulário de motion do vídeo (poucos gestos, cada um com a pergunta que responde);
- áudio: fonte contínua, pausas, música, níveis;
- formatos e como cada um será recomposto;
- alternativas consideradas e por que foram descartadas;
- riscos de implementação e plano de QA ([qa de render](docs/engenharia/qa-de-render.md)).

## regras firmes

- não invente interface. se o ambiente é software, use o real; se não há real, mude o ambiente ([interfaces](docs/gramatica/interfaces.md)).
- não corte a fala para caber na edição; cubra (DEC-02).
- cursor só para ações, com o objeto acompanhando (DEC-04).
- tempo final mora num lugar só; legenda e keyframe ancorados na fala são convertidos antes de entrar ([tempo e playback](docs/engenharia/tempo-e-playback.md)).
- nada é dado como verificado sem render exportado e medido.
- "FINAL" no nome não é aprovação (DEC-13).
- Bootzy não é obrigatória; a família vem de quem fala no quadro ([tipografia](docs/gramatica/tipografia.md)).

## arquivos de origem

- arquivos Figma de origem são só leitura. experimentos vão para cópia ou arquivo novo ([Figma como motor](docs/engenharia/figma-como-motor.md)).
- nunca publique no repositório: vídeo, áudio, imagem, fonte tipográfica, conversa, link temporário, credencial, e-mail. o validador barra.

## escrita

português brasileiro, minúsculas em prosa, sem travessão, sem exclamação, frases diretas, raciocínio antes da resposta, identificadores técnicos intactos entre crases ([escrita](docs/metodo/escrita.md)). se o texto poderia ter sido escrito por qualquer um, reescreva.

## ao terminar um trabalho

registre estudo, evidências, decisões e falhas, e rode:

```bash
python3 tools/validate.py
python3 -m unittest discover -s tests
```

## quando a base não responde

diga que não responde, proponha com base no conteúdo e registre a lacuna em [lacunas](docs/fontes/lacunas.md). não estique uma regra para caber num caso que ela não cobre.
