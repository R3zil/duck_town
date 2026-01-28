# Simple MCP Server

A simple Model Context Protocol (MCP) server that provides basic tools including echo, add, get_time, and file system operations.

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

### 4. read_file
Reads the contents of a file.

**Parameters:**
- `path` (string, required): Path to the file to read

**Returns:** File contents as text

**Error Handling:**
- Returns error message if file not found
- Returns error message if path is not a file
- Returns error message if permission denied

### 5. write_file
Writes content to a file. Creates parent directories if they don't exist.

**Parameters:**
- `path` (string, required): Path to the file to write
- `content` (string, required): Content to write to the file

**Returns:** Success message with file path

**Error Handling:**
- Returns error message if permission denied
- Automatically creates parent directories

### 6. list_directory
Lists files and directories in a given path.

**Parameters:**
- `path` (string, optional): Path to the directory to list (defaults to current directory)

**Returns:** List of entries with type (FILE or DIR) and name

**Error Handling:**
- Returns error message if directory not found
- Returns error message if path is not a directory
- Returns error message if permission denied

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
- **read_file:** `{"path": "/path/to/file.txt"}` → Returns file contents
- **write_file:** `{"path": "/path/to/file.txt", "content": "Hello, World!"}` → Writes content to file
- **list_directory:** `{"path": "/path/to/directory"}` → Lists files and directories

## Requirements

- Python 3.10 or higher
- mcp package (official MCP Python SDK)

## Development

The server is implemented using the official MCP Python SDK and follows the MCP protocol specification for tool calling.
