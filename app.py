import gradio as gr
import os
from langchain_community.chat_models import ChatXAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase

# Load or save API key
API_KEY_FILE = "api_key.txt"

def load_api_key():
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, 'r') as f:
            return f.read().strip()
    return ""

def save_api_key(api_key):
    with open(API_KEY_FILE, 'w') as f:
        f.write(api_key)
    return "API key saved!"

# Initialize database and LLM
db = SQLDatabase.from_uri("sqlite:///vaers.db")

def query_vaers(question, api_key):
    if not api_key:
        return "Please enter your xAI API key."
    
    # Save API key if provided
    save_api_key(api_key)
    
    try:
        # Set up LLM with Grok model
        llm = ChatXAI(xai_api_key=api_key, model="grok-beta")
        db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
        
        # Run query
        response = db_chain.run(question)
        return response
    except Exception as e:
        return f"Error: {str(e)}. Check your API key or question."

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# VAERS LLM App")
    gr.Markdown("Enter your xAI API key (get one at https://x.ai/api) and ask questions about VAERS data.")
    
    api_key_input = gr.Textbox(
        label="xAI API Key",
        value=load_api_key(),
        placeholder="Enter your xAI API key",
        type="password"
    )
    question_input = gr.Textbox(
        label="Ask a question",
        placeholder="E.g., How many death reports for COVID vaccines in 2021?"
    )
    output = gr.Textbox(label="Answer")
    
    submit_btn = gr.Button("Submit")
    submit_btn.click(
        fn=query_vaers,
        inputs=[question_input, api_key_input],
        outputs=output
    )

demo.launch()
