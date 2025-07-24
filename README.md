# AutoCommit 🤖

AutoCommit is a Python tool that uses Google's Gemini AI to automatically generate conventional commit messages based on your staged git changes.

## Features

- Analyzes `git diff --staged` output.
- Uses the Gemini API to generate a high-quality commit message.
- Follows the [Conventional Commits](https://www.conventionalcommits.org/) specification.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/autocommit.git
    cd autocommit
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    # Create venv
    python -m venv .venv
    # Activate it (Windows)
    .venv\Scripts\activate
    # Or (macOS/Linux)
    source .venv/bin/activate
    # Install packages
    pip install -r requirements.txt 
    ```
    *(Note: You will need to create a `requirements.txt` file by running `pip freeze > requirements.txt`)*

3.  **Set up your API Key:**
    - Get your API key from [Google AI Studio](https://aistudio.google.com/).
    - Create a file named `.env` in the project root.
    - Add your key to the `.env` file: `GOOGLE_API_KEY="YOUR_API_KEY_HERE"`

## Usage

1.  Stage your changes using `git add .` or `git add <file>`.
2.  Run the script:
    ```bash
    python autocommit.py
    ```
3.  The tool will print a suggested commit message. Copy and paste it into your `git commit` command.