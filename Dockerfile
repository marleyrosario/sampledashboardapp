# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Update the package list and install sudo
RUN apt-get update && apt-get install -y sudo

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p ~/.streamlit

RUN echo "\
[general]\n\
email = \"marleymrosario@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

RUN echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
port = 80\n\
[browser]\n\
gatherUsageStats = false\n\
" > ~/.streamlit/config.toml

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python


# Make port 80 available to the world outside this container
EXPOSE 80

# Run trends_app.py when the container launches
CMD ["streamlit", "run", "trends_app.py"]