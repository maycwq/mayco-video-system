# CLAUDE.md

as instruções valem para qualquer agente e estão em [AGENTS.md](AGENTS.md). leia esse arquivo primeiro.

particularidades para Claude Code:

- ao inspecionar Figma pelo MCP, use só leitura: `get_metadata`, `get_screenshot`, `use_figma` com scripts que não alteram nada (modelo em `tools/figma/inspect-stage.js`) e `export_video`. não crie, renomeie nem apague nós em arquivos de origem.
- `export_video` estoura o limite em stages longos; não insista, registre a pendência ([qa de render](docs/engenharia/qa-de-render.md)).
- links de screenshot e de export do Figma são temporários e não podem ir para o repositório.
- antes de commitar, rode `python3 tools/validate.py` e `python3 -m unittest discover -s tests`.
