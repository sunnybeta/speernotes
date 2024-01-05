FROM python:3.12
WORKDIR /app
COPY . .
RUN python -m venv .venv
RUN .venv/bin/pip install --upgrade pip
RUN .venv/bin/pip install -r requirements.txt
EXPOSE 8000
CMD [".venv/bin/uvicorn","app.asgi:app"]
