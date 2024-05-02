# Pull official base image
FROM python:3.11-slim

# Set work directory
WORKDIR /backend

# Copy Dependencies
COPY ./pyproject.toml ./poetry.lock /backend/

# Running bash commands / Installing dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copying the rest of the app
COPY . /backend/

# Run at port 8000
EXPOSE 8000

# Run the app
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

# Commands to build and run the Docker image
# docker build -t backend .
# docker run -p 8000:8000 -d backend