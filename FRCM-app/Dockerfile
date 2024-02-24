# Pull official base image
FROM python:3.11-alpine

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1s

# Copy Project
COPY /FRCM-app/FRCM /app/FRCM
COPY /FRCM-app/db.sqlite3 /app/
COPY /FRCM-app/manage.py /app/
COPY /FRCM-app/pyproject.toml /app/
COPY /FRCM-app/poetry.lock /app/

# Running bash commands
RUN pip install pipx
RUN pipx install poetry
RUN /root/.local/bin/poetry install


# Run at port 8000
EXPOSE 8000

# Run the app
CMD ["/root/.local/bin/poetry", "run", "python", "manage.py", "runserver", "8000"]