import os
import json
import requests
from dotenv import load_dotenv
import re

def convert_paragraph_to_steps(paragraph):
    """
    Converts a paragraph into a JSON format with steps using the Gemini API.

    Args:
        paragraph (str): The input paragraph to convert.

    Returns:
        dict: The JSON output with steps or an error message.
    """
    # Load environment variables from .env file
    if not load_dotenv(override=True):
        raise FileNotFoundError(".env file not found. Please create one with the required API key.")

    # Read the API key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set in the .env file.")

    GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    HEADERS = {
        "Content-Type": "application/json"
    }

    # Define the prompt
    prompt = f"""
    You are an expert at converting paragraphs into a series of steps.
    Given the following paragraph, convert it into a JSON format with a "steps" array.
    Each step should have one of the following keys: "goto", "act", or "wait".
    "goto" should be used when navigating to a URL.
    "act" should be used for actions like searching, clicking, or pressing a button.
    "wait" should be used to specify a delay in seconds.
    press enter /click should be used for actions like searching.

    Example Output:
    {{
        "steps": [
            {{ "goto": "https://www.youtube.com"}},
            {{ "act": "search for 'funny cat videos'"}},
            {{ "act": "press enter"}},
            {{ "wait": 2}},
            {{ "act": "click on the first video" }},
            {{ "wait": 2}},
            {{ "act": "wait for the page to load" }},
            {{ "wait": 2}},
            {{ "act": "click on the play button" }}
        ]
    }}

    Paragraph:
    {paragraph}

    Output:
    """

    # Prepare the request body
    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    # Make the API request
    response = requests.post(GEMINI_API_URL, headers=HEADERS, json=body)

    if response.status_code != 200:
        return {
            "error": f"API request failed with status code {response.status_code}: {response.text}"
        }

    try:
        # Parse the response
        text_output = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        # Clean markdown backticks
        clean_text = re.sub(r"```(?:json)?", "", text_output).strip()
        return json.loads(clean_text)
    except (KeyError, json.JSONDecodeError) as e:
        return {"error": f"Failed to parse response: {str(e)}", "raw": response.text}

# Example usage
if __name__ == "__main__":
    paragraph = "Go to google.com, search for 'toothpaste', click on the first link, add to cart, wait for 2 seconds, and then click on checkout."
    steps = convert_paragraph_to_steps(paragraph)
    print(json.dumps(steps, indent=4))