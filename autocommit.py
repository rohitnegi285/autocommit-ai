import google.generativeai as genai
import os
from dotenv import load_dotenv
import subprocess
# Load environment variables from .env file

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key: 
    raise ValueError("GOOGLE_API_KEY environment variable not set") 

genai.configure(api_key=api_key)    
model = genai.GenerativeModel("gemini-2.0-flash")

COMMIT_MESSAGE_PROMPT = """
Analyze the following git diff for the staged changes and generate a concise, professional commit message. The message must follow the Conventional Commits specification.

The structure should be:
<type>[optional scope]: <description>

[optional body]

Examples of <type>:
- feat: A new feature
- fix: A bug fix
- docs: Documentation only changes
- refactor: A code change that neither fixes a bug nor adds a feature
- test: Adding missing tests or correcting existing tests
- chore: Changes to the build process or auxiliary tools

Provide only the commit message, with no extra text or explanations before or after it.

Here is the git diff:
---
{diff}
---
"""

def get_staged_diff():
    """Get the staged git diff."""
    try:
        result = subprocess.run(
            ["git", "diff", "--staged"],
            check=True,
            text=True,
            capture_output=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error getting staged diff: {e}")
        return None, f"An Error while getting staged diff: {e}"
    
def generate_commit_message(diff: str): 
    """Generate a commit message based on the staged git diff."""
    if not diff:
        return "No changes staged for commit."

    prompt = COMMIT_MESSAGE_PROMPT.format(diff=diff)
    
    try:
        response = model.generate_content(prompt)
        commit_message = response.text.strip()
        return commit_message
    except Exception as e:
        print(f"Error generating commit message: {e}")
        return f"An Error while generating commit message: {e}"    
    
if __name__ == "__main__":
    print("🤖 AutoCommit: Analyzing your staged changes...")

    staged_diff = get_staged_diff()
    if staged_diff:
        commit_message = generate_commit_message(staged_diff)
        print(commit_message)
    else:
        print("No staged changes found.")
    
    commit_message = generate_commit_message(staged_diff)
    print("\n" + "="*50)
    print("✨ AI Suggested Commit Message:")
    print("="*50)
    print(commit_message)
    print("="*50)