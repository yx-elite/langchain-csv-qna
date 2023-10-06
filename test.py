## Add results export features

import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def main():
    load_dotenv()
    st.set_page_config(page_title="AI CSV QnA Bot")
    st.header("🤖 AI CSV QnA Bot")
    
    # Upload CSV file
    user_csv = st.file_uploader("Upload your CSV", type="csv")
    
    if user_csv is not None:
        user_prompt = st.text_input("Ask a question about your CSV:")
        response = ""
        
        if user_prompt:
            llm = OpenAI(temperature=0)
            agent = create_csv_agent(llm, user_csv, verbose=True)   # Think automatically
            
            try:
                with st.spinner("Generating answer..."):
                    with get_openai_callback() as cb:
                        response = agent.run(user_prompt)
                        print(cb)
                        
                st.success("Answer is generated successfully")
                
                # Export results
                export_result(response, user_csv)
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            
        st.write(response)


def export_result(response, user_csv):
    # Create a DataFrame with the response
    df = pd.DataFrame({'Answer': [response]})
    
    # Add relevant CSV data to the DataFrame
    csv_data = pd.read_csv(user_csv)
    df['CSV Data'] = csv_data.to_string(index=False)
    
    # Export DataFrame to Excel file
    excel_file = 'qna_results.xlsx'
    df.to_excel(excel_file, index=False)
    
    # Provide download link to the user
    st.markdown(f"Download the results as an Excel file: [Download]({excel_file})")


if __name__ == '__main__':
    main()
