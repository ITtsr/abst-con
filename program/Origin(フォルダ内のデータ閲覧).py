import os
import tkinter as tk
from tkinter import scrolledtext

MAIN_FOLDER = "U:\課題研究\新\全体設計プログラム\データベースⅡ（仮）"  # 固定フォルダーのパスを設定

def list_folders(parent_folder):
    for widget in frame.winfo_children():
        widget.destroy()
    
    folders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]
    
    for folder in folders:
        folder_path = os.path.join(parent_folder, folder)
        btn = tk.Button(frame, text=folder, command=lambda p=folder_path: list_files_and_folders(p))
        btn.pack(pady=5, fill='x')

def list_files_and_folders(folder_path):
    for widget in frame.winfo_children():
        widget.destroy()
    
    items = os.listdir(folder_path)
    
    for item in items:
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            btn = tk.Button(frame, text=item, command=lambda p=item_path: list_files_and_folders(p))
        else:
            btn = tk.Button(frame, text=item, command=lambda p=item_path: display_file_content(p))
        btn.pack(pady=5, fill='x')
    
    back_btn = tk.Button(frame, text="Back", command=lambda: list_folders(MAIN_FOLDER))
    back_btn.pack(pady=10, fill='x')

def display_file_content(file_path):
    for widget in frame.winfo_children():
        widget.destroy()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        content = f"Error reading file: {e}"
    
    text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=15)
    text_area.insert(tk.INSERT, content)
    text_area.config(state=tk.DISABLED)
    text_area.pack(pady=10, fill='both', expand=True)
    
    back_btn = tk.Button(frame, text="Back", command=lambda: list_files_and_folders(os.path.dirname(file_path)))
    back_btn.pack(pady=10, fill='x')

root = tk.Tk()
root.title("Folder Browser")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=20, fill='both', expand=True)

list_folders(MAIN_FOLDER)

root.mainloop()
