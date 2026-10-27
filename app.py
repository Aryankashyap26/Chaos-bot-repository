import ollama

EXIT_COMMANDS = {
    "exit", "/exit", ".exit", "exit()",
    "quit", "/quit", ".quit", "quit()",
    "bye", "/bye", "q", ":q"
}

def chatbot():
    print("\n🤖 Gemma Assistant initialized! Type 'exit' or '/exit' to quit.\n")
    messages = [{"role": "system", "content": "You are a helpful, friendly, and concise AI assistant."}]
    
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        # Flexible exit check (e.g. /exit, exit, quit, :q, etc.)
        clean_input = user_input.lower().rstrip("()").lstrip("/.")
        if clean_input in {"exit", "quit", "bye", "q"} or user_input.lower() in EXIT_COMMANDS:
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})
        print("Gemma: ", end="", flush=True)
        
        try:
            response_stream = ollama.chat(model='gemma2:2b', messages=messages, stream=True)
            full_response = ""
            for chunk in response_stream:
                content = chunk['message']['content']
                print(content, end="", flush=True)
                full_response += content
            print("\n")
            messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            print(f"\n[Error: {e}]\n")

if __name__ == "__main__":
    chatbot()

