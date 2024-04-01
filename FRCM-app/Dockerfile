# Pull official base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1s

# Set work directory
WORKDIR /backend

# Copy Dependencies
COPY ./pyproject.toml ./poetry.lock /backend/

# Running bash commands / Installing dependencies
RUN pip install pipx
RUN pipx install poetry
RUN /root/.local/bin/poetry install

# COpying the rest of the app
COPY . /backend/



# Run at port 8000
EXPOSE 8000

# Run the app
CMD ["/root/.local/bin/poetry", "run", "python", "manage.py", "runserver", "8000"]



# Commands to build and run the Docker image
# docker build -t backend .
# docker run -p 8000:8000 -d backend