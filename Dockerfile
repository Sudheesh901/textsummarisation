FROM python:3.10-slim

# Prevent parallelism issues in tokenizers
ENV TOKENIZERS_PARALLELISM=false

# Set working directory
WORKDIR /app

# Install system dependencies (optional but recommended)
RUN apt update -y && apt install -y git

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8080

# Run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
