import ollama
import sys
from IPython.core.magic import register_cell_magic
from IPython import get_ipython
from IPython.display import display, HTML, clear_output

@register_cell_magic
def prompt(line, cell):
    """
    %%prompt - Streams Ollama output directly into the cell output area
    and then injects the final code into the same cell.
    """
    user_prompt = cell.strip()
    full_response = ""
    
    shell = get_ipython()
    if not shell:
        print("Error: This must be run inside a Jupyter environment.")
        return

    display_handle = display(HTML("<b> Autocoder is thinking...</b>"), display_id=True)
    
    try:
        stream = ollama.generate(
            model='autocoder',
            prompt=f"System: Return only raw python code. No markdown, no intro, no backticks.\nUser: {user_prompt}",
            stream=True
        )

        for chunk in stream:
            text = chunk['response']
            full_response += text
            
            html_content = f"""
            <div style="padding:15px; 
                        border-left: 5px solid #007acc; 
                        background-color: #f4f4f4; 
                        color: #333;
                        font-family: 'Cascadia Code', 'Consolas', monospace; 
                        font-size: 14px;
                        line-height: 1.5;
                        white-space: pre-wrap;
                        border-radius: 0 5px 5px 0;
                        margin-top: 10px;">
<span style="color: #007acc; font-weight: bold;"># Streaming Preview:</span>
{full_response}
            </div>
            """
            display_handle.update(HTML(html_content))
        
    except Exception as e:
        display_handle.update(HTML(f"<b style='color:red;'> Ollama Error: {e}</b>"))
        return

    cleaned_code = full_response.strip()
    if "```" in cleaned_code:
        parts = cleaned_code.split("```")
        if len(parts) >= 3:
            cleaned_code = parts[-2]
            if cleaned_code.lower().startswith("python"):
                cleaned_code = cleaned_code[6:].strip()
        else:
            cleaned_code = cleaned_code.replace("```python", "").replace("```", "").strip()

    payload = {
        "source": "set_next_input",
        "text": cleaned_code,
        "replace": False,
    }
    shell.payload_manager.write_payload(payload)
    
    display_handle.update(HTML("<b> Generation Complete! Code injected below.</b>"))

print("--- Autocoder Ecosystem Active ---")
print("Usage: Use %%prompt at the top of a cell to generate code.")


