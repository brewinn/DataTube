# Pull python base image -- there is no official django image
FROM python:3.10

# Setup geckodriver
WORKDIR /usr/local/bin
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
RUN tar -xvf geckodriver-v0.32.0-linux64.tar.gz

# Set the working directory from the django app
WORKDIR /usr/src/app

# Some environmental variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Update and install dependencies
RUN apt update -y && apt upgrade -y 
RUN apt install netcat firefox-esr -y

# Get dependencies
RUN pip install --upgrade pip
COPY datatube/requirements.txt .
RUN pip install -r requirements.txt

# Run entrypoint.sh (checks db is healthy before running migrations)
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
