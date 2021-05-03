FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN python3 -m venv /.venv
RUN /.venv/bin/pip install -e .


CMD ["/.venv/bin/gunicorn", "--bind", "0.0.0.0:5000", "stocksproject:create_app()"]
