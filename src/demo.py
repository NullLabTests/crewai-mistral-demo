import os
from crewai import Agent, Task, Crew, LLM

# Configure Mistral LLM
mistral_llm = LLM(
    model="mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY"),
    base_url="https://api.mistral.ai/v1"
)

# Create agents
researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover groundbreaking AI trends for 2026",
    backstory="An expert in emerging AI technologies with a knack for spotting trends before they go mainstream.",
    llm=mistral_llm,
    verbose=True
)

writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling content about AI trends",
    backstory="A professional writer who simplifies complex AI concepts into engaging narratives.",
    llm=mistral_llm,
    verbose=True
)

# Create tasks
research_task = Task(
    description="Research and identify the top 5 AI trends that will dominate in 2026. Focus on practical applications and real-world impact.",
    expected_output="A list of 5 AI trends with brief descriptions and examples of companies or projects leading the charge.",
    agent=researcher
)

write_task = Task(
    description="Write a detailed blog post about the top 5 AI trends for 2026. Include real-world examples and potential challenges for each trend.",
    expected_output="A 1500-2000 word blog post in markdown format, with clear sections for each trend, examples, and a conclusion summarizing the impact.",
    agent=writer,
    context=[research_task]
)

# Create and run crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Starting CrewAI + Mistral Demo...")
    result = crew.kickoff()
    print(f"\\n📄 Generated Content:\\n{result}")
