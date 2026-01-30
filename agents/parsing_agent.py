from adk import Agent, tool
from tools.pdf_parser import extract_vulns

@tool
async def parse_pdf(pdf_path: str):
    return extract_vulns(pdf_path)

parsing_agent = Agent(
    name="parsing-agent",
    instructions="Extract vulnerabilities",
    tools=[parse_pdf]
)
