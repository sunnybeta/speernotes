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

If the above `pip` installation fails, due to `psyopg2` missing, you will need the `lib-pq` library instead.

I will try to add a docker `compose.yml` file as soon as possible.

### Tests

```bash
# With the virtual environment activated, run:
# source .venv/bin/activate
pytest -v
```

![PyTestSS](/images/tests.png)

## License

![MIT](LICENSE)
