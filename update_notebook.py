import json
import os

notebook_path = os.path.join(os.path.dirname(__file__), 'Anthropic 1P/00_Tutorial_How-To.ipynb')

with open(notebook_path, 'r') as f:
    nb = json.load(f)

for cell in nb['cells']:
    # Replace pip install
    if cell['cell_type'] == 'code' and '!pip install anthropic' in ''.join(cell['source']):
        cell['source'] = ['!pip install anthropic python-dotenv']
    
    # Replace markdown instructions
    if cell['cell_type'] == 'markdown' and '3. Set up your API key' in ''.join(cell['source']):
        cell['source'] = ["3. Set up your API key and model name. We recommend using a `.env` file to store your API key. Create a file named `.env` in this directory and add `ANTHROPIC_API_KEY=your_api_key_here` to it."]
    
    # Replace API key loading logic
    if cell['cell_type'] == 'code' and 'API_KEY = "your_api_key_here"' in ''.join(cell['source']):
        cell['source'] = [
            "import os\n",
            "from dotenv import load_dotenv\n",
            "\n",
            "# Load environment variables from .env file\n",
            "load_dotenv()\n",
            "\n",
            "API_KEY = os.getenv(\"ANTHROPIC_API_KEY\")\n",
            "MODEL_NAME = \"claude-3-haiku-20240307\"\n",
            "\n",
            "if not API_KEY:\n",
            "    print(\"ERROR: ANTHROPIC_API_KEY not found. Please check your .env file.\")\n",
            "\n",
            "# Stores the API_KEY & MODEL_NAME variables for use across notebooks within the IPython store\n",
            "%store API_KEY\n",
            "%store MODEL_NAME"
        ]

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
