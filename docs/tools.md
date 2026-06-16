# Tool reference

StatPlot exposes two MCP tools: `statplot` and `get_columns_info`.

## `get_columns_info`

Returns the column names and inferred pandas data types for a CSV file.

### Parameters

| Parameter | Type | Required | Description |
|---|---:|---:|---|
| `file_path` | string | yes | Path to the CSV file. |

### Example

```json
{
  "file_path": "data/sample.csv"
}
```

### Response

```text
Columns: ['time', 'temperature', 'salinity', 'depth', 'station', 'region'], Dtypes: {'time': 'int64', 'temperature': 'float64', ...}
```

## `statplot`

Creates a statistical plot from a CSV file and saves it to disk.

### Parameters

| Parameter | Type | Required | Description |
|---|---:|---:|---|
| `file_path` | string | yes | Path to the CSV file. |
| `plot_type` | string | yes | Seaborn plot function to use. |
| `x` | string or null | no | Column used on the x-axis. |
| `y` | string or null | no | Column used on the y-axis. |
| `hue` | string or null | no | Column used for grouping by color. |
| `row` | string or null | no | Row faceting variable for figure-level plots. |
| `col` | string or null | no | Column faceting variable for figure-level plots. |
| `output_path` | string or null | no | Output image path. A random JPG filename is generated when omitted. |
| `y_multiple` | list of strings or null | no | Multiple numeric columns to plot as separate line series. Only applies to `lineplot`. |

### Supported plot types

Axis-level plots:

```text
scatterplot, lineplot, histplot, kdeplot, ecdfplot, rugplot, stripplot,
swarmplot, boxplot, violinplot, boxenplot, pointplot, barplot, countplot,
regplot, residplot
```

Figure-level plots:

```text
relplot, displot, catplot, lmplot
```

Matrix plots:

```text
heatmap, clustermap
```

### Example

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

### Response

```text
Plot saved successfully to /absolute/path/to/outputs/temperature_lineplot.jpg
```
