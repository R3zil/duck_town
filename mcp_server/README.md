# Simple MCP Server

A simple Model Context Protocol (MCP) server that provides three basic tools: echo, add, and get_time.

## Tools

### 1. echo
Returns the input message back.

**Parameters:**
- `message` (string, required): The message to echo back

### 2. add
Adds two numbers together.

**Parameters:**
- `a` (number, required): First number
- `b` (number, required): Second number

### 3. get_time
Returns the current timestamp in ISO format.

**Parameters:** None

## Installation

1. Install dependencies:
```bash
pip install -e .
```

Or install the MCP SDK directly:
```bash
pip install mcp
```

## Usage

### Running the Server

The server uses stdio for communication:

```bash
python server.py
```

### Using with Claude Desktop

Add this configuration to your Claude Desktop config file:

**MacOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "simple-tools": {
      "command": "python",
      "args": ["/absolute/path/to/mcp_server/server.py"]
    }
  }
}
```

Replace `/absolute/path/to/mcp_server/` with the actual path to this directory.

### Testing the Tools

Once connected, you can use the tools through the MCP client:

- **echo:** `{"message": "Hello, World!"}`
- **add:** `{"a": 5, "b": 3}` → Returns: `8`
- **get_time:** `{}` → Returns current ISO timestamp

## Requirements

- Python 3.10 or higher
- mcp package (official MCP Python SDK)

## Development

The server is implemented using the official MCP Python SDK and follows the MCP protocol specification for tool calling.
