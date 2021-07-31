FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app






