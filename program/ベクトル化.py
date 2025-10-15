from transformers import AutoTokenizer, AutoModel
import torch

def latex_to_vector(text: str, model_path: str = "witiko/mathberta") -> torch.Tensor:
    """
    LaTeX形式の文章を768次元のベクトルに変換する。

    Parameters:
    - text (str): LaTeXを含む文章
    - model_path (str): ローカルに保存されたMathBERTaのパスまたはHuggingFaceのモデル名

    Returns:
    - torch.Tensor: 文全体の768次元ベクトル（[CLS]トークンの表現）
    """
    # トークナイザーとモデルの読み込み
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModel.from_pretrained(model_path)
    model.eval()

    # 入力テキストのトークン化
    inputs = tokenizer(text, return_tensors="pt")

    # 勾配を計算しないモードでベクトル化
    with torch.no_grad():
        outputs = model(**inputs)
        # [CLS] トークンのベクトルを抽出
        cls_embedding = outputs.last_hidden_state[0, 0, :]

    return cls_embedding

# 使用例
if __name__ == "__main__":
    sample_text = "This is an example sentence with a formula [MATH] a^2 + b^2 = c^2 [/MATH]."
    vector = latex_to_vector(sample_text, model_path="./models/mathberta")  # ローカルパスに変更可
    print("768次元ベクトル:\n", vector)
    print("次元数:", vector.shape[0])

