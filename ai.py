import tkinter as tk
from tkinter import scrolledtext
import openai

# Set your OpenAI API key
openai.api_key = ""

def chat_with_gpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="dall-e-3",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def send_message():
    user_message = user_input.get()
    if not user_message.strip():
        return

    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_message}\n")
    chat_history.config(state=tk.DISABLED)

    user_input.delete(0, tk.END)

    response = chat_with_gpt(user_message)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"ChatGPT: {response}\n\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)

# Create the main application window
root = tk.Tk()
root.title("ChatGPT Tkinter App")

# Chat history display
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=20, width=50)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# User input field
user_input = tk.Entry(root, width=40)
user_input.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the application
root.mainloop()