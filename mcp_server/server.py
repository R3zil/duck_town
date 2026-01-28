#!/usr/bin/env python3
"""Simple MCP server with echo, add, get_time, and file system tools."""

import asyncio
import os
from datetime import datetime
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent


# Create server instance
app = Server("simple-tools-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="echo",
            description="Returns the input message back",
            inputSchema={
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message to echo back"
                    }
                },
                "required": ["message"]
            }
        ),
        Tool(
            name="add",
            description="Adds two numbers together",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="get_time",
            description="Returns the current timestamp",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="read_file",
            description="Reads the contents of a file",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file to read"
                    }
                },
                "required": ["path"]
            }
        ),
        Tool(
            name="write_file",
            description="Writes content to a file",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file to write"
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to write to the file"
                    }
                },
                "required": ["path", "content"]
            }
        ),
        Tool(
            name="list_directory",
            description="Lists files and directories in a given path",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the directory to list (defaults to current directory)"
                    }
                }
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls."""
    if name == "echo":
        message = arguments.get("message", "")
        return [TextContent(type="text", text=message)]

    elif name == "add":
        a = arguments.get("a", 0)
        b = arguments.get("b", 0)
        result = a + b
        return [TextContent(type="text", text=str(result))]

    elif name == "get_time":
        current_time = datetime.now().isoformat()
        return [TextContent(type="text", text=current_time)]

    elif name == "read_file":
        path = arguments.get("path")
        if not path:
            return [TextContent(type="text", text="Error: path is required")]

        try:
            file_path = Path(path).expanduser().resolve()
            if not file_path.exists():
                return [TextContent(type="text", text=f"Error: File not found: {path}")]
            if not file_path.is_file():
                return [TextContent(type="text", text=f"Error: Path is not a file: {path}")]

            content = file_path.read_text()
            return [TextContent(type="text", text=content)]
        except PermissionError:
            return [TextContent(type="text", text=f"Error: Permission denied: {path}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error reading file: {str(e)}")]

    elif name == "write_file":
        path = arguments.get("path")
        content = arguments.get("content", "")

        if not path:
            return [TextContent(type="text", text="Error: path is required")]

        try:
            file_path = Path(path).expanduser().resolve()
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)
            return [TextContent(type="text", text=f"Successfully wrote to {path}")]
        except PermissionError:
            return [TextContent(type="text", text=f"Error: Permission denied: {path}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error writing file: {str(e)}")]

    elif name == "list_directory":
        path = arguments.get("path", ".")

        try:
            dir_path = Path(path).expanduser().resolve()
            if not dir_path.exists():
                return [TextContent(type="text", text=f"Error: Directory not found: {path}")]
            if not dir_path.is_dir():
                return [TextContent(type="text", text=f"Error: Path is not a directory: {path}")]

            entries = []
            for entry in sorted(dir_path.iterdir()):
                entry_type = "DIR" if entry.is_dir() else "FILE"
                entries.append(f"{entry_type}: {entry.name}")

            if not entries:
                return [TextContent(type="text", text="Directory is empty")]

            return [TextContent(type="text", text="\n".join(entries))]
        except PermissionError:
            return [TextContent(type="text", text=f"Error: Permission denied: {path}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error listing directory: {str(e)}")]

    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    """Run the server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
