# Stocks


## Overview
This is a very simple django website that displays 10 chosen stocks. This project uses the [Finnhub API](https://finnhub.io) to get the current prices for each stock. [Live View](https://lit-sea-51914.herokuapp.com/)

## Diagram
## Setup

In order to run this project, you need a [Finnhub](https://finnhub.io) API key.
Once you have an API key:
- Create a `.env ` file
- `API_KEY=<YOUR API KEY>`

### Run Locally

Create virtualenv and activate it

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Dependencies
```bash
pip install -r requirements.txt
```

Launch Server (Default is localhost:8000)
```bash
gunicorn stocksproject.wsgi
```

### Run with Docker

To run the app in a docker container:
```bash
$ docker-compose up
```

### Heroku
This project supports Heroku

## Technologies Used

- [Django](https://www.djangoproject.com)
- [Docker](https://www.docker.com)
- [Heroku](https://www.heroku.com)
- [Finnhub Python](https://github.com/Finnhub-Stock-API/finnhub-python)

## Background
Resources used to get this up and running:
- [Heroku Tutorial](https://devcenter.heroku.com/articles/getting-started-with-python)
- [Django STATIC_ROOT issue](https://dev.to/developerroad/tutorial-deploying-a-django-app-on-heroku-4k6o)
- [docker-compose](https://docs.docker.com/compose/gettingstarted/)
- [Finnhub Documentation](https://finnhub.io/docs/api/quote)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

Robert Rabinovich & Francis Severino
