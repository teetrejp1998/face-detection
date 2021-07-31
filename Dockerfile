FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY images/ /app/images
COPY models/ /app/models
COPY routes/ /app/routes
COPY testing/ /app/testing
COPY utils/ /app/utils
COPY conftest.py/ /app
COPY face_detection_engine.py/ /app
COPY haarcascade_frontalface_default.xml/ /app
COPY README.md/ /app
COPY run.py/ /app





