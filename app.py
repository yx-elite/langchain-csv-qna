import streamlit as st
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
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            
        st.write(response)


if __name__ == '__main__':
    main()