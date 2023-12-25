# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory to /app
WORKDIR /blockmatics

# Copy the contents of /Users/bill/blockmatics into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r ./requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8501

# Run your Python script when the container launches
CMD ["streamlit", "run",  "/app/nodestream.py"]
