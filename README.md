# MCP-AI2SQL

A Python project that provides tools for generating SQL queries through a FastMCP server interface in Cursor IDE.

## Features

- **SQL Query Generation**: Generate SQL queries based on natural language requests
- **FastMCP Server**: Runs as a server that can be queried for these tools
- **Cursor Integration**: Works seamlessly with Cursor IDE through MCP configuration
- **Claude Integration**: Compatible with Claude AI assistant for natural language SQL query generation

## Prerequisites

- Python 3.10 or higher
- UV package manager 
- Dependencies listed in `pyproject.toml`
- Cursor IDE

## Installation

### Using UV Package Manager (Recommended)

1. Create a new project
```bash
uv init mcp-ai2sql
cd mcp-ai2sql
```

2. Create and activate virtual environment
```bash
# Create virtual env
uv venv

# Activate for macOS/Linux
source .venv/bin/activate

# Activate for Windows
.venv\Scripts\activate
```

3. Install dependencies
```bash
uv add "mcp[cli]" dotenv
```

### Alternative Installation Method

1. Clone this repository
```bash
git clone https://github.com/yourusername/mcp-ai2sql.git
cd mcp-ai2sql
```

2. Set up a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -e .
```

## Usage

Run the MCP server:

```bash
python main.py
```

### Cursor IDE Integration

To use MCP-AI2SQL with Cursor IDE, configure the MCP server in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "mcp-ai2sql": {
      "command": "/path/to/your/python/uv",
      "args": [
        "--directory",
        "/path/to/mcp-ai2sql",
        "run",
        "main.py"
      ]
    }
  }
}
```

Replace the paths with your actual Python/UV path and project directory.

### Claude App Integration

MCP-AI2SQL can be used with Claude AI assistant for more intuitive SQL query generation:

1. Make sure your MCP server is running
2. In Claude's interface, you can request SQL queries in natural language
3. Claude will utilize the MCP-AI2SQL tool to generate accurate SQL based on your descriptions

Example prompt for Claude:
```
Use the AI2SQL tool to create a query that finds all customers who placed orders in the last month.
```

Claude will process this request and generate the appropriate SQL using the MCP-AI2SQL backend.

### Available Tools

#### SQL Generator Tool

Generate SQL queries from natural language:

```python
generate_sql(
    request="find all users", 
    table_name="users", 
    columns="id, name, email"
)
```

Supports various SQL operations:
- SELECT queries
- CREATE TABLE statements
- INSERT statements
- UPDATE statements
- DELETE statements
- DROP TABLE statements

## Environment Variables

Create a `.env` file in the root directory with the following variables:
```
# Add any environment variables needed here
```

## Project Structure

- `main.py` - Main server implementation with tool definitions
- `pyproject.toml` - Project configuration and dependencies

## License

MIT License

Copyright (c) 2023 Mustafa Ergisi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

[Add contribution guidelines here]
