# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the port
EXPOSE 81

# Run the service
CMD ["uvicorn", "cache:app", "--host", "0.0.0.0", "--port", "85"]
