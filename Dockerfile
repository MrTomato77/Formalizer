# Use the official Streamlit base image
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y xclip && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the Streamlit app
CMD ["streamlit", "run", "your_app.py"]
