# MCP Servers Learning Project

This repository contains examples and implementations of Model Context Protocol (MCP) servers and clients. MCP is a protocol that allows LLMs like Claude to interact with external tools and data sources in a standardized way.

## Project Structure

The repository is organized into several modules, each focusing on different aspects of MCP:

### 1. Quickstart Resources

The `1_quickstart-resources` directory contains sample implementations of MCP clients and servers to help you get started:

- **mcp-client-python**: A Python client implementation for connecting to MCP servers
- **mcp-client-typescript**: A TypeScript client implementation for connecting to MCP servers
- **weather-server-python**: A sample Python MCP server that provides weather information
- **weather-server-typescript**: A sample TypeScript MCP server that provides weather information

These examples demonstrate basic MCP concepts and provide starting points for your own implementations.

### 2. MCP Documentation Server

The `2_mcpdoc` directory contains a specialized MCP server for serving documentation:

- Implements an MCP server that can retrieve and serve documentation from various sources
- Includes configuration examples and a robust project structure
- Demonstrates advanced MCP concepts like error handling and resource management

### 3. Terminal Server

The `3_building_securing_and_containerizing_mcp_server` directory contains a custom MCP server implementation that:

- Exposes a terminal command execution tool allowing access to system commands
- Provides a resource for accessing MCP documentation
- Demonstrates proper error handling and input validation
- Shows how to implement both tools and resources in a single server

## Getting Started

### Prerequisites

- Python 3.10 or higher
- MCP SDK 1.2.0 or higher
- For TypeScript examples: Node.js and npm

### Installation

```bash
# For Python dependencies
uv add "mcp[cli]" httpx

# Or with pip
pip install "mcp[cli]" httpx
```

### Running MCP Servers

You can run any of the MCP servers using:

```bash
# With Python directly
python <path_to_server.py>

# Or with the MCP CLI
mcp dev <path_to_server.py>
```

For example, to run the terminal server:

```bash
python 3_building_securing_and_containerizing_mcp_server/server.py

# Or
mcp dev 3_building_securing_and_containerizing_mcp_server/server.py
```

### Connecting to Claude Desktop

To connect an MCP server to Claude Desktop:

```bash
mcp install <path_to_server.py>
```

## Key Concepts

- **Tools**: Functions that can be called by Claude to execute code or produce side effects
- **Resources**: Data exposed to Claude that can be read and referenced
- **Prompts**: Templates for structuring interactions with Claude

## Contributing

Feel free to extend and modify these examples for your own use cases. If you develop a useful MCP server, consider sharing it with the community!

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Claude Desktop](https://claude.ai/download) 