import arxiv
import requests
import fitz  # PyMuPDF
import io
import re
import tkinter as tk
from tkinter import messagebox, scrolledtext

def download_pdf(arxiv_id):
    search = arxiv.Search(id_list=[arxiv_id])
    client = arxiv.Client(num_retries=3, delay_seconds=3)
    results = client.results(search)
    result = next(results, None)

    if result is None:
        raise ValueError("論文が見つかりません。")
    
    pdf_url = result.pdf_url
    response = requests.get(pdf_url)
    response.raise_for_status()
    return io.BytesIO(response.content), result.title

def extract_proof_sections(pdf_stream):
    doc = fitz.open(stream=pdf_stream, filetype="pdf")
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    pattern = r"(Proof(?: of [^\n\r:]+)?)[\s:]*\n(.*?)(?=\n[A-Z][^\n]{0,100}\n|\Z)"
    matches = re.findall(pattern, full_text, re.DOTALL)

    if not matches:
        return "『Proof』セクションが見つかりませんでした。"

    output = ""
    for i, (heading, content) in enumerate(matches, 1):
        output += f"\n--- Proof {i}: {heading} ---\n"
        output += content.strip()[:3000] + "\n"
    
    return output

def on_extract():
    arxiv_id = entry.get().strip()
    if not arxiv_id:
        messagebox.showwarning("入力エラー", "arXiv IDを入力してください。")
        return

    try:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "処理中...\n")
        root.update()

        pdf_stream, title = download_pdf(arxiv_id)
        result = extract_proof_sections(pdf_stream)

        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, f"論文タイトル: {title}\n")
        text_output.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("エラー", str(e))

# GUI設定
root = tk.Tk()
root.title("arXiv Proof Extractor")

tk.Label(root, text="arXiv ID を入力してください:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Proofセクション抽出", command=on_extract).pack(pady=5)

text_output = scrolledtext.ScrolledText(root, width=100, height=30)
text_output.pack(padx=10, pady=10)

root.mainloop()