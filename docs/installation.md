# Installation

## Requirements

StatPlot requires Python 3.10 or later. The server depends on the MCP Python SDK, pandas, seaborn and matplotlib.

## Local installation

Clone the repository and create a virtual environment.

```bash
git clone https://github.com/<user>/statplot-mcp.git
cd statplot-mcp
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Dependency-only installation

```bash
pip install -r requirements.txt
```

## Run the server

```bash
python -m statplot.server
```

If the package was installed with `pip install -e .`, the console command can also be used:

```bash
statplot-mcp
```
