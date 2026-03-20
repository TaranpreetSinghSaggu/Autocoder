# Autocoder (Ollama + Jupyter)

This project is a local code-generation workflow built around:
- a custom Ollama model named `autocoder`
- Jupyter Notebook usage with a `%%prompt` cell magic
- optional terminal testing through `main.py`

`mcp/` is present in the repository but **not part of this workflow**.

## What has been implemented

- `ModelFile` defines how to build the Ollama model (`FROM` local `.gguf`, template, and parameters).
- `ollama_connection.py` registers `%%prompt` (IPython cell magic) that:
	- sends notebook prompts to Ollama (`autocoder` model),
	- streams response live in notebook output,
	- injects generated Python code into the next input cell.
- `main.py` sends a direct chat prompt to the same model as a quick CLI verification.
- `magic.ipynb` exists as the working notebook scaffold for this flow.

## Prerequisites

- Windows with Python 3.13+
- [Ollama](https://ollama.com/) installed and running
- A local `.gguf` model file path you can reference in `ModelFile`

## Initialization (from scratch)

### 1) Prepare Python environment

From project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .
```

### 2) Build the Ollama model

Edit `ModelFile` first:
- Update the `FROM "...gguf"` path to your machine’s actual `.gguf` location.

Then run:

```powershell
ollama create autocoder -f ModelFile
```

Verify model is available:

```powershell
ollama list
```

### 3) Register Jupyter kernel

```powershell
python -m ipykernel install --user --name=autocoder-env --display-name "Python (Autocoder)"
```

### 4) Start Jupyter

```powershell
jupyter notebook
```

Open `magic.ipynb` and select kernel **Python (Autocoder)**.

### 5) Load notebook magic

In the first notebook cell:

```python
%run ollama_connection.py
```

Then use:

```python
%%prompt
Write a Python function that solves shortest path using Dijkstra and A* with an example.
```

## Quick terminal test (optional)

Run:

```powershell
python main.py
```

If Ollama and model setup are correct, you should get a generated response from `autocoder`.

## Notes

- If PowerShell blocks activation scripts, run PowerShell as current user and execute:
	```powershell
	Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
	```
- Keep Ollama running before notebook/CLI prompts.
- Ensure `ModelFile` points to a valid local `.gguf`; model creation fails otherwise.
