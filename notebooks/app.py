import chainlit as cl
import os
import sys
import json
from IPython.display import display, HTML

# Add the src directory to the path
sys.path.append(os.path.abspath('..'))

# Import our RAG chatbot implementation
from src.rag_chatbot import RAGChatbot

# For visualization
from IPython.display import Image, display
import matplotlib.pyplot as plt

# Option 1: Set the API key directly (replace with your actual key)
#  API
os.environ['OPENAI_API_KEY'] = 'api keys here'
os.environ["COHERE_API_KEY"] = 'api keys here'

# Option 2: Load from a .env file or check if already set
#from dotenv import load_dotenv
#load_dotenv()  # This will load environment variables from a .env file if present

# Verify the API key is set
if "OPENAI_API_KEY" not in os.environ or not os.environ["OPENAI_API_KEY"]:
    print("⚠️ Warning: OPENAI_API_KEY is not set. Please set it before proceeding.")
else:
    print("✓ OPENAI_API_KEY is set!")

# Initialize the chatbot with GPT-3.5-Turbo
# You can also use 'gpt-4' if you have access to it
chatbot = RAGChatbot(model="gpt-4o")

print("RAG Chatbot initialized!")


try:
    # Attempt to draw the graph if LangGraph supports it
    from langgraph.graph import get_graph_representation, get_mermaid
    
    # Get the graph from our implementation
    graph = chatbot.graph.graph
    
    # Generate mermaid representation
    mermaid_representation = get_mermaid(graph)
    
    # Display as mermaid diagram
    display(HTML(f"""
    <div class="mermaid">
    {mermaid_representation}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({{startOnLoad:true}});</script>
    """))
except Exception as e:
    print(f"Could not generate graph visualization: {e}")
    print("\nFallback text representation:")
    print("Supervisor → Retrieve → Generate → Supervisor")
    print("Supervisor → Generate → Supervisor")
    print("Supervisor → Summarize → Done")
    print("Supervisor → Done")



@cl.step(type = "ChatRobot")
async def ChatRobot(query, stream=False):
    """Format the chat nicely for display"""
    print(f"🧑 User: {query}")
    print("\n")
    
    # Get the response
    try:
        if stream:
            response, steps = chatbot.chat(query, stream=True)
        else:
            response = chatbot.chat(query)
            
        # Format the response appropriately
        if isinstance(response, list) and len(response) > 0:
            if isinstance(response[-1], dict):
                print(f"🤖 Assistant: {response[-1].get('content', 'No content')}\n")
            else:
                print(f"🤖 Assistant: {response}\n")
        else:
            print(f"🤖 Assistant: {response}\n")
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None
    
    print("-" * 80)
    return response

@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    # Call the ChatRobot
    res = await ChatRobot(message.content)

    await cl.Message(content = res).send()
