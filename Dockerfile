# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy current project files to container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask requests twilio

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
