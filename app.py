import ollama

def chatbot():
    print("\n🤖 Gemma Assistant initialized! Type 'exit' to quit.\n")
    messages = [{"role": "system", "content": "You are a helpful, friendly, and concise AI assistant."}]
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        messages.append({"role": "user", "content": user_input})
        print("Gemma: ", end="", flush=True)
        response_stream = ollama.chat(model='gemma2:2b', messages=messages, stream=True)
        full_response = ""
        for chunk in response_stream:
            content = chunk['message']['content']
            print(content, end="", flush=True)
            full_response += content
        print("\n")
        messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    chatbot()
