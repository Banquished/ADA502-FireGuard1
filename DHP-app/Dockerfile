# Pull official base image
FROM python:3.11-alpine

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1s

# Copy Project
COPY /DHP-app/DHP/ /app/DHP/
COPY /DHP-app/db.sqlite3 /app/
COPY /DHP-app/manage.py /app/
COPY /DHP-app/pyproject.toml /app/
COPY /DHP-app/poetry.lock /app/

# Running bash commands
RUN pip install pipx
RUN pipx install poetry
RUN /root/.local/bin/poetry install


# Run at port 8000
EXPOSE 8000

# Run the app
CMD ["/root/.local/bin/poetry", "run", "python", "manage.py", "runserver", "8000"]