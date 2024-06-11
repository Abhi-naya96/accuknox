# Use a lightweight base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy Wisecow application code
COPY . .

# Expose port (replace with actual port used by Wisecow)
EXPOSE 8000

# Start Wisecow application (replace with actual command)
CMD [ "python", "wisecow_app.py" ]
