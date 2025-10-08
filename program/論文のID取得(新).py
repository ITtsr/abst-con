
import tkinter as tk
from tkinter import scrolledtext

def display_text():
    # 証明文を取得して下に表示
    proof_text = input_text.get("1.0", tk.END).strip()
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, proof_text)

    # Arxiv IDを取得して下に表示
    arxiv_id = arxiv_entry.get().strip()
    arxiv_output.delete("1.0", tk.END)
    arxiv_output.insert(tk.END, f"Arxiv ID: {arxiv_id}")

# ウィンドウ作成
root = tk.Tk()
root.title("Arxiv表示プログラム")

# 証明文入力欄
tk.Label(root, text="証明を入力").pack()
input_text = scrolledtext.ScrolledText(root, width=70, height=6)
input_text.pack()

# Arxiv ID入力欄
tk.Label(root, text="Arxiv IDを入力").pack()
arxiv_entry = tk.Entry(root, width=50)
arxiv_entry.pack()

# ボタン
tk.Button(root, text="テキストをキャンバスに表示", command=display_text).pack(pady=10)

# 出力エリア（証明文）
tk.Label(root, text="入力内容").pack()
output_text = scrolledtext.ScrolledText(root, width=70, height=6)
output_text.pack()

# 出力エリア（Arxiv ID）
tk.Label(root, text="入力したArxiv ID").pack()
arxiv_output = scrolledtext.ScrolledText(root, width=70, height=3)
arxiv_output.pack()

# メインループ
root.mainloop()

"""The Erdos-Kac theorem, a foundational result in probabilistic number theory, states that the number of prime factors of an integer follows a Gaussian distribution. In this paper we develop and analyze probabilistic models for "random integers" to study the mechanisms underlying this theorem. We begin with a simple model, where each prime p is chosen as a divisor with probability 1/p in a sequence of independent trials. A preliminary analysis shows that this construction almost surely yields an integer with infinitely many prime factors. To create a tractable framework, we study a truncated version Nx = product of p<=x of p^Xp, where Xp are independent Bernoulli(1/p) random variables. We prove an analogue of the Erdos-Kac theorem within this framework, showing that the number of prime factors omega(Nx) satisfies a central limit theorem with mean and variance asymptotic to log log x."""
"""2509.04102"""