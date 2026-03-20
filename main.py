import ollama

prompt = "Write a Python function to generate shortest path using Djikstra's algorithm and A* algorithm with code example."

print(f"Prompt: {prompt}")
print("Generating response...")
response = ollama.chat(
    model='autocoder', 
    messages=[
        {"role": "system", "content": "You are an expert Python engineer. Output only working Python code inside markdown blocks."},
        {"role": "user", "content": prompt}
    ]
)
print("Response:")
print(response)
print("=" * 50)
print(response.message.content)