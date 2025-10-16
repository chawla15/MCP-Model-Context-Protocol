# MCP-Model-Context-Protocol

A demonstration of the Model Context Protocol (MCP) using LangChain and GPT-4. This project showcases how to build context-aware AI applications that maintain and utilize conversation context for more personalized and relevant responses.

## What is Model Context Protocol (MCP)?

The Model Context Protocol is an approach to managing and utilizing context in language model interactions. It enables:
- **Context Awareness**: Maintaining user preferences, conversation history, and relevant background information
- **Personalized Responses**: Tailoring AI responses based on accumulated context
- **Improved Continuity**: Creating more coherent multi-turn conversations

## Features

✨ **Context-Aware LLM Chain**: Demonstrates how to inject context into prompts using LangChain

🔑 **Secure API Key Management**: Uses python-dotenv for environment variable handling

🎯 **GPT-4 Integration**: Leverages OpenAI's GPT-4 model for intelligent responses

📝 **Practical Example**: Includes a complete working example with sample context and user input

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/chawla15/MCP-Model-Context-Protocol.git
cd MCP-Model-Context-Protocol
```

2. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

3. **Create a `.env` file** in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

To run the main application:
```bash
python main.py
```

This will execute the MCP example, demonstrating how context is loaded, managed, and used in a conversation with GPT-4.

## Code Example

Here's the core implementation from `main.py`:

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Load environment variables
load_dotenv()

def run_mcp_example():
    """Demonstrates Model Context Protocol with LangChain and GPT-4"""
    
    # Initialize GPT-4 model
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Define conversation context
    context = {
        "user_name": "Alice",
        "previous_topic": "artificial intelligence and machine learning",
        "user_preference": "technical explanations with practical examples"
    }
    
    # Create context-aware prompt template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. The user's name is {user_name}. "
                   "They previously discussed {previous_topic}. "
                   "They prefer {user_preference}."),
        ("user", "{user_input}")
    ])
    
    # Build the LLM chain
    chain = prompt_template | llm | StrOutputParser()
    
    # Execute with context
    response = chain.invoke({
        "user_name": context["user_name"],
        "previous_topic": context["previous_topic"],
        "user_preference": context["user_preference"],
        "user_input": "Can you explain how context is used in language models?"
    })
    
    return response
```

## How It Works

1. **Environment Setup**: The application loads the OpenAI API key from environment variables using `python-dotenv`

2. **Context Definition**: User-specific context is defined including:
   - User name for personalization
   - Previous conversation topics for continuity
   - User preferences for response style

3. **Prompt Engineering**: A `ChatPromptTemplate` is created that injects context into the system message, ensuring the AI is aware of the user's background

4. **LLM Chain Creation**: LangChain's chain syntax (`|` operator) connects:
   - Prompt template → GPT-4 model → String output parser

5. **Context-Aware Execution**: The chain is invoked with both context and user input, producing a personalized response

## Example Output

```
Initializing MCP Example with LangChain and GPT-4...

Context Information:
  - User: Alice
  - Previous Topic: artificial intelligence and machine learning
  - Preference: technical explanations with practical examples

User Input: Can you explain how context is used in language models?

AI Response:
Hi Alice! Since you're interested in AI and ML, let me explain context in language models...
[Personalized response based on context]

MCP Example completed successfully!
```

## Project Structure

```
MCP-Model-Context-Protocol/
├── main.py              # Main application with MCP implementation
├── requirements.txt     # Project dependencies
├── README.md           # Project documentation
└── .env                # Environment variables (create this file)
```

## Dependencies

- **langchain**: Framework for developing applications powered by language models
- **langchain-openai**: OpenAI integration for LangChain
- **openai**: Official OpenAI Python client library
- **python-dotenv**: Environment variable management

## Use Cases

This MCP implementation can be extended for:
- 🤖 **Chatbots** that remember user preferences
- 📚 **Educational assistants** that adapt to learning styles
- 💼 **Business applications** that maintain customer context
- 🔍 **Research tools** that track investigation topics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
