# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the Kaggle API token
COPY kaggle.json /root/.kaggle/kaggle.json

# Set permissions for the Kaggle API token
RUN chmod 600 /root/.kaggle/kaggle.json

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pandas sqlalchemy psycopg2-binary kaggle
RUN pip install kaggle

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Add HEALTHCHECK directive to wait for the database to be ready
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=5 CMD python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(('db', 5432))"

# Run the application
CMD ["python", "data_pipeline.py"]








