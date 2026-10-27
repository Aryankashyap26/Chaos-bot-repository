# Gemma Bot Repository

A simple streaming CLI chatbot powered by Google's Gemma 2 (2B) model using [Ollama](https://ollama.ai).

## Prerequisites

1. Install and run [Ollama](https://ollama.ai).
2. Pull the Gemma 2 model:
   ```bash
   ollama pull gemma2:2b
   ```

## Setup & Running

1. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Run the chatbot:
   ```bash
   python3 app.py
   ```

3. To exit the chat, type `exit`, `/exit`, `quit`, or press `Ctrl + C`.