# ferramentas

cada ferramenta resolve um problema que aconteceu no acervo ou nesta reconstrução. todas usam só a biblioteca padrão do python 3.11+; `render_qa.py` chama ffprobe e ffmpeg.

| ferramenta | problema que resolve | uso |
|---|---|---|
| `validate.py` | base que apodrece: citação para evidência que não existe, link quebrado, documento órfão, número sem fonte, estudo de falha incompleto, escrita fora do tom, mídia ou credencial publicada por engano | `python3 tools/validate.py [--report]` |
| `render_qa.py` | render que difere da timeline: duração, tamanho, preto, congelamento, silêncio, loudness, nível de fala x música | `python3 tools/render_qa.py arquivo.mp4 [opções]` |
| `timeline_map.py` | confusão entre tempo da fonte e tempo final em edições com pausas inseridas | `python3 tools/timeline_map.py plano.toml --tabela` |
| `figma/inspect-stage.js` | ler um stage do Figma sem abrir o editor e sem alterar nada | colar no `use_figma` do Figma MCP, ajustar ids |
| `exemplos/plano-insercoes.toml` | exemplo de plano para o mapa de tempo | ver [tempo e playback](../docs/engenharia/tempo-e-playback.md) |

## o que o validador checa

1. registros em `data/`: campos obrigatórios, classes e níveis de aprovação válidos, ids únicos, referências entre registros.
2. citações nos markdown: todo `EV-`, `DEC-`, `FAL-` e `S-` existe.
3. links relativos e âncoras.
4. documentos órfãos: todo `.md` em `docs/` alcançável a partir do README.
5. afirmações sem evidência: nos estudos, na gramática e no capítulo do ambiente, blocos com medida (s, px, dB, LUFS) ou node id citam evidência.
6. estudos de falha com os doze campos.
7. escrita: travessão, frase começando com maiúscula, termos que o manual evita (fora de crase), exclamação (aviso).
8. publicação: extensões de mídia, fonte e pdf; arquivos acima de 1 MB; urls assinadas e temporárias; tokens; e-mails.

saída com código 1 se houver erro. avisos não falham: hoje avisam exclamação e evidência registrada mas não citada.

## testes

```bash
python3 -m unittest discover -s tests -v
```

os testes do `render_qa.py` geram um vídeo sintético com ffmpeg (cor, preto, cor; tom, silêncio, tom) e pulam se ffmpeg não estiver instalado.
