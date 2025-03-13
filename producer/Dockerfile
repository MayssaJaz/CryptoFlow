FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Kafka consumer
EXPOSE 9093

# Command to run the application
CMD ["python", "producer.py"]