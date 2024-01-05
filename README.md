# Speer Notes

*A simple notes backend for Speer Technologies*

## Getting Started

```bash
git clone https://github.com/sunnybeta/speernotes
cd speernotes
```

### Local Setup

```bash
# DataBase
cd db
docker build -t speer-db:latest . 
docker run -d -e POSTGRES_PASSWORD=password --name speer-db -p 5432:5432 speer-db
```

```bash
# API
cd api
python -m venv .venv # choose your appropriate python path
source .venv/bin/activate # instead of bin its Scripts on windows/
pip install --upgrade pip
pip install -r requirements.txt
```

If the above `pip` installation fails, due to `psycopg2` missing, you will probably need the `libpq` library.

I will try to add a docker `compose.yml` file as soon as possible.

### Tests

```bash
# With the virtual environment activated, run:
# source .venv/bin/activate
pytest -v
```

![PyTestSS](/images/tests.png)

## Tech Stack

* Back End: **FastAPI** It's quite easy to get q protoype up and running in Python. As I started the task really late, I believe it was a good choice. Alternate choice would have been Go.

* Database: **PostgreSQL** I chose PostgerSQL as we had a single service which handles user creation, authentication and notes creation. It is easy to have relations among these entities and retrieve the required data.

* Containerization: **Docker**

* Front End: Would I will continue working on this and woudl go with Next.

## License

![MIT](LICENSE)
