from mcp.server.fastmcp import FastMCP
import ollama

# Initialize FastMCP server
mcp = FastMCP("AutoCoder")

@mcp.tool()
async def generate_code(prompt: str) -> str:
    """
    Generates expert Python code using the fine-tuned LFM2.5 model.
    Use this for complex algorithms like Dijkstra, A*, or Flask models.
    """
    response = ollama.chat(
        model='autocoder',
        messages=[
            {"role": "system", "content": "You are an expert Python engineer. Output only working code."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.message.content

if __name__ == "__main__":
    mcp.run(transport="stdio")