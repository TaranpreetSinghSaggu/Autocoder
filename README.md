# Autocoder

> *A lightning-fast local code generation assistant powered by Ollama. Works completely offline with zero-latency AI-assisted coding inside Jupyter Notebooks.*

Autocoder is a minimal, focused Python ecosystem that integrates a fine-tuned Ollama model with Jupyter Notebooks via a custom `%%prompt` magic command. Write natural language prompts and watch the AI stream Python code directly into executable cells.

---

## Prerequisites

Before you start, ensure you have the following installed:

1. **[Ollama](https://ollama.com/):** For running the model engine locally.
2. **[uv](https://docs.astral.sh/uv/):** Python package and project manager (fast alternative to pip/venv).
3. **Python 3.13+** (bundled by uv)

---

## Quick Start

### Step 1: Pull the Model

Open your terminal and run:

```bash
ollama run saggutaranpreetsingh/autocoder
```

*(Type `/bye` to exit the chat once it downloads. The model is now cached on your machine.)*

### Step 2: Set Up the Environment

Clone/enter the repository and sync dependencies using `uv`:

```bash
# Clone the repository (if needed)
git clone https://github.com/TaranpreetSinghSaggu
cd Autocoder

# Sync dependencies and activate environment
uv sync
source .venv/bin/activate  # On Windows: .\.venv\Scripts\Activate.ps1
```

### Step 3: Launch Jupyter & Load the Extension

Start Jupyter from the project directory:

```bash
jupyter notebook
```

1. Open `magic.ipynb` or create a new notebook.
2. In the **first cell**, load the extension:
   ```python
   %load_ext ollama_connection
   ```

### Step 4: Use the `%%prompt` Magic

In any cell, use the `%%prompt` magic followed by your instruction:

```text
%%prompt
Solve the python problem regarding topological sort 
```

Hit `Shift + Enter`. The AI will:
- Stream the response live in the output area
- Automatically inject the generated Python code into the next input cell below

---

## What's Implemented

| File | Purpose |
|------|---------|
| `ollama_connection.py` | IPython magic (`%%prompt`) that streams Ollama responses and injects code into Jupyter cells |
| `main.py` | CLI demo: sends a prompt to Ollama and prints the response (optional) |
| `magic.ipynb` | Pre-configured notebook scaffold for using the `%%prompt` magic |
| `ModelFile` | (Optional) Defines how to build a custom Ollama model from a local `.gguf` file |
| `pyproject.toml` | Python dependencies and project metadata |
| `mcp/` | (Learning purposes only — not part of active workflow) |

---

## Usage Examples

### Generate Code in Jupyter

```python
%%prompt
Solve the python problem regarding topological sort and tell the possible question linked with topic
```

The magic command will:
1. Send your prompt to the `saggutaranpreetsingh/autocoder` model running locally
2. Stream the generated code in real-time below the cell
3. Auto-inject the final Python code into a new cell for execution

### Quick Terminal Test (Optional)

To verify your Ollama setup without Jupyter:

```bash
python main.py
```

This runs a synchronous chat request to the model and prints the response.

---

## Troubleshooting

**Ollama not connecting?**
- Ensure Ollama is running: `ollama serve` (or check your system tray)
- Verify the model exists: `ollama list`
- Re-pull if needed: `ollama run saggutaranpreetsingh/autocoder`

**Magic command not loading?**
- Make sure you're using the correct `uv`-managed kernel in Jupyter
- Check that `ollama_connection.py` is in the project root
- Reload Jupyter or restart the kernel

**PowerShell activation issues (Windows)?**
- Run as Administrator and execute:
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```
- Then retry: `.\.venv\Scripts\Activate.ps1`

---

## Project Structure

```
Autocoder/
├── ollama_connection.py    # IPython magic registration
├── main.py                 # CLI test script
├── magic.ipynb             # Jupyter notebook scaffold
├── ModelFile               # (Optional) Ollama model builder config
├── pyproject.toml          # Project dependencies
└── mcp/                    # (Learning purposes only)
```

---

## Notes

- Keep Ollama running before executing notebooks or CLI commands.
- The `%%prompt` magic automatically cleans markdown formatting from code output.
- `ModelFile` is optional—by default, the setup uses `saggutaranpreetsingh/autocoder` from Ollama.
