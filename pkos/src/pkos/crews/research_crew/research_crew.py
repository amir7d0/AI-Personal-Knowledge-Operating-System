# src/latest_ai_flow/crews/content_crew/content_crew.py
import os
from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

from crewai import LLM

llm = LLM(
    provider="openai",
    model="meta/llama-3.2-3b-instruct",
    api_key=os.environ.get("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
)


@CrewBase
class ResearchCrew:
  """Single-agent research crew used inside the Flow."""

  agents: List[BaseAgent]
  tasks: List[Task]

  agents_config = "config/agents.yaml"
  tasks_config = "config/tasks.yaml"

  @agent
  def researcher(self) -> Agent:
    return Agent(
      llm=llm,
      config=self.agents_config["researcher"],  # type: ignore[index]
      verbose=True,
      # tools=[SerperDevTool()],
    )

  @task
  def research_task(self) -> Task:
    return Task(
      config=self.tasks_config["research_task"],  # type: ignore[index]
    )

  @crew
  def crew(self) -> Crew:
    return Crew(
      agents=self.agents,
      tasks=self.tasks,
      process=Process.sequential,
      verbose=True,
    )