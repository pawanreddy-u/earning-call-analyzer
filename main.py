from utils import extract_text_pdf,generate_response,get_prompt
def analyse_earnings(files_info,initial_prompt_loc,multi_earnings_prompt,summarize_prompt):
    for index,file in enumerate(files_info.values()):
        if index == 0:
            print(index)
            #passing the first few pages to extract the quarter and year
            system_prompt = get_prompt(initial_prompt_loc)
            content = extract_text_pdf(file)
            quarter_response = generate_response(system_prompt = system_prompt,content = content,model="gpt-4o")
        elif (index>0)&(index<len(files_info.values())-1):
            #intermediate earnings analysis
            print('intermediate',index)
            current_earnings_content = extract_text_pdf(file)
            content = f"Previous quarter pointers:{quarter_response}. Current quarterly call transcript:{current_earnings_content}"
            system_prompt = get_prompt(multi_earnings_prompt)
            quarter_response = generate_response(system_prompt = system_prompt,content = content,model="gpt-4o")
        else:
            #final analysis
            print("final",index)
            current_earnings_content = extract_text_pdf(file)
            content = f"Previous quarter pointers:{quarter_response}. Current quarterly call transcript:{current_earnings_content}"
            system_prompt = get_prompt(summarize_prompt)
            quarter_response = generate_response(system_prompt = system_prompt,content = content,model="gpt-4o")
    return quarter_response