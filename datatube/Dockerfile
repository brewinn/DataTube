# Pull python base image -- there is no official django image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /usr/src/app

# Set the base directory for the datatube directory
#ARG BASE_DIR

# Some environmental variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Update and install dependencies
RUN apt update -y && apt upgrade -y 
RUN apt install netcat -y

# Get dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy Django code
COPY . .

# Run entrypoint.sh (checks db is healthy before running migrations)
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
