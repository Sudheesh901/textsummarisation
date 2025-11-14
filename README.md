# End-To-End Text-Summarisation-Project 

# model  T5-small (text-to-text transformer)

## Workflows

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




## 3. Deployment:

    - AWS ECR: 782198887741.dkr.ecr.us-east-1.amazonaws.com/texts

### These libraries together enable a full ML pipeline — from dataset preparation and model training to evaluation and cloud-ready deployment.

## 🔄 Model Update: Migration from Pegasus to T5-small

This project originally experimented with the **Pegasus (google/pegasus-cnn_dailymail)** model inside Google Colab.  
Pegasus is a high-performance abstractive summarization model designed specifically for long-form text summarization.

However, during End-to-End pipeline development on a **local CPU environment**, Pegasus became impractical due to its size and heavy GPU requirements. This led to Continuous Out-Of-Memory (OOM) errors, kernel crashes, and extremely slow training.

To make the pipeline lightweight, stable, and deployment-friendly, the project was migrated to **T5-small**, a compact text-to-text model.

---

## ✔ Why T5-small Was Chosen

T5-small contains only **60M parameters**, making it efficient for:
- Local CPU training  
- Fast iteration  
- Low-resource deployment  
- MLOps pipeline demonstrations  

Even though it is smaller than Pegasus, T5-small still performs well for dialogue/news summarization tasks.

---

## 🔍 Differences Between Pegasus and T5-small

### **Model Comparison Table**

| Feature | Pegasus (cnn_dailymail) | T5-small |
|--------|--------------------------|----------|
| Model Type | Seq2Seq (summarization-specialized) | Seq2Seq (general text-to-text) |
| Parameters | ~568M | ~60M |
| Summarization Quality | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐☆ |
| Speed | Slow | Fast |
| Hardware Needs | Requires GPU | CPU-friendly |
| Input Format | Plain text | Requires prefix: `summarize: <text>` |
| Training Cost | High | Low |
| Best Use | Research, long summaries, GPU servers | Deployment, CPU training, prototypes |

---

## 📌 When to Use Each Model

### **Use Pegasus if:**
- You need state-of-the-art summarization performance  
- You have access to a powerful GPU  
- You are working with long documents or research-level tasks  

### **Use T5-small if:**
- You are training and deploying on a CPU machine  
- You need a lightweight and fast model  
- You are building an end-to-end MLOps pipeline  
- You want quick experimentation or cost-efficient deployment  

---

## 📘 Final Summary

- The project initially used **Pegasus** for experimentation in Colab.  
- Due to hardware limitations on the local machine, the pipeline was migrated to **T5-small**.  
- T5-small provides a balanced combination of speed, stability, and summarization quality.  
- All components—data transformation, training, evaluation, and deployment—now run using **T5-small** to ensure smooth execution on CPU.
