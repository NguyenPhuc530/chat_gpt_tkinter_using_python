# ChatGPT Tkinter Application

This project is a simple ChatGPT application built using Python's Tkinter library for the graphical user interface (GUI) and the OpenAI API for generating responses.

## Project Structure

```
chatgpt-tkinter-app
├── src
│   ├── app.py                # Main entry point of the application
│   ├── chatgpt
│   │   ├── __init__.py       # Marks the directory as a Python package
│   │   └── gpt_client.py      # Handles communication with the OpenAI API
├── requirements.txt           # Lists the dependencies required for the project
└── README.md                  # Documentation for the project
```

## Requirements

To run this application, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the source code.
2. Go to https://platform.openai.com/api-keys to get the api_key
3. If you don't know how to do that visit this page:https://www.merge.dev/blog/chatgpt-api-key
4. Navigate to the project directory.
5. Go to openai.py and paste your openai api_key in this command:
openai.api_key = "your_api_key"
6. Run the application using the following command:

```
python chat_gpt_tkinter_using_python
```

4. A GUI window will open where you can interact with the ChatGPT model. Type your message in the input field and press Enter to receive a response.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
