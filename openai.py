import tkinter as tk
from tkinter import scrolledtext
import openai

# === CẤU HÌNH API ===
openai.api_key = ""

# === GỌI CHATGPT ===
def get_gpt_response(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # hoặc "gpt-4" nếu bạn có quyền
            messages=[
                {"role": "system", "content": "Bạn là một trợ lý thông minh."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Lỗi: {str(e)}"

# === HÀM GỬI TIN NHẮN ===
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    chat_window.insert(tk.END, "Bạn: " + user_input + "\n", 'user')
    entry.delete(0, tk.END)

    chat_window.insert(tk.END, "ChatGPT đang trả lời...\n", 'bot')
    chat_window.update()

    response = get_gpt_response(user_input)
    
    chat_window.insert(tk.END, "ChatGPT: " + response + "\n", 'bot')
    chat_window.see(tk.END)

# === TẠO GIAO DIỆN ===
root = tk.Tk()
root.title("ChatGPT - Tkinter GUI + OpenAI")
root.geometry("600x600")

# Cửa sổ hiển thị đoạn chat
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.tag_config('user', foreground='blue')
chat_window.tag_config('bot', foreground='green')

# Entry để nhập văn bản
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(fill=tk.X, padx=10, pady=5)
entry.bind("<Return>", lambda event=None: send_message())

# Nút gửi
send_button = tk.Button(root, text="Gửi", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

# Chạy app
root.mainloop()
