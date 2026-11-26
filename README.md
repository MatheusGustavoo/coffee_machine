Link da ideia informal de arquitetura
https://www.tldraw.com/f/OXgSun1dadWqt3JxqSMQL?d=v-49.294.1733.1617.page

O versionamento começou pelo método GitFlow mas mudou para Trunk Based devido à facilidade de integração.

## Testes

Instale as dependências de teste e execute a suíte com cobertura:

```powershell
uv sync --group test
uv run pytest
```

A suíte exige pelo menos 75% de cobertura de linhas nos módulos de domínio e na
rota de produtos incluídos no escopo de testes.