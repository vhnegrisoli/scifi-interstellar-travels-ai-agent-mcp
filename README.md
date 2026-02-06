# 🚀 Sci-Fi Interstellar Travels AI Agent MCP

Agente de IA inteligente que utiliza o **Model Context Protocol (MCP)** para consultar uma API sobre mecanismos de viagens interestelares em obras de ficção científica. O projeto demonstra uma arquitetura completa com API REST, servidor MCP e agente de IA conversacional.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia     | Versão  | Uso                    |
| -------------- | ------- | ---------------------- |
| Python         | 3.8+    | Linguagem principal    |
| FastAPI        | 0.116.1 | Framework web          |
| Uvicorn        | 0.35.0  | Servidor ASGI          |
| OpenAI         | -       | Modelo de linguagem    |
| MCP            | 1.26.0  | Model Context Protocol |
| FastMCP        | 2.14.5  | Framework MCP          |
| Strands Agents | 1.24.0  | Framework de agentes   |
| Requests       | 2.32.5  | Cliente HTTP           |

## 📋 Sobre o Projeto

Este projeto explora diferentes tecnologias de viagem interestelar presentes em obras clássicas de ficção científica como **Star Wars**, **Star Trek**, **Duna**, **Fundação** e **Interestelar**. O sistema permite que um agente de IA consulte informações sobre esses mecanismos de viagem através de um servidor MCP que se comunica com uma API REST.

### 🎯 Funcionalidades

- 🔍 Buscar viagens interestelares por ID, tipo ou obra
- 📚 Consultar informações sobre diferentes mecanismos FTL (Faster Than Light)
- 🤖 Interagir com um agente de IA que entende o contexto das viagens espaciais
- 🌐 API REST completa com arquitetura em camadas
- 🔌 Servidor MCP para integração com agentes de IA

---

## 🏗️ Arquitetura do Projeto

```
interstellar_travel_mcp_ai_agent/
├── 🤖 ftl_agent/                 # Agente de IA
├── 🔌 ftl_travel_mcp_server/     # Servidor MCP
└── 🌐 interstellar_api/          # API REST
```

---

## 📦 Módulos e Responsabilidades

### 🤖 **ftl_agent/** - Agente de IA

O agente de IA é o componente conversacional do sistema que interage com usuários através de linguagem natural.

**Responsabilidades:**
- Processar perguntas dos usuários sobre viagens interestelares
- Comunicar-se com o servidor MCP para obter informações
- Gerar respostas contextualizadas e inteligentes
- Manter o contexto da conversa

**Tecnologias:**
- `strands-agents[openai]` - Framework para criação de agentes de IA
- `strands-agents-tools` - Ferramentas auxiliares para agentes
- `fastmcp` - Cliente MCP para comunicação com o servidor
- `python-dotenv` - Gerenciamento de variáveis de ambiente
- `OpenAI` - Modelo de linguagem para processamento

**Arquivos:**
- `agent.py` - Implementação do agente de IA
- `model.py` - Modelos de dados do agente
- `.env` - Configurações (API keys, modelo)
- `requirements.txt` - Dependências Python

---

### 🔌 **ftl_travel_mcp_server/** - Servidor MCP

O servidor MCP (Model Context Protocol) atua como uma ponte entre o agente de IA e a API REST, expondo ferramentas que o agente pode utilizar.

**Responsabilidades:**
- Expor ferramentas (tools) para o agente de IA
- Fazer requisições HTTP para a API REST
- Transformar dados da API em formato consumível pelo agente
- Gerenciar a comunicação via protocolo MCP

**Tecnologias:**
- `mcp` - Implementação do Model Context Protocol
- `fastmcp` - Framework para criar servidores MCP rapidamente
- `requests` - Cliente HTTP para comunicação com a API
- `python-dotenv` - Gerenciamento de variáveis de ambiente

**Ferramentas Expostas:**
1. `get_db_schema()` - Retorna estrutura do banco (IDs, tipos, obras)
2. `find_by_id(id)` - Busca viagem por identificador único
3. `find_by_type(type)` - Busca viagens por tipo (ex: "Warp Drive")
4. `find_by_work(work)` - Busca viagens por obra (ex: "Star Wars")

**Arquivos:**
- `mcp_server.py` - Servidor MCP com definição das ferramentas
- `mcp_client.py` - Cliente MCP para testes
- `requirements.txt` - Dependências Python

---

### 🌐 **interstellar_api/** - API REST

API REST completa construída com FastAPI, seguindo arquitetura em camadas para organização e manutenibilidade.

**Responsabilidades:**
- Fornecer endpoints HTTP para consulta de dados
- Gerenciar o banco de dados JSON
- Implementar lógica de negócio
- Validar e serializar dados

**Tecnologias:**
- `FastAPI` - Framework web moderno e rápido
- `Uvicorn` - Servidor ASGI de alta performance
- `python-dotenv` - Gerenciamento de variáveis de ambiente

**Arquitetura em Camadas:**

#### 📂 **database/**
Camada de persistência e acesso aos dados.
- `db.py` - Inicialização e conexão com o banco
- `interstellar_db.json` - Banco de dados JSON com informações das viagens

