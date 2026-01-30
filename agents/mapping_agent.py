from adk import Agent, tool
from tools.csv_loader import load_mapping

@tool
async def load(csv_path: str):
    """_summary_

    Args:
        csv_path (str): _description_

    Returns:
        _type_: _description_
    """
    return load_mapping(csv_path)

mapping_agent = Agent(
    name="mapping-agent",
    instructions="Load CSV mapping",
    tools=[load]
)
