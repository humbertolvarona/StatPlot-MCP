# StatPlot MCP

StatPlot is a Model Context Protocol server for creating statistical graphics from CSV files. It uses pandas for tabular data handling, seaborn for statistical visualization and matplotlib for figure rendering. The server exposes MCP tools that allow a compatible client to inspect CSV columns and generate publication-oriented plots as image files.

## Main features

- Reads local CSV files with pandas.
- Generates seaborn statistical plots through MCP tool calls.
- Supports scatter, line, histogram, KDE, ECDF, box, violin, bar, regression, residual, categorical, relational and matrix plots.
- Supports multi-series line plots through a wide-to-long transformation using `pandas.melt`.
- Saves figures as high-resolution image files with 500 DPI.
- Applies a consistent visual style with bold axis labels, bold tick labels and a refined grid.
- Provides a helper tool to inspect CSV columns and inferred data types before plotting.

## Repository contents

```text
statplot-mcp/
├── src/statplot/server.py       # MCP server implementation
├── data/sample.csv              # Minimal example dataset
├── docs/                        # Full documentation
├── examples/client_examples.md  # Example MCP payloads
├── pyproject.toml               # Python package metadata
├── requirements.txt             # Runtime dependencies
├── LICENSE                      # MIT license
└── README.md                    # Main project documentation
```

## Requirements

- Python 3.10 or later
- MCP Python SDK
- pandas
- seaborn
- matplotlib

## Installation

```bash
git clone https://github.com/<user>/statplot-mcp.git
cd statplot-mcp
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -e .
```

## Run the MCP server

```bash
python -m statplot.server
```

After editable installation, it can also be launched with:

```bash
statplot-mcp
```

## MCP client configuration

Use this pattern in an MCP-compatible client. Replace the repository path with the real absolute path on your system.

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

If a virtual environment is used, point the command to the environment-specific Python executable:

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

## Available tools

### `get_columns_info`

Inspects a CSV file and returns column names and inferred data types.

Example payload:

```json
{
  "file_path": "data/sample.csv"
}
```

Example response:

```text
Columns: ['time', 'temperature', 'salinity', 'depth', 'station', 'region'], Dtypes: {'time': 'int64', 'temperature': 'float64', 'salinity': 'float64', 'depth': 'int64', 'station': 'object', 'region': 'object'}
```

### `statplot`

Creates a statistical plot and saves the output image to disk.

Parameters:

| Parameter | Type | Required | Description |
|---|---:|---:|---|
| `file_path` | string | yes | Path to the input CSV file. |
| `plot_type` | string | yes | Plot type to generate. |
| `x` | string or null | no | Column used on the x-axis. |
| `y` | string or null | no | Column used on the y-axis. |
| `hue` | string or null | no | Column used for color grouping. |
| `row` | string or null | no | Row faceting variable for figure-level plots. |
| `col` | string or null | no | Column faceting variable for figure-level plots. |
| `output_path` | string or null | no | Output image path. If omitted, a random JPG name is generated. |
| `y_multiple` | list of strings or null | no | Multiple columns to plot as independent line series. Only valid with `lineplot`. |

## Supported plot types

Axis-level seaborn plots:

```text
scatterplot, lineplot, histplot, kdeplot, ecdfplot, rugplot, stripplot,
swarmplot, boxplot, violinplot, boxenplot, pointplot, barplot, countplot,
regplot, residplot
```

Figure-level seaborn plots:

```text
relplot, displot, catplot, lmplot
```

Matrix plots:

```text
heatmap, clustermap
```

## Usage examples

### Line plot

```json
{
  "file_path": "data/sample.csv",
  "plot_type": "lineplot",
  "x": "time",
  "y": "temperature",
  "hue": "station",
  "output_path": "outputs/temperature_lineplot.jpg"
}
```

### Scatter plot

```json
{
  "file_path": "data/sample.csv",
  "plot_type": "scatterplot",
  "x": "salinity",
  "y": "temperature",
  "hue": "station",
  "output_path": "outputs/temperature_salinity_scatter.jpg"
}
```

### Multiple line series

```json
{
  "file_path": "data/sample.csv",
  "plot_type": "lineplot",
  "x": "time",
  "y_multiple": ["temperature", "salinity"],
  "output_path": "outputs/multiple_series.jpg"
}
```

### Correlation heatmap

```json
{
  "file_path": "data/sample.csv",
  "plot_type": "heatmap",
  "output_path": "outputs/correlation_heatmap.jpg"
}
```

## Notes on heatmaps and clustermaps

For `heatmap`, StatPlot selects numeric columns and plots their Pearson correlation matrix. For `clustermap`, StatPlot selects numeric columns and passes the numeric table directly to seaborn. Non-numeric columns are ignored in matrix plots.

## Documentation

Additional documentation is available in the `docs` directory:

- `docs/installation.md`
- `docs/configuration.md`
- `docs/tools.md`
- `docs/usage.md`
- `docs/development.md`

## License

This project is distributed under the MIT License.
