# Coffee Machine

API e domínio de uma máquina de café.

## Requisitos

- Python 3.13 ou superior
- [uv](https://docs.astral.sh/uv/) para instalar dependências e executar o projeto
- Docker e Docker Compose, somente para iniciar o PostgreSQL local

## Configuração e execução

Instale as dependências do projeto e do conjunto de testes:

```powershell
uv sync --group test
```

Inicie a API FastAPI com Uvicorn:

```powershell
uv run uvicorn main:app --reload
```

A aplicação fica disponível em <http://127.0.0.1:8000>. A documentação
interativa do FastAPI fica em <http://127.0.0.1:8000/docs>.


### PostgreSQL local

Para iniciar o PostgreSQL 16 definido no Docker Compose, crie o arquivo `.env` a partir do
exemplo e preencha as credenciais:

```powershell
Copy-Item .env.example .env
```

Defina `DB_USER`, `DB_PASSWORD` e `DB_NAME`. `DB_HOST` deve ser `127.0.0.1` e
`DB_PORT` deve corresponder à porta local publicada.
Depois, suba o serviço:

```powershell
docker compose up -d db
```

O banco pode ser acessado localmente em `127.0.0.1:<DB_PORT>`; os dados são
mantidos no volume Docker `coffee_machine_pgdata`.
```

## Testes

Execute toda a suíte com relatório de cobertura:

```powershell
uv run pytest
```

Para executar somente os testes de integração:

```powershell
uv run pytest -m integration --no-cov
```


## Arquitetura

```text
main.py
└── FastAPI
    └── routes/produtos.py 

Domínio (Python, em memória)
├── Catalogo/
│   ├── Bebida.py
│   └── CatalogoBebidas.py (catálogo e fábrica)
├── DTO/
│   ├── ItemDTO.py
│   └── PedidoDTO.py
├── Estoque/ (produtos e regras de quantidade)
├── services/
│   ├── Credito.py
│   ├── Pedido.py
│   └── Maquina.py
└── Excessoes/

Persistência preparada
├── database/ (Base, engine, sessão e ponto de inicialização)
└── models/ (Produto, Pedido, Estoque e Maquina)
```

### API e fluxo da aplicação

`main.py` instancia o `FastAPI` e inclui somente `produtos_router`. Hoje,
`GET /produtos/` responde com `{"mensagem": "Rota de produtos funcionando"}`;
não lista o catálogo. Os módulos de rotas de crédito, pedidos, operador, status
e troco contêm declarações incompletas e não são incluídos na aplicação.
Assim, esses caminhos não fazem parte da API servida atualmente.

As camadas de domínio são classes Python e operam em memória:

- `CatalogoBebidas` mantém as bebidas e permite busca e alteração de preço;
  `BebidaFactory` cria cópias de uma bebida do catálogo, inclusive com a
  quantidade de açúcar informada. O catálogo inicial contém café expresso,
  café longo, café com leite, cappuccino e chocolate quente.
- `ProdutoEstoque` define quantidades, capacidades, consumo e reabastecimento.
  Suas subclasses registram-se automaticamente, e `Estoque` instancia os tipos
  registrados. O estoque inicial de cada item começa cheio.
- `Credito` valida as denominações aceitas e o limite de R$ 50,00.
- `Pedido` agrega itens, preço e estoque; `Maquina` reúne estado, crédito,
  estoque, catálogo e operações de pedido/manutenção. Os estados são definidos
  por enumerações.
- Os DTOs em `src/DTO` representam os dados de pedido e seus itens.

Esses componentes não estão atualmente ligados às rotas expostas. As regras de
negócio e os estados esperados estão descritos em
[`docs/regras_negocio.md`](docs/regras_negocio.md), mas esse documento não
implica que todas as regras estejam implementadas ou acessíveis pela API.

### Persistência

O projeto prepara PostgreSQL 16 por Docker Compose, conexão via SQLAlchemy e
modelos declarativos para produto, pedido, estoque e máquina. As colunas de
valores monetários dos modelos usam `Numeric(10, 2)`/`Decimal`; os objetos de
domínio do catálogo e crédito usam valores numéricos Python em memória. As
variáveis de conexão estão exemplificadas em `.env.example`.

A persistência ainda não está conectada aos serviços ou às rotas; não há
criação automática do esquema nem migrações configuradas. Os modelos são,
portanto, uma estrutura de persistência preparada, não a fonte de estado usada
pela API atual.

## Decisões técnicas e histórico

- **Separação do domínio por responsabilidade:** catálogo, estoque, crédito,
  pedido e máquina ficam em módulos próprios. O histórico inclui a criação da
  máquina e do estoque (`15c6abc`, `8809833`) e a reorganização das rotas
  (`ea84bf1`).
- **Registro de produtos de estoque:** subclasses de `ProdutoEstoque` são
  descobertas pelo registro da classe base, evitando manter uma lista separada
  de classes no construtor do estoque (`8c3eb51`).
- **DTOs para pedidos:** os itens e pedidos têm estruturas de transferência
  próprias (`b53c3bc`), separadas das classes de domínio.
- **PostgreSQL e SQLAlchemy para persistência:** foram adicionados modelos
  relacionais (`98b0ab1`) e a configuração de conexão está preparada para
  variáveis de ambiente e execução local em contêiner. Essa escolha ainda não
  foi integrada ao fluxo da aplicação.
- **Testes automatizados com pytest:** a suíte contém testes unitários de
  domínio e teste de integração da aplicação ASGI; a configuração acompanha a
  cobertura de módulos selecionados e estabelece o mínimo de 75%
  (`7a1d091`).
- **Trunk Based Development:** o README anterior registra a transição de
  GitFlow para Trunk Based, motivada pela facilidade de integração. O histórico
  recente está na branch principal `main`.

O diagrama de ideias da arquitetura está disponível no
[tldraw](https://www.tldraw.com/f/OXgSun1dadWqt3JxqSMQL?d=v-49.294.1733.1617.page).

## Regras de negócio

As regras funcionais detalhadas, incluindo estados da máquina, valores de
crédito, pedidos, cancelamento, limpeza e manutenção, estão em
[`docs/regras_negocio.md`](docs/regras_negocio.md). Esse arquivo descreve o
comportamento esperado do produto; consulte a seção [Arquitetura](#arquitetura)
para distinguir esse escopo do que está ligado e disponível no código atual.
