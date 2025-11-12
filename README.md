#開発手順 

1. クローンする 

まずGitHub上のレポジトリをローカルに持ってきます。 

git clone https://github.com/ユーザー名/リポジトリ名.git 

cd リポジトリ名 



2. ブランチを作成（推奨） 

直接 main や master に触るよりも、新しいブランチを切って作業した方が安全です。 

git checkout -b feature/修正内容 

※修正内容は任意 



3. ファイルを変更 

エディタなどでコードやドキュメントを編集します。 

 

2. 仮想環境を作成 

Pythonの標準モジュール venv を使うのが一般的です。 

python -m venv .venv 

.venv は仮想環境用のディレクトリ名（任意） 

プロジェクトごとに作るのがベスト 


3. 仮想環境をアクティベート 

OSによってコマンドが少し違います。 

Windows (PowerShell の場合) 

.venv\Scripts\Activate.ps1 

Windows (cmd.exe の場合) 

.venv\Scripts\activate.bat 

アクティベートされると、コマンドラインの先頭に (.venv) のように表示されます。 



4. requirements.txt をインストール 

pip install -r requirements.txt 
