import tkinter as tk
from tkinter import scrolledtext

class CanvasTextInputUI:
    def __init__(self, root):
        self.root = root
        self.root.title("予想保存 UI")

        # テキスト入力欄
        self.text_input = scrolledtext.ScrolledText(root, width=70, height=5, wrap=tk.WORD)
        self.text_input.pack(pady=10)

        # ボタン
        self.submit_button = tk.Button(root, text="テキストをキャンバスに表示", command=self.display_text_on_canvas)
        self.submit_button.pack()

    def display_text_on_canvas(self):
        text = self.text_input.get("1.0", tk.END).strip()
        self.canvas.delete("all")  # キャンバスをリセット
        self.canvas.create_text(10, 10, anchor='nw', text=text, font=("Arial", 12), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasTextInputUI(root)
    root.mainloop()