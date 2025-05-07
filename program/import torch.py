import torch
from transformers import AutoTokenizer, AutoModel

class LatexVectorizer:
    def __init__(self, model_name="CanvasAI/MathBERTa"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)

    def vectorize(self, latex_text: str) -> torch.Tensor:
        inputs = self.tokenizer(latex_text, return_tensors="pt", padding=True, truncation=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # 平均プーリングにより文ベクトルを作成
        token_embeddings = outputs.last_hidden_state  # (batch_size, seq_len, hidden_dim)
        attention_mask = inputs["attention_mask"].unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * attention_mask, dim=1)
        sum_mask = torch.clamp(attention_mask.sum(dim=1), min=1e-9)
        return sum_embeddings / sum_mask

# 使用例
if __name__ == "__main__":
    vectorizer = LatexVectorizer()
    latex_doc = r"""
        Let $f(x) = x^2 + 3x + 2$. Then $f'(x) = 2x + 3$.
    """
    vector = vectorizer.vectorize(latex_doc)
    print(vector.shape)
    print(vector)
