from datetime import date
from google.adk.agents.llm_agent import Agent
from agents.parsing_agent import parsing_agent
from agents.mapping_agent import mapping_agent
from agents.matching_agent import matching_agent
from agents.export_agent import export_agent

def get_current_date() -> str:
    """Returns the current date as a string."""
    return str(date.today())

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Combine data from csv files to produce output csv file',
    instruction='Full orchestration pipeline',
    tools=[get_current_date],
    sub_agents=[parsing_agent, mapping_agent, matching_agent, export_agent]
)
