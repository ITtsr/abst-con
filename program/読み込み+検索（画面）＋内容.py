import os
import re
import tkinter as tk
from tkinter import filedialog, scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def select_file():
    root = tk.Tk()
    root.withdraw()  # Tkウィンドウを非表示にする

    file_path = filedialog.askopenfilename(
        title="LaTeXファイルを選択してください",
        filetypes=[("LaTeX files", "*.tex"), ("All files", "*.*")]
    )

    return file_path

def extract_text_from_latex(file_path):
    if not os.path.exists(file_path):
        return "File not found."
    
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # LaTeXのコメントとコマンドを除去
    content = re.sub(r"%.*", "", content)  # コメント除去
    content = re.sub(r"\\[a-zA-Z]+(?:\{.*?\})?", "", content)  # コマンド除去
    return content

def find_most_similar_text(latex_text, predefined_texts):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([latex_text] + predefined_texts)
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    best_match_index = similarity_scores.argmax()
    return predefined_texts[best_match_index]

def read_latex_file():
    file_path = select_file()
    
    if not file_path:
        result_label.config(text="ファイルが選択されませんでした。", fg="red")
        return
    
    if not os.path.isfile(file_path):
        result_label.config(text="指定されたファイルが存在しません。", fg="red")
        return
    
    if not file_path.endswith(".tex"):
        result_label.config(text="LaTeX（.tex）ファイルを指定してください。", fg="red")
        return
    
    try:
        extracted_text = extract_text_from_latex(file_path)
        if extracted_text == "File not found.":
            result_label.config(text="ファイルが見つかりませんでした。", fg="red")
            return
        
        predefined_texts = [
            "この文書は数学の証明について述べています。",
            "この文書は物理学の理論について説明しています。",
            "この文書はコンピュータサイエンスのアルゴリズムを扱っています。"
        ]
        
        best_match = find_most_similar_text(extracted_text, predefined_texts)
        result_label.config(text=f"最も類似する文章: {best_match}", fg="green")
        
        text_area.config(state=tk.NORMAL)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, extracted_text)
        text_area.config(state=tk.DISABLED)
    except Exception as e:
        result_label.config(text=f"エラー: {e}", fg="red")

# メインウィンドウの作成
root = tk.Tk()
root.title("LaTeXファイル選択（類似文検索）")
root.geometry("500x400")

# ボタンの作成
button = tk.Button(root, text="ファイル選択", command=read_latex_file)
button.pack(pady=10)

# 結果表示用ラベル
result_label = tk.Label(root, text="", wraplength=450)
result_label.pack(pady=10)

# ファイル内容表示エリア
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=60)
text_area.pack(pady=10)
text_area.config(state=tk.DISABLED)

# メインループの開始
root.mainloop()
