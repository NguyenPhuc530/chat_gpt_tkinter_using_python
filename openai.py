import os
import threading
import tkinter as tk
from tkinter import scrolledtext
import openai

# Lấy API key từ biến môi trường (không hardcode)
openai.api_key = os.getenv("OPENAI_API_KEY", "")

if not openai.api_key:
    print("Warning: OPENAI_API_KEY environment variable is not set. Set it before running the app.")

# Lưu conversation history để duy trì context
messages = [
    {"role": "system", "content": "Bạn là một trợ lý thông minh và lịch sự."}
]

def get_gpt_response(prompt):
    messages.append({"role": "user", "content": prompt})
    try:
        # Gọi API đúng theo SDK OpenAI
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=512
        )
        assistant_message = resp.choices[0].message["content"].strip()
        messages.append({"role": "assistant", "content": assistant_message})
        return assistant_message
    except Exception as e:
        return f"Lỗi khi gọi OpenAI: {str(e)}"

def send_message_background(user_input):
    response = get_gpt_response(user_input)
    def ui_update():
        # Xóa dòng "đang trả lời..." nếu muốn — ở đây chỉ thêm phản hồi
        chat_window.insert(tk.END, "ChatGPT: " + response + "\n", 'bot')
        chat_window.see(tk.END)
        send_button.config(state=tk.NORMAL)
        entry.config(state=tk.NORMAL)
    root.after(0, ui_update)

def send_message(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return
    chat_window.insert(tk.END, "Bạn: " + user_input + "\n", 'user')
    entry.delete(0, tk.END)
    chat_window.insert(tk.END, "ChatGPT đang trả lời...\n", 'bot')
    chat_window.see(tk.END)

    send_button.config(state=tk.DISABLED)
    entry.config(state=tk.DISABLED)

    threading.Thread(target=send_message_background, args=(user_input,), daemon=True).start()

# === Tạo giao diện ===
root = tk.Tk()
root.title("ChatGPT - Tkinter GUI + OpenAI")
root.geometry("600x600")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.tag_config('user', foreground='blue')
chat_window.tag_config('bot', foreground='green')

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(fill=tk.X, padx=10, pady=5)
entry.bind("<Return>", send_message)

send_button = tk.Button(root, text="Gửi", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

root.mainloop()