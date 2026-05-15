# Odin-s-Opera
📜 Protocolo "Ópera de Odin": Configuração do Conselho de Asgard
A Ópera de Odin agora inclui a camada de entrega final. O fluxo segue o padrão de automação de ciclo de vida (SDLC), onde a inteligência evolui do requisito ao deploy sem intervenção manual.

 O Elenco Atualizado
Odin (Product Manager): Define o PRD (prd.md).

Loki (Architect): Desenha o sistema (system_design.md).

Hella (Project Manager): Organiza o cronograma (tasks.json).

Thor (Engineer): Forja o código na pasta code/.

Freya (QA Engineer): Valida a precisão em tests/.

Heimdall (Scribe & Gatekeeper): Vigia as Crônicas e protege os segredos no .env.

Tyr (DevOps Engineer): O executor do deploy. Ele possui autoridade total para publicar o app em produção assim que os portões por Freya forem abertos.

1. Visão Geral: Ópera de Odin
A Ópera de Odin é um ecossistema de orquestração de Inteligência Artificial baseado no modelo de Sistemas Multiagentes (MAS). O objetivo é automatizar o Ciclo de Vida de Desenvolvimento de Software (SDLC) através de uma equipe de agentes autônomos que simulam os papéis de uma empresa de tecnologia. O sistema opera sob a filosofia de que o código é o resultado de procedimentos operacionais padrão (SOP) rigorosamente seguidos por especialistas digitais.  

2. O Conselho de Asgard (Papéis e Agentes)
O sistema utiliza sete personas baseadas na mitologia nórdica, cada uma com responsabilidades específicas dentro do fluxo de desenvolvimento:

Odin (Product Manager): Responsável pela visão estratégica, criando o Documento de Requisitos do Produto (PRD) e definindo as user stories.

Loki (Architect): Elabora o desenho técnico do sistema, escolhe as APIs (como Google Routes e Inmetro) e define os diagramas de fluxo.

Hella (Project Manager): Gerencia o cronograma, decompõe a arquitetura de Loki em tarefas granulares e monitora o progresso.

Thor (Engineer): O executor técnico que utiliza Python para implementar a lógica de cálculo e a interface visual em Streamlit.

Freya (QA Engineer): Garante a qualidade através de testes automatizados e validação dos critérios de aceitação definidos por Odin.

Heimdall (Scribe & Gatekeeper): Atua como cronista da orquestração e guardião da segurança, gerenciando segredos em arquivos .env e protegendo chaves de API.

Tyr (DevOps Engineer): Possui autoridade para realizar o deploy autônomo da aplicação em ambientes de nuvem assim que os portões de qualidade de Freya forem aprovados.  

3. Stack Tecnológica e Linguagens
A infraestrutura da Ópera de Odin foi construída sobre tecnologias modernas de 2025/2026:

Linguagem Base: Python 3.11/3.12.

Framework de Orquestração: CrewAI, escolhido por sua modularidade e facilidade de configuração em ambientes de nuvem.

Cérebro (LLM): Google Gemini 1.5/2.0 Flash, acessado via API para processamento de contexto amplo e raciocínio lógico.

Infraestrutura: GitHub Codespaces, fornecendo um ambiente Linux isolado e reprodutível.

Documentação: Markdown, utilizado como linguagem nativa para comunicação entre agentes e geração de artefatos.

Dependência Crítica: pysqlite3-binary para emular o SQLite 3.35+ exigido pelo banco de dados vetorial ChromaDB no Codespaces.

4. Como e Onde Usar
Onde usar:
A Ópera de Odin é ideal para automação de DevOps Agêntico, prototipagem rápida de MVPs, e sistemas que exigem integração complexa de múltiplas APIs onde a decisão do caminho de execução deve ser dinâmica e não baseada em scripts rígidos.  

Como operar:

Preparação: O ambiente deve ser configurado no Codespaces com as extensões de Python e a permissão python.terminal.useEnvFile habilitada.

Segurança: As chaves de API (Gemini, Google Maps, tokens de deploy) devem ser inseridas no arquivo odins_opera/config/.env, protegido pelo .gitignore.

Execução: A orquestração é disparada pelo comando python3 odins_opera/code/orchestrator.py, que inicia o fluxo sequencial onde o output de um agente (ex: Odin) alimenta automaticamente o input do próximo (ex: Loki).

Autonomia: O sistema é configurado para ser "Hands-off", onde Tyr realiza o deploy final sem intervenção humana se todos os validadores de Freya passarem.

Esta orquestração transforma o desenvolvedor de um "escritor de linhas de código" em um "diretor de inteligência", focando na definição da intenção e na supervisão estratégica do conselho de agentes.
