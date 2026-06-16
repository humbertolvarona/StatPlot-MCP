# Usage guide

## Basic workflow

1. Prepare a CSV file with tabular data.
2. Use `get_columns_info` to inspect column names and data types.
3. Select a supported plot type.
4. Call `statplot` with the corresponding x, y and grouping variables.
5. Open the generated image from the output path.

## Example dataset

The repository includes `data/sample.csv`.

```csv
time,temperature,salinity,depth,station,region
1,26.4,35.1,5,A,north
2,26.7,35.0,5,A,north
3,27.1,35.2,5,A,north
4,27.4,35.4,5,A,north
```

## Create a line plot

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

## Create a scatter plot

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

## Create a correlation heatmap

```json
{
  "file_path": "data/sample.csv",
  "plot_type": "heatmap",
  "output_path": "outputs/correlation_heatmap.jpg"
}
```

For `heatmap`, StatPlot selects numeric columns and computes the Pearson correlation matrix with pandas before plotting.

## Create a multi-series line plot

```json
{
  "file_path": "data/sample.csv",
  "plot_type": "lineplot",
  "x": "time",
  "y_multiple": ["temperature", "salinity"],
  "output_path": "outputs/multiple_series.jpg"
}
```

When `y_multiple` is used with `lineplot`, the CSV table is internally converted from wide format to long format using `pandas.melt`. Each selected variable becomes an independent series.