#### 📊 **model/**
Modelos de dados e schemas Pydantic.
- `interstellar_model.py` - Definição do modelo InterstellarTravelModel

#### 🗄️ **repository/**
Camada de acesso aos dados (Data Access Layer).
- `interstellar_repository.py` - Queries e operações no banco de dados

#### 🔧 **service/**
Lógica de negócio da aplicação.
- `interstellar_service.py` - Regras de negócio e orquestração

#### 🛣️ **route/**
Definição dos endpoints da API.
- `interstellar_route.py` - Rotas HTTP e controllers

**Endpoints Disponíveis:**
- `GET /api/interstellar/info` - Retorna IDs, tipos e obras disponíveis
- `GET /api/interstellar/id/{id}` - Busca por ID específico
- `GET /api/interstellar/type/{type}` - Busca por tipo de viagem
- `GET /api/interstellar/work/{work}` - Busca por obra de ficção

**Arquivos:**
- `app.py` - Aplicação FastAPI principal
- `requirements.txt` - Dependências Python

---

## 🗃️ Banco de Dados

O banco de dados contém informações sobre 6 tipos de viagens interestelares:

| ID                                 | Tipo                  | Obra         | Descrição                       |
| ---------------------------------- | --------------------- | ------------ | ------------------------------- |
| `duna_holtzman_foldspace`          | Dobra do Espaço       | Duna         | Efeito Holtzman com Navegadores |
| `foundation_hyperspace_jump`       | Salto pelo Hiperspaço | Fundação     | Dimensão alternativa            |
| `star_wars_hyperspace`             | Hiperespaço           | Star Wars    | Dimensão paralela               |
| `star_trek_warp_drive`             | Warp Drive            | Star Trek    | Campo de dobra espacial         |
| `interstellar_wormhole`            | Buraco de Minhoca     | Interestelar | Conexão espaço-temporal         |
| `interstellar_relativistic_travel` | Viagem Relativística  | Interestelar | Dilatação temporal              |

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- pip

### 1️⃣ Executar a API REST

```bash
cd interstellar_api
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

A API estará disponível em `http://localhost:8000`

### 2️⃣ Executar o Servidor MCP

```bash
cd ftl_travel_mcp_server
pip install -r requirements.txt

# Configure o .env com:
# INTERSTELLAR_API_BASE_URL=http://localhost:8000/api/interstellar
# HOST=localhost
# PORT=3000

python mcp_server.py
```

O servidor MCP estará disponível em `http://localhost:3000`

### 3️⃣ Executar o Agente de IA

```bash
cd ftl_agent
pip install -r requirements.txt

# Configure o .env com:
# OPENAI_KEY=sua-chave-aqui
# OPENAI_MODEL=gpt-4-mini

python agent.py
```

---

## 🔧 Configuração

### Variáveis de Ambiente

**ftl_agent/.env**
```env
OPENAI_KEY=sua-chave-openai
OPENAI_MODEL=gpt-4-mini
```

**ftl_travel_mcp_server/.env**
```env
INTERSTELLAR_API_BASE_URL=http://localhost:8000/api/interstellar
HOST=localhost
PORT=3000
```

---

## 💡 Exemplos de Uso

### Consultar via API REST
```bash
# Listar todas as informações disponíveis
curl http://localhost:8000/api/interstellar/info

# Buscar por obra
curl http://localhost:8000/api/interstellar/work/Star%20Wars

# Buscar por tipo
curl http://localhost:8000/api/interstellar/type/Warp%20Drive
```

### Interagir com o Agente de IA
```
Usuário: "Me fale sobre as viagens em Star Wars"
Agente: [Consulta o MCP e retorna informações sobre hiperespaço]

Usuário: "Qual a diferença entre Warp Drive e Hiperespaço?"
Agente: [Compara os dois mecanismos usando dados da API]
```

---

## 📚 Conceitos Importantes

### O que é MCP (Model Context Protocol)?
O MCP é um protocolo que permite que modelos de IA (como GPT-4) acessem ferramentas e dados externos de forma estruturada. Ele define como agentes de IA podem descobrir e usar ferramentas disponíveis.

### Por que usar MCP?
- ✅ Padronização na comunicação entre IA e ferramentas
- ✅ Descoberta automática de capacidades
- ✅ Separação de responsabilidades
- ✅ Escalabilidade e manutenibilidade

### Arquitetura em Camadas
A API segue o padrão de arquitetura em camadas:
- **Route** → Recebe requisições HTTP
- **Service** → Processa lógica de negócio
- **Repository** → Acessa dados
- **Database** → Armazena informações

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Adicionar novas viagens interestelares
- Melhorar a documentação
- Implementar novos endpoints
- Otimizar o código

---

## 📄 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

---

## 🌟 Créditos

Inspirado nas obras de ficção científica:
- **Duna** - Frank Herbert
- **Fundação** - Isaac Asimov
- **Star Wars** - George Lucas
- **Star Trek** - Gene Roddenberry
- **Interestelar** - Christopher Nolan

---

**Feito com ❤️ e ☕ para explorar o universo da ficção científica através da tecnologia!**
