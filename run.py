import subprocess
from gemini_script import convert_paragraph_to_steps
import json




def run_node_script(json_file):
    try:
        # Run the Node.js script with the specified JSON file
        result = subprocess.run(
            ["node", "./dist/cli.js", json_file],
            capture_output=True,
            text=True,
            check=True
        )
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

# Example usage
if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
    if (len(paragraph) > 0):
        # Convert a paragraph to steps using the Python function
        steps = convert_paragraph_to_steps(paragraph)
        
        # Save the steps to a JSON file
        json_file = "steps.json"
        with open(json_file, "w") as f:
            json.dump(steps, f, indent=4)
        
        # Run the Node.js script with the generated JSON file
        run_node_script(json_file)
        exit(0)
    # Convert a paragraph to steps using the Python function
    paragraph = "Go to google.com, search for 'toothpaste', click on the first link, add to cart, wait for 2 seconds, and then click on checkout."
    steps = convert_paragraph_to_steps(paragraph)
    
    # Save the steps to a JSON file
    json_file = "steps.json"
    with open(json_file, "w") as f:
        json.dump(steps, f, indent=4)
    
    # Run the Node.js script with the generated JSON file
    run_node_script(json_file)