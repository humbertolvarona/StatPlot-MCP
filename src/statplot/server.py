import sys
import uuid
from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
from mcp.server.fastmcp import FastMCP

server = FastMCP("statplot")

SUPPORTED_AXES_PLOTS = {
    "scatterplot",
    "lineplot",
    "histplot",
    "kdeplot",
    "ecdfplot",
    "rugplot",
    "stripplot",
    "swarmplot",
    "boxplot",
    "violinplot",
    "boxenplot",
    "pointplot",
    "barplot",
    "countplot",
    "regplot",
    "residplot",
}

SUPPORTED_FIGURE_PLOTS = {
    "relplot",
    "displot",
    "catplot",
    "lmplot",
}

SUPPORTED_MATRIX_PLOTS = {
    "heatmap",
    "clustermap",
}

SUPPORTED_PLOTS = SUPPORTED_AXES_PLOTS | SUPPORTED_FIGURE_PLOTS | SUPPORTED_MATRIX_PLOTS


def apply_refined_style() -> None:
    sns.set_theme(
        style="whitegrid",
        rc={
            "axes.grid": True,
            "grid.color": "lightgray",
            "axes.labelweight": "bold",
            "axes.labelsize": 12,
            "axes.titlesize": 12,
            "axes.titleweight": "bold",
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "legend.fontsize": 12,
            "legend.title_fontsize": 12,
        },
    )


def adjust_ticks(ax) -> None:
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=8, prune="both"))
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=8, prune="both"))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontweight("bold")


def resolve_output_path(output_path: Optional[str]) -> str:
    if output_path is None:
        return f"plot_{uuid.uuid4().hex}.jpg"
    return output_path


def validate_file_path(file_path: str) -> Path:
    path = Path(file_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")
    if path.suffix.lower() != ".csv":
        raise ValueError(f"Input file must be a CSV file: {path}")
    return path


def validate_columns(df: pd.DataFrame, columns: list[str]) -> None:
    missing = [column for column in columns if column and column not in df.columns]
    if missing:
        raise ValueError(f"Columns not found in CSV file: {missing}")


@server.tool()
def statplot(
    file_path: str,
    plot_type: str,
    x: Optional[str] = None,
    y: Optional[str] = None,
    hue: Optional[str] = None,
    row: Optional[str] = None,
    col: Optional[str] = None,
    output_path: Optional[str] = None,
    y_multiple: Optional[list[str]] = None,
) -> str:
    output_path = resolve_output_path(output_path)
    input_path = validate_file_path(file_path)

    if plot_type not in SUPPORTED_PLOTS:
        return f"Invalid plot type. Supported values: {sorted(SUPPORTED_PLOTS)}"

    df = pd.read_csv(input_path)
    validate_columns(df, [x, y, hue, row, col])

    apply_refined_style()

    if y_multiple and plot_type == "lineplot":
        validate_columns(df, [x, *y_multiple])
        df = df.melt(id_vars=[x], value_vars=y_multiple, var_name="serie", value_name="valor")
        y = "valor"
        hue = "serie"

    output = Path(output_path).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    if plot_type in SUPPORTED_AXES_PLOTS:
        fig, ax = plt.subplots(figsize=(10, 6))
        getattr(sns, plot_type)(data=df, x=x, y=y, hue=hue, ax=ax)
        adjust_ticks(ax)
        if ax.get_legend():
            legend = ax.legend(title=hue, loc="best")
            for text in legend.get_texts():
                text.set_weight("bold")
            legend.get_title().set_fontweight("bold")
        plt.tight_layout()
        plt.savefig(output, dpi=500)

    elif plot_type in SUPPORTED_FIGURE_PLOTS:
        grid = getattr(sns, plot_type)(data=df, x=x, y=y, hue=hue, row=row, col=col)
        for ax in grid.axes.flat:
            adjust_ticks(ax)
        grid.add_legend(title=hue)
        if grid.legend:
            for text in grid.legend.texts:
                text.set_weight("bold")
            grid.legend.get_title().set_fontweight("bold")
        grid.savefig(output, dpi=500)

    elif plot_type in SUPPORTED_MATRIX_PLOTS:
        numeric_df = df.select_dtypes(include=["number"])
        if numeric_df.empty:
            raise ValueError("Matrix plots require at least one numeric column.")
        if plot_type == "heatmap":
            plt.figure(figsize=(10, 8))
            sns.heatmap(data=numeric_df.corr(), annot=True, cmap="coolwarm")
            plt.tight_layout()
            plt.savefig(output, dpi=500)
        else:
            grid = sns.clustermap(data=numeric_df, cmap="coolwarm")
            grid.savefig(output, dpi=500)

    plt.close("all")
    return f"Plot saved successfully to {output}"


@server.tool()
def get_columns_info(file_path: str) -> str:
    input_path = validate_file_path(file_path)
    df = pd.read_csv(input_path)
    return f"Columns: {list(df.columns)}, Dtypes: {df.dtypes.astype(str).to_dict()}"


if __name__ == "__main__":
    try:
        server.run()
    except Exception as error:
        sys.stderr.write(f"Critical MCP server error: {str(error)}\n")
        sys.exit(1)
