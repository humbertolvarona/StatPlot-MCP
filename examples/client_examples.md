# Client examples

## Inspect CSV columns

```json
{
  "file_path": "data/sample.csv"
}
```

## Line plot

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

## Scatter plot

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

## Multiple line series

```json
{
  "file_path": "data/sample.csv",
  "plot_type": "lineplot",
  "x": "time",
  "y_multiple": ["temperature", "salinity"],
  "output_path": "outputs/multiple_series.jpg"
}
```

## Heatmap

```json
{
  "file_path": "data/sample.csv",
  "plot_type": "heatmap",
  "output_path": "outputs/correlation_heatmap.jpg"
}
```
