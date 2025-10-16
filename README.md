# MCP-Model-Context-Protocol

## Project Summary

The MCP (Model Context Protocol) project is a Python-based implementation designed to facilitate context management for language models. This project leverages LangChain for building language model applications and OpenAI GPT-4.0 for advanced natural language processing capabilities.

### Features
- Integration with LangChain framework
- OpenAI GPT-4.0 model support
- Modular architecture for easy extension
- Environment-based configuration management

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/chawla15/MCP-Model-Context-Protocol.git
cd MCP-Model-Context-Protocol
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

To run the main application:

```bash
python main.py
```

This will execute the main function and initialize the MCP Model Context Protocol.

## Project Structure

```
MCP-Model-Context-Protocol/
├── main.py              # Main application entry point
├── requirements.txt     # Project dependencies
├── README.md           # Project documentation
└── .env                # Environment variables (create this file)
```

## Dependencies

- **langchain**: Framework for developing applications powered by language models
- **openai**: Official OpenAI Python client library
- **python-dotenv**: Environment variable management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
