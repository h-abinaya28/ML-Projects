from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get the weather for a specific location.
    :param location: The location to get the weather for
    :return: The weather information for the location
    """
    return f"The weather in {location} is sunny."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
