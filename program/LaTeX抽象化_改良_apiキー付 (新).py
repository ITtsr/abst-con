import openai

# 環境変数からAPIキーを取得
# セキュリティ上、APIキーは直接記述せず、環境変数で管理してください。（実際のプログラム）
openai.api_key = "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"

def summarize_with_chatgpt(text):
    """
    入力された文章をChatGPTを利用して要約する関数。
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # 使用するモデル（例: gpt-4 または gpt-3.5-turbo）
            messages=[
                {
                    "role": "user",
                    "content": f"""次の文章を以下の例に沿って抽象化してください
# 例1:
\\documentclass{{article}}
\\usepackage{{amsmath}}

\\begin{{document}}

$\\triangle ABD$と$\\triangle ACE$において、
仮定より
\\[
AB = AC \\quad \\cdots (1)
\\]
\\[
DA = EA \\quad \\cdots (2)
\\]
また、
\\[
\\angle DAB = \\angle CAB - \\angle CAD = 60^\\circ - \\angle CAD \\quad \\cdots (3)
\\]
\\[
\\angle EAC = \\angle EAD - \\angle CAD = 60^\\circ - \\angle CAD \\quad \\cdots (4)
\\]
より、
\\[
\\angle DAB = \\angle EAC \\quad \\cdots (5)
\\]
(1), (2), (5)より、2辺とその間の角がそれぞれ等しいので
\\[
\\triangle ABD \\equiv \\triangle ACE
\\]
\\end{{document}}

# 出力例1:
ある図形の性質から、特定の辺の長さに関する関係が成り立つ。
ある図形の性質から、一定の角に関する関係が成り立つ。
よって、二つの図形AとBの間には特定の関係が成り立つ。

# 例2:
\\documentclass{{article}}
\\usepackage{{amsmath}}
\\begin{{document}}
\\begin{{enumerate}}
\\item
ベクトル $\\vec{{p}} = (a, b), \\vec{{q}} = (x, y)$ のなす角を $\\theta$ とおく。内積の定義により、
\\[
\\vec{{p}} \\cdot \\vec{{q}} = |\\vec{{p}}||\\vec{{q}}| \\cos\\theta \\leq |\\vec{{p}}||\\vec{{q}}|
\\] 
よって
\\[ ax + by \\leq \\sqrt{{a^2 + b^2}} \\sqrt{{x^2 + y^2}} \\quad \\cdots [1] \\] が成り立つから、両辺を2乗すると
\\[
(ax + by)^2 \leq (a^2 + b^2)(x^2 + y^2) 
\\]
が得られる。
\\item
\\[
a^2 + b^2 = c^2 
\\] 
つまり 
\\[
\sqrt{{a^2 + b^2}} = c 
\\] 
のとき、[1] において $x, y$ をそれぞれ $\\sqrt{{x}}, \\sqrt{{y}}$ に置き換えると、
\\[
a\\sqrt{{x}} + b\\sqrt{{y}} \\leq \\sqrt{{a^2 + b^2}} \\sqrt{{(\\sqrt{{x}})^2 + (\\sqrt{{y}})^2}}
\\]
\\[
= c\\sqrt{{x+y}}
\\] が得られる。
\\end{{enumerate}} 
\\end{{document}} 

# 出力例2:
(1)ある概念の定義式に対する公式、不等式の性質による式変形によってある不等式は成り立つ。  

(2)定数の必要十分条件によって不等式Aを変形すると、不等式Bが成り立つ。


対象の文章:
{text}
"""
                }
            ],#例3を追加する可能性
            max_tokens=150,  # 要約の長さを制御
            temperature=0.2  # 出力のランダム性を調整
        )
        summary = response['choices'][0]['message']['content']
        return summary.strip()
    except Exception as e:
        return f"エラーが発生しました: {e}"

def main():
    print("要約したい文章を入力してください（終了するには'quit'と入力）：")
    while True:
        text = input("入力: ")

        if text.lower() == 'quit':
            print("プログラムを終了します。")
            break

        # 要約の実行
        summary = summarize_with_chatgpt(text)
        print("要約結果:", summary)

if __name__ == "__main__":
    main()