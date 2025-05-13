# Use python version 3.13
FROM python:3.13-slim 

# Set the working directory to /app inside the container. This will generate a working directory "app".
WORKDIR /docker_app

# Copy your requirements (into WORKDIR) 
COPY requirements.txt .

# Install the dependencies (--no-cache-dir ensures that it does not use any preinstalled cached packages).
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the necessary app files into /docker_app. Make sure you preserve the structure of youf file system.
COPY run.py .
COPY app ./app

EXPOSE 5000

# Run the app
CMD ["python", "run.py"]