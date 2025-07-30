from mcp.server.fastmcp import FastMCP

# Math is a server name
mcp = FastMCP("Math")


@mcp.tool()
def add(x: int, y: int) -> int:
    """
    Adds two integers together.
    :param x: First integer
    :param y: Second integer
    :return: Sum of x and y
    """
    return x + y


@mcp.tool()
def multiply(x: int, y: int) -> int:
    """
    Multiplies two integers together.
    :param x: First integer
    :param y: Second integer
    :return: Product of x and y
    """
    return x * y


if __name__ == "__main__":
    # transport stdio returns the result to the standard output to tool calls
    # and reads the input from the standard input.
    mcp.run(transport="stdio")
