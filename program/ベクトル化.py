import requests
import numpy as np
from typing import List

class MathBERTaVectorizerAPI:
    def __init__(self, api_token: str, model_name: str = "witiko/mathberta"):
        self.api_token = api_token
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

    def vectorize(self, latex_text: str) -> np.ndarray:
        response = requests.post(self.api_url, headers=self.headers, json={"inputs": latex_text})

        if response.status_code != 200:
            raise RuntimeError(f"API request failed: {response.status_code} - {response.text}")

        features = response.json()
        # トークンごとのベクトルの平均を文ベクトルとする
        return np.mean(np.array(features), axis=0)

# 使用例
if __name__ == "__main__":
    import os
    HF_API_TOKEN = "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"  # 環境変数にトークンを設定しておく

    if HF_API_TOKEN is None:
        raise ValueError("Hugging Face API トークンが設定されていません。環境変数 HF_API_TOKEN を指定してください。")

    vectorizer = MathBERTaVectorizerAPI(api_token=HF_API_TOKEN)
    latex_input = r"Let $f(x) = x^2 + 3x + 2$. Then $f'(x) = 2x + 3$."
    vec = vectorizer.vectorize(latex_input)

    print("ベクトルの次元:", vec.shape)
    print("ベクトルの内容（一部）:", vec[:10])
