from datetime import date
from google.adk.agents.llm_agent import Agent

def get_current_date() -> str:
    """Returns the current date as a string."""
    return str(date.today())

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[get_current_date]
)
