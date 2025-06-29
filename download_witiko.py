# Load model directly
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("witiko/mathberta")
model = AutoModelForMaskedLM.from_pretrained("witiko/mathberta")
