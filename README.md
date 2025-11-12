#Text-Summarisation-Project

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
| **boto3** | Integrates with AWS S3 for storing and retrieving models/data (optional). |
| **notebook** | Used for experimentation and interactive model testing in Jupyter. |

# These libraries together enable a full ML pipeline — from dataset preparation and model training to evaluation and cloud-ready deployment.