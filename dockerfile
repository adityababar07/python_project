# Dockerfile

# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/class_12/python_project/
RUN pip3 install pipenv && pipenv install --system

# Copy project
COPY . /code/class_12/python_project/