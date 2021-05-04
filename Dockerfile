FROM python:3.8-slim-buster

WORKDIR /app

# Copy current directory to container
COPY . .

# create a virtual environment & install dependencies
RUN python3 -m venv /.venv
RUN /.venv/bin/pip install -r requirements.txt

# Run gunicorn
CMD ["/.venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "stocksproject.wsgi"]
