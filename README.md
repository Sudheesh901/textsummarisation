# End-To-End Text-Summarisation-Project

##Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update configuration manger in src/textSummarizer config
5. Update components
6. Update pipeline
7. Update main.py
8. app.py

### 🧠 Tech Stack & Libraries Used

| Library | Purpose / Significance |
|----------|------------------------|
| **transformers[sentencepiece]** | Leverages pretrained NLP models (T5, BART, Pegasus) and SentencePiece tokenizer for text tokenization. |
| **datasets** | Efficiently loads and preprocesses large text datasets via Hugging Face’s Dataset API. |
| **torch** | Deep learning framework used to train and fine-tune the summarization model. |
| **pandas** | Data manipulation and CSV handling for dataset preparation and output formatting. |
| **nltk** | Sentence tokenization, stopwords, and text preprocessing utilities. |
| **tqdm** | Adds progress bars for long-running training and preprocessing loops. |
| **PyYAML** | Loads configuration files (model params, paths, etc.). |
| **matplotlib** | Visualization of training metrics and evaluation results. |
| **sacrebleu** | Evaluates summarization quality using BLEU scores. |
| **rouge_score** | Evaluates summarization quality using ROUGE precision/recall/f1 metrics. |
| **python-box** | Converts YAML/JSON configs into dot-accessible Python objects for clean code. |
| **fastapi** | Serves the trained model as a REST API endpoint. |
| **uvicorn** | Lightweight ASGI server to run the FastAPI app efficiently. |
| **boto3** | Integrates with AWS S3 for storing and retrieving models/data (git). |
| **notebook** | Used for experimentation and interactive model testing in Jupyter. |

### These libraries together enable a full ML pipeline — from dataset preparation and model training to evaluation and cloud-ready deployment.


# we've taken HuggingFace transformer (Seq2Seq) Pegasus and trained it with dataset in Google Collab