from mcp.server.fastmcp import FastMCP
import subprocess
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create an MCP server
mcp = FastMCP("Terminal Server")

@mcp.tool()
def run_command(command: str) -> str:
    """Run a terminal command and return the output
    
    Args:
        command: The terminal command to execute
        
    Returns:
        The command output
    """
    logger.info(f"Running command: {command}")
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True,
            timeout=30  # Add timeout for safety
        )
        
        # Return stdout or stderr if there was an error
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 30 seconds"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.resource("readme://mcp")
def get_readme() -> str:
    """Get the MCP Python SDK README content
    
    Returns:
        The content of the mcpreadme.md file
    """
    logger.info("Getting MCP README content")
    
    # Get the current file's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(current_dir, "mcpreadme.md")
    
    try:
        with open(readme_path, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        logger.error(f"Error reading readme: {str(e)}")
        return f"Error: Could not read readme file: {str(e)}"

# If the file is run directly
if __name__ == "__main__":
    logger.info("Starting MCP Terminal Server...")
    # This will start the server and keep it running
    mcp.run()
