import requests

OLLAMA_API = "http://localhost:11434/api/generate"

def summarize_blog(content):
    """
    Sends the blog content to DeepSeek running locally via Ollama API 
    and generates a summarized version.
    """
    data = {
        "model": "deepseek-r1:1.5b",  # Ensure this matches your installed model
        "prompt": f"Summarize this AWS blog with:\n1. The use case it solves.\n2. Steps involved.\n\nContent:\n{content}",
        "stream": False  # Set to True for streaming response
    }

    response = requests.post(OLLAMA_API, json=data)

    if response.status_code == 200:
        return response.json()["response"]  # Extract AI-generated summary
    else:
        return f"Error: {response.status_code}, {response.text}"

# Test the function
if __name__ == "__main__":
    test_content = "Quantum computing leverages quantum mechanics to process information in a fundamentally different way from classical computing."
    print(summarize_blog(test_content))