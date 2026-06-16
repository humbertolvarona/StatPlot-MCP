# Development notes

## Repository layout

```text
statplot-mcp/
├── src/statplot/
│   ├── __init__.py
│   └── server.py
├── data/
│   └── sample.csv
├── docs/
│   ├── configuration.md
│   ├── development.md
│   ├── installation.md
│   ├── tools.md
│   └── usage.md
├── examples/
│   └── client_examples.md
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
└── requirements.txt
```

## Code structure

The server is implemented in `src/statplot/server.py`. The MCP instance is created with:

```python
server = FastMCP("statplot")
```

The tool functions are registered with the `@server.tool()` decorator. The module can be launched directly with:

```bash
python -m statplot.server
```

## Adding new plot types

To add a new seaborn axis-level function, add its name to `SUPPORTED_AXES_PLOTS`. To add a figure-level function, add its name to `SUPPORTED_FIGURE_PLOTS`. Matrix-like plots that require custom preprocessing should be handled separately in the `SUPPORTED_MATRIX_PLOTS` branch.

## Error handling

The implementation validates that the CSV file exists, that the input has a `.csv` extension, that the plot type is supported and that referenced columns are present in the input table. Matrix plots require numeric columns.

## Output policy

Generated figures are written to disk. If `output_path` is omitted, a unique JPG file name is created with `uuid.uuid4`. Parent output directories are created automatically.
