FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN python3 -m venv /.venv
RUN /.venv/bin/pip install -r requirements.txt

WORKDIR /app/stocksproject

CMD ["/.venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "stocksproject.wsgi"]
