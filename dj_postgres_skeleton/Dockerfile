FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/code

COPY pyproject.toml ./
COPY poetry.lock ./

RUN pip3 install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install