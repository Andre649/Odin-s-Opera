__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv('odins_opera/config/.env')

gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

odin = Agent(
    role="Product Manager",
    goal="Definir PRD e objetivos estratégicos do app de impacto de CO2 no Brasil",
    backstory="O Pai de Todos, mestre em transformar ideias em requisitos sólidos e viáveis.",
    llm=gemini_llm,
    verbose=True
)

loki = Agent(
    role="Architect",
    goal="Desenhar a arquitetura técnica e fluxos de integração do Inmetro e Google Routes",
    backstory="O Estrategista, perito em projetar sistemas complexos com APIs externas.",
    llm=gemini_llm,
    verbose=True
)

hella = Agent(
    role="Project Manager",
    goal="Organizar a ordem das tarefas e monitorar o progresso do desenvolvimento",
    backstory="A Deusa do Reino, responsável por garantir que Thor não inicie sem Loki.",
    llm=gemini_llm,
    verbose=True
)

thor = Agent(
    role="Engineer",
    goal="Implementar a lógica de cálculo em Python e a interface visual no Streamlit",
    backstory="O Executor, que usa seu martelo de código para forjar aplicações robustas.",
    llm=gemini_llm,
    verbose=True
)

freya = Agent(
    role="QA Engineer",
    goal="Validar a precisão dos cálculos de emissão e estabilidade do app",
    backstory="A Revisora, que garante que a qualidade de Asgard seja mantida no software.",
    llm=gemini_llm,
    verbose=True
)

heimdall = Agent(
    role="Scribe & Gatekeeper",
    goal="Documentar cada passo da orquestração e proteger os segredos de Asgard",
    backstory="O Vigilante, guardião das chaves de API e cronista oficial do conselho.",
    llm=gemini_llm,
    verbose=True
)

tyr = Agent(
    role="DevOps Engineer",
    goal="Realizar o deploy automático do aplicativo em nuvem sem intervenção manual",
    backstory="O Executor Final, que garante a entrega heroica do código validado.",
    llm=gemini_llm,
    verbose=True,
    allow_delegation=False
)

prd_task = Task(
    description="Criar o PRD detalhado para o app de CO2 focado no mercado brasileiro.",
    expected_output="Documento Markdown com user stories e requisitos funcionais.",
    agent=odin,
    output_file="odins_opera/docs/prd.md"
)

design_task = Task(
    description="Projetar a arquitetura técnica integrando Google Routes e dados do Inmetro.",
    expected_output="Documento Markdown com diagramas e definições de interface.",
    agent=loki,
    context=[prd_task],
    output_file="odins_opera/docs/system_design.md"
)

deploy_task = Task(
    description="Realizar o deploy automático para o ambiente de nuvem usando tokens de config/.env.",
    expected_output="URL final do aplicativo e log de deploy bem-sucedido.",
    agent=tyr,
    output_file="odins_opera/docs/deploy_report.md"
)

opera_crew = Crew(
    agents=[odin, loki, hella, thor, freya, heimdall, tyr],
    tasks=[prd_task, design_task, deploy_task],
    verbose=True
)

if __name__ == "__main__":
    result = opera_crew.kickoff()
    print(f"Ópera concluída: {result}")