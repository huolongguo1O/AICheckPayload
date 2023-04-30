import gradio as gr
import transformers
from transformers import BertTokenizer, DataCollatorWithPadding
from transformers import AutoModelForSequenceClassification
tokenizer = BertTokenizer.from_pretrained('huolongguo10/check_sec')
model = AutoModelForSequenceClassification.from_pretrained('huolongguo10/check_sec', num_labels=2)
_tokenizer = BertTokenizer.from_pretrained('huolongguo10/check_sec_tiny')
_model = AutoModelForSequenceClassification.from_pretrained('huolongguo10/check_sec_tiny', num_labels=2)
import torch
def check_each(text):
    inputs = tokenizer(text, return_tensors="pt",max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    print(f'{logits.argmax().item()}:{text}')
    return 'secure' if predicted_class_id==0 else 'insecure'
def _check_each(text):
    inputs = _tokenizer(text, return_tensors="pt",max_length=512)
    with torch.no_grad():
        logits = _model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    print(f'{logits.argmax().item()}:{text}')
    return 'secure' if predicted_class_id==0 else 'insecure'
def _check(text):
    t=text
    while len(t)>512:
        t=t[0:511]
        if check_each(t)=='insecure':
            return 'insecure'
    return check_each(t)
def _check_tiny(text):
    t=text
    while len(t)>512:
        t=t[0:511]
        if _check_each(t)=='insecure':
            return 'insecure'
    return _check_each(t)
def check(text):
    return _check(text),_check_tiny(text)
with gr.Blocks() as demo:
    text = gr.Textbox(label="Text")
    output = gr.Textbox(label="Output Box")
    _output = gr.Textbox(label="Output Box(By Tiny)")
    # org = gr.Textbox(label="By normal check")
    greet_btn = gr.Button("Check!")
    greet_btn.click(fn=check, inputs=text, outputs=[output,_output], api_name="check")
    gr.Markdown('''# check_sec
检查web参数安全性，支持多种payload(v0.0.3)
## 类型
```
LABEL_0: secure
LABEL_1: insecure(可能包含payload)
```
    ''')
# gr.Interface.load("models/huolongguo10/check_sec").launch()

demo.launch()
