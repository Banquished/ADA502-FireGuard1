# Pull official base image
FROM python:3.11-alpine

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1s

# Copy Project
COPY /Frontend-app/API /app/API
COPY /Frontend-app/frontend /app/frontend
COPY /Frontend-app/db.sqlite3 /app/
COPY /Frontend-app/manage.py /app/
COPY /Frontend-app/pyproject.toml /app/
COPY /Frontend-app/poetry.lock /app/

# Running bash commands
RUN pip install pipx
RUN pipx install poetry
RUN /root/.local/bin/poetry install


# Run at port 8000
EXPOSE 8000

# Run the app
CMD ["/root/.local/bin/poetry", "run", "python", "manage.py", "runserver", "8000"]