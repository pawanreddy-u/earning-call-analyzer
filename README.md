## Example Usage

The following Python script demonstrates how to use the `analyse_earnings` function to analyze earnings call transcripts and summarize insights:

```python
# Ensure the necessary dependencies are installed
# pip install pypdf2  # For working with PDF files
# pip install openai  # For interacting with OpenAI models

# Importing required functions
from main import analyse_earnings  # Function to perform analysis on earnings call data
from utils import extract_quarter_info  # Utility function to extract quarter-wise information from transcript files

# Define the list of transcript files to be analyzed
files = [
    'transcripts/apr_laurus.pdf', 
    'transcripts/jan_laurus.pdf', 
    'transcripts/Jul_laurus.pdf', 
    'transcripts/oct_laurus.pdf'
]

# Define the paths to the prompt files
initial_prompt_loc = 'prompts/analyse_earnings.prompt'  # Prompt file for single-quarter analysis
multi_earnings_prompt = 'prompts/analyze_multiple_earnings.prompt'  # Prompt file for multi-quarter analysis
summarize_prompt = 'prompts/summarize.prompt'  # Prompt file for summarizing the results

# Extract quarter information from the list of transcript files
files_info = extract_quarter_info(files=files)
print(files_info)  # Print the extracted information for debugging purposes

# Perform earnings analysis using the specified prompts and extracted file info
result = analyse_earnings(files_info, initial_prompt_loc, multi_earnings_prompt, summarize_prompt)
print(result)  # Output the final analysis results
