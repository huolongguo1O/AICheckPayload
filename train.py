# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-04-30T09:59:54.109952Z","iopub.execute_input":"2023-04-30T09:59:54.110346Z","iopub.status.idle":"2023-04-30T10:00:23.133448Z","shell.execute_reply.started":"2023-04-30T09:59:54.110312Z","shell.execute_reply":"2023-04-30T10:00:23.132423Z"}}
from datasets import load_dataset
from transformers import BertTokenizer, DataCollatorWithPadding

raw_datasets = load_dataset("huolongguo10/insecure")
checkpoint = "prajjwal1/bert-mini"
tokenizer = BertTokenizer.from_pretrained(checkpoint)


def tokenize_function(example):
    return tokenizer(example["sentence1"], max_length=512, truncation=True)


tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-04-30T10:00:26.922238Z","iopub.execute_input":"2023-04-30T10:00:26.922631Z","iopub.status.idle":"2023-04-30T10:00:27.019214Z","shell.execute_reply.started":"2023-04-30T10:00:26.922589Z","shell.execute_reply":"2023-04-30T10:00:27.018201Z"}}
from transformers import TrainingArguments

training_args = TrainingArguments("trainer-cs-tiny",save_strategy="epoch")

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-04-30T10:00:29.512010Z","iopub.execute_input":"2023-04-30T10:00:29.512474Z","iopub.status.idle":"2023-04-30T10:00:31.366712Z","shell.execute_reply.started":"2023-04-30T10:00:29.512433Z","shell.execute_reply":"2023-04-30T10:00:31.365671Z"}}
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-04-30T10:00:45.438170Z","iopub.execute_input":"2023-04-30T10:00:45.438977Z","iopub.status.idle":"2023-04-30T10:05:09.730326Z","shell.execute_reply.started":"2023-04-30T10:00:45.438915Z","shell.execute_reply":"2023-04-30T10:05:09.729087Z"}}
trainer.train()

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-04-30T10:00:36.769254Z","iopub.execute_input":"2023-04-30T10:00:36.770348Z","iopub.status.idle":"2023-04-30T10:00:41.289265Z","shell.execute_reply.started":"2023-04-30T10:00:36.770305Z","shell.execute_reply":"2023-04-30T10:00:41.288186Z"}}
from transformers import Trainer

trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets["train"],
    data_collator=data_collator,
    tokenizer=tokenizer,
)



