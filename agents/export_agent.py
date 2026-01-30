from adk import Agent, tool
from tools.exporter import export_csv

@tool
async def export(data: list, path: str):
    """Export data

    Args:
        data (list): data list
        path (str): the path where the file should be exported.

    Returns:
        _type_: _description_
    """
    export_csv(data, path)
    return path

export_agent = Agent(
    name="export-agent",
    instructions="Export CSV",
    tools=[export]
)
