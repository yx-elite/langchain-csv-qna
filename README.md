# AI CSV Q&A Agent

Upload a CSV file and ask questions about the data in plain English. An AI agent writes and runs pandas code to work out each answer.

> 📦 **Status:** Archived · 2023 learning project
> Built with LangChain `0.0.305` and the OpenAI SDK `0.28`. The CSV agent has since moved to `langchain-experimental`, so the code won't run on current versions without changes.

## Overview

Answering questions about tabular data usually means writing queries or code. This app lets a language model do that part: it decides what analysis is needed, runs it, and explains the result.

## Architecture

1. **Upload:** the CSV is loaded into a pandas DataFrame
2. **Reason:** GPT (temperature 0, for consistent output) plans the steps needed to answer the question
3. **Act:** the agent writes pandas code, runs it, and reads the result
4. **Repeat:** it continues reasoning and acting until it can answer, then replies in plain English

Token usage and cost for each question are logged to the console. A `sample_data.csv` file is included for testing.

## Tech Stack

Python · Streamlit · LangChain agents · OpenAI API · pandas

## Getting Started

```bash
cp .env.example .env            # add your OPENAI_API_KEY
pip install -r requirements.txt
streamlit run app.py
```

`test.py` is a work-in-progress version that experiments with exporting results to Excel.

## Lessons Learned

- **Agents vs. chat:** built in September 2023, during the first wave of LLM agents. My first hands-on project where an LLM decides on an action, carries it out and checks the result, instead of only generating text
- **Security:** the agent runs code the model generates. That's acceptable in a local demo, but in production it needs a sandbox, least-privilege permissions and input validation
