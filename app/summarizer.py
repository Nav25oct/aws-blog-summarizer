import requests
import json  # Needed for parsing the response

OLLAMA_API = "http://localhost:11434/api/generate"

def summarize_blog(blog_content):
    """
    Sends blog content to DeepSeek LLM via API to generate a structured summary.
    """

    prompt = f"""Summarize the following AWS blog in a structured JSON format:
    Blog Content:
    {blog_content}

    Return the summary as a JSON object with the following fields:
    {{
        "main_topic": "Brief topic of the blog",
        "challenges": ["Challenge 1", "Challenge 2"],
        "solutions": ["Solution 1", "Solution 2"],
        "services_used": ["AWS Service 1", "AWS Service 2"],
        "best_practices": ["Best Practice 1", "Best Practice 2"]
    }}

    Do not include any extra text before or after the JSON output.
    """

    data = {
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_API, json=data)

    if response.status_code == 200:
        raw_summary = response.json().get("response", "{}")  # Get response text
        try:
            structured_summary = json.loads(raw_summary)  # Convert to dictionary
            return structured_summary
        except json.JSONDecodeError:
            return {"error": "Failed to parse LLM response as JSON"}
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}