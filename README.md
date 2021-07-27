# Backend for Simple Face Detection Challenges

Select a task from Task#1 or Task#2. 

## Task#1 Simple Backend for Simple Face Detection

#### Requirements
We have face detection engine which consume webcam image from localhost.
However, we need to run engine in the high performance server. 

1. Such that, you must create a client which consume webcam and send data over HTTP to the engine that also consume data using HTTP server.

2. We should deploy (run) the API, Queue (not required), and Worker in different hosts.
   
3. You may use any backend framework.

4. You may use any queue (**not required**).

#### Extra points
We don't required these, but you may show your skills in these ways:
- clean and readable code
- good object oriented style
- apply HTTPS instead of HTTP
- any new technology
- message queue (**not required**)

## Task#2 Scalable Backend for Simple Face Detection

#### Requirements
1. Create an API as task#1 described, but it should received data in the json format and push data into a queue (**required**).

2. Create a worker that consume data from the queue (**required**).

3. We should start new workers (image consumer tasks) as many as need.

4. Store the result in a database.

#### Extra points
We don't required these, but you may show your skills in these ways:
- clean and readable code
- good object oriented style
- apply HTTPS instead of HTTP
- any new technology
- save the result in an object storage

## ============
## Installation
run these command to install this project.

### 1. Clone repo
```bash
git clone https://github.com/ratthapon/face-detection
```

### 2. Setup virtual environment
```bash
python3 -m venv venv
```

### 3. Install dependencies
```bash
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Deployment


### 1. Load installed dependencies
```bash
source venv/bin/activate
```

### 2. Start engine in a terminal manner 
```bash
python3 face_detection_engine.py
```
