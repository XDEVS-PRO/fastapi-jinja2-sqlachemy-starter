FROM python:3.11.0-bullseye

WORKDIR /app

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

#COPY ./pyproject.toml ./poetry.lock* /app/
COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-root

COPY . /app

CMD uvicorn --host 0.0.0.0 --port 8000 main:app
