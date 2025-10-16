import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Load environment variables from .env file
load_dotenv()

def run_mcp_example():
    """
    Demonstrates a simple Model Context Protocol (MCP) example.
    
    This function:
    - Loads OpenAI API key from environment
    - Creates a GPT-4 LLM chain using LangChain
    - Runs a context-aware prompt showing how context is retrieved and used
    - Returns the AI response
    """
    # Verify API key is loaded
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    print("Initializing MCP Example with LangChain and GPT-4...\n")
    
    # Initialize GPT-4 model
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.7,
        api_key=api_key
    )
    
    # Define context that will be used in the conversation
    context = {
        "user_name": "Alice",
        "previous_topic": "artificial intelligence and machine learning",
        "user_preference": "technical explanations with practical examples"
    }
    
    # Create a context-aware prompt template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. The user's name is {user_name}. "
                   "They previously discussed {previous_topic}. "
                   "They prefer {user_preference}."),
        ("user", "{user_input}")
    ])
    
    # Create the LLM chain
    chain = prompt_template | llm | StrOutputParser()
    
    # Example user input
    user_input = "Can you explain how context is used in language models?"
    
    print(f"Context Information:")
    print(f"  - User: {context['user_name']}")
    print(f"  - Previous Topic: {context['previous_topic']}")
    print(f"  - Preference: {context['user_preference']}")
    print(f"\nUser Input: {user_input}\n")
    
    # Run the chain with context
    response = chain.invoke({
        "user_name": context["user_name"],
        "previous_topic": context["previous_topic"],
        "user_preference": context["user_preference"],
        "user_input": user_input
    })
    
    print(f"AI Response:\n{response}\n")
    print("MCP Example completed successfully!")
    
    return response

def main():
    """
    Main function to run the MCP example.
    """
    try:
        run_mcp_example()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have:")
        print("1. Created a .env file with your OPENAI_API_KEY")
        print("2. Installed requirements: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
