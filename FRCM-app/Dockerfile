# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Set environment variables to ensure a consistent Python environment.
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr
# PYTHONFAULTHANDLER: Dump the Python traceback on crash
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry:
    POETRY_VERSION=1.1.12 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Add Poetry to PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python3 -

# Copy only requirements to cache them in docker layer
WORKDIR $PYSETUP_PATH
COPY ./FRCM-app/pyproject.toml ./FRCM-app/poetry.lock ./

# Project initialization:
# Install runtime dependencies using poetry.
RUN poetry install --no-dev
RUN ls -la

# Copy project files into the docker image
WORKDIR /app
COPY . /app

# Run the application on port 8000 using Uvicorn
CMD ["uvicorn", "FRCM.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
