import os
from PyPDF2 import PdfReader
from openai import OpenAI

def extract_text_pdf(file_location,num_pages=None):
    # Read the file utilizing the PyPDF library.
    reader = PdfReader(file_location)
    # Obtain the total number of pages as an integer
    pages = len(reader.pages)
    extracted_text_lst = []
    if num_pages:
        total_pages = range(num_pages)
    else:
        total_pages = range(pages)
    # Extract the text from each page
    print(len(total_pages))
    for page, _ in enumerate(total_pages):
        read = reader.pages[page]
        text = read.extract_text()
        extracted_text_lst.append(text)
    extracted_text = " ".join(extracted_text_lst)
    return extracted_text

def generate_response(system_prompt,content,model="gpt-4o"):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content}
        ],
        #max_tokens=1000,
        #n=1,
        #temperature=0.7
        )
    return response.choices[0].message.content

def sort_quarter_dict(quarter_dict):
    def quarter_key(item):
        quarter, year = item[0].split('_')  # Split 'q4_2024' into 'q4' and '2024'
        quarter_num = int(quarter[1])       # Extract '4' from 'q4'
        year_num = int(year)                # Convert '2024' to integer
        return (year_num, quarter_num)      # Sort by year first, then quarter

    sorted_items = sorted(quarter_dict.items(), key=quarter_key, reverse=False)
    return dict(sorted_items)

def extract_quarter_info(files,prompt_loc = "prompts/extract_quarter.prompt"):
    files_info = {}
    for file_name in files:
        #passing the first few pages to extract the quarter and year
        with open(prompt_loc, "r") as prompt_file:
            system_prompt = prompt_file.read()
        content = extract_text_pdf(file_name,num_pages=3)
        result = generate_response(system_prompt,content)
        #print(file_name,result)
        files_info[result] = file_name
    return sort_quarter_dict(files_info)

def get_prompt(prompt_loc):
    with open(prompt_loc, "r") as prompt_file:
        prompt = prompt_file.read()
    return prompt
