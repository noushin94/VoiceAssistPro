# Use the official Python image with Python 3.8
FROM python:3.8-slim-buster

# Set environment variables to prevent Python from buffering stdout and stdin
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libsndfile1-dev \
    portaudio19-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and source code into the container
COPY requirements.txt .
COPY src/ ./src/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download necessary NLTK data
RUN python -m nltk.downloader punkt stopwords

# Download SpaCy language model
RUN python -m spacy download en_core_web_sm

# Expose any necessary ports (optional)
# EXPOSE 5000

# Set the entry point to the application
CMD ["python", "src/main.py"]
