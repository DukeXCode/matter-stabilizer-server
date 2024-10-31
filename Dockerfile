# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies (if you have a requirements.txt file)
# Uncomment the following line if you need to install packages
# RUN pip install -r requirements.txt

# Expose the port the server will run on
EXPOSE 2101

# Run the server
CMD ["python", "main.py"]
