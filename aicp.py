import transformers
from transformers import BertTokenizer, DataCollatorWithPadding
from transformers import AutoModelForSequenceClassification
tokenizer = BertTokenizer.from_pretrained('huolongguo10/check_sec')
model = AutoModelForSequenceClassification.from_pretrained('huolongguo10/check_sec', num_labels=2)
import torch
def check(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    print(f'{logits.argmax().item()}:{text}')
    return 'secure' if predicted_class_id==0 else 'insecure'
