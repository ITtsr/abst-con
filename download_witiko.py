from transformers import AutoTokenizer, AutoModel
model = AutoModel.from_pretrained("witiko/mathberta")
tokenizer = AutoTokenizer.from_pretrained("witiko/mathberta")

model.save_pretrained("mathberta")
tokenizer.save_pretrained("mathberta")
