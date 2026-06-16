# MCP client configuration

StatPlot is an MCP server. It must be launched by an MCP-compatible client through a local command.

## Generic MCP configuration

Use the following pattern and adjust the absolute path to the repository.

```json
{
  "mcpServers": {
    "statplot": {
      "command": "python",
      "args": ["-m", "statplot.server"],
      "cwd": "/absolute/path/to/statplot-mcp"
    }
  }
}
```

## Configuration using an explicit virtual environment

```json
{
  "mcpServers": {
    "statplot": {
      "command": "/absolute/path/to/statplot-mcp/.venv/bin/python",
      "args": ["-m", "statplot.server"],
      "cwd": "/absolute/path/to/statplot-mcp"
    }
  }
}
```

On Windows, the Python executable is usually located at:

```text
C:\absolute\path\to\statplot-mcp\.venv\Scripts\python.exe
```

## Recommended working directory

The working directory should be the root of the repository. This makes relative paths such as `data/sample.csv` and `outputs/plot.jpg` easier to use.
