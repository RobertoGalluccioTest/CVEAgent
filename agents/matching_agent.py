from adk import Agent, tool
from tools.vertex_matcher import semantic_match

@tool
async def match(vulns: list):
    return semantic_match(vulns)

matching_agent = Agent(
    name="matching-agent",
    instructions="Semantic endpoint matching",
    tools=[match]
)
