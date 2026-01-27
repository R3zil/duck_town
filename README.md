# Duck Town

A multi-agent workspace manager powered by Gas Town, featuring an MCP server for Claude Desktop integration.

## Overview

Duck Town is a comprehensive agent coordination system that provides:

- **Multi-agent workflow management** - Coordinate work across agents using beads (issue tracking)
- **MCP Server** - Model Context Protocol server for Claude Desktop integration
- **Gas Town Infrastructure** - Agent coordination, lifecycle management, and task dispatch

## Features

### MCP Server

Duck Town includes a simple MCP (Model Context Protocol) server that provides basic tools for Claude Desktop:

**Available Tools:**
- `echo` - Returns the input message back
- `add` - Adds two numbers together
- `get_time` - Returns the current timestamp in ISO format

See [mcp_server/README.md](mcp_server/README.md) for detailed installation and usage instructions.

### Agent Infrastructure

- **Mayor** - Global coordinator handling cross-rig communication and escalations
- **Deacon** - Daemon beacon receiving mechanical heartbeats and running monitoring
- **Witness** - Per-rig worker monitor managing polecat lifecycles
- **Refinery** - Merge queue processor handling code integration

### Beads Issue Tracking

Built-in issue tracking system that supports:
- Hierarchical task organization (epics, tasks, bugs)
- Dependency management
- Molecule-based workflows (reusable work patterns)
- Git-based persistence with JSONL and SQLite backends

## Quick Start

### Setting up the MCP Server

1. Navigate to the MCP server directory:
```bash
cd mcp_server
```

2. Install dependencies:
```bash
pip install -e .
```

3. Configure Claude Desktop by adding to your config file:

**MacOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "duck-town-tools": {
      "command": "python",
      "args": ["/absolute/path/to/duck_town/mcp_server/server.py"]
    }
  }
}
```

4. Restart Claude Desktop and the tools will be available.

### Working with Beads

```bash
# List all open issues
bd list --status=open

# Create a new task
bd create -t task "Task description"

# Show issue details
bd show <issue-id>

# Update issue status
bd update <issue-id> -s in_progress

# Sync changes to git
bd sync
```

## Project Structure

```
duck_town/
├── .beads/              # Issue tracking database
├── mcp_server/          # MCP server for Claude Desktop
├── daemon/              # Daemon management
├── deacon/              # Deacon agent
├── mayor/               # Mayor coordinator
├── Conducktor_rig/      # Example rig configuration
├── logs/                # System logs
├── plugins/             # Plugin system
└── settings/            # Configuration files
```

## Requirements

- Python 3.10 or higher
- Git
- MCP Python SDK (`pip install mcp`)

## Development

### Running Tests

```bash
# Run MCP server tests
cd mcp_server
python -m pytest
```

### Issue Tracking

All development tasks are tracked using the beads system:

```bash
# See what's ready to work on
bd ready

# Check for bugs
bd list --type=bug --status=open
```

## Repository

**URL:** https://github.com/R3zil/duck_town.git
**Branch:** master

## License

Copyright 2026 - Gas Town Project

## Contributing

This project uses the beads issue tracking system. To contribute:

1. Check available work: `bd ready`
2. Claim an issue: `bd update <id> --claim`
3. Make your changes
4. Sync beads: `bd sync`
5. Commit and push changes

## Documentation

- [MCP Server Documentation](mcp_server/README.md)
- [Agent Roles](AGENTS.md)
- [Claude Integration](CLAUDE.md)

## Support

For issues or questions, file a bead:
```bash
bd create -t bug "Issue description"
```
