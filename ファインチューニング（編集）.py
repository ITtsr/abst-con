
import openai
import os

os.environ["OPENAI_API_KEY"]=api_key="ここにAPIキーなど"
cilent=openai.OpenAI()






with open(r"C:\\Users\\kinuy\\Downloads\\training_data_utf8.jsonl", "rb") as f:
    train_file = cilent.files.create(
        file=f,
        purpose="fine-tune"
    )
    
job = cilent.fine_tuning.jobs.create(
    training_file = train_file.id, model = "gpt-3.5-turbo"
)

from datetime import datetime

finetune_deta = cilent.fine_tuning.jobs.list().data
print(finetune_deta)


