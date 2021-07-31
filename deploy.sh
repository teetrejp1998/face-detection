#!/bin/bash
ssh root@188.166.178.217 'rm -r ~/face-detection/face-detection'
scp -r ../face-detection root@188.166.178.217:~/face-detection

ssh root@188.166.178.217 'docker stop faceapi'
ssh root@188.166.178.217 'docker rm faceapi'

ssh root@188.166.178.217 'docker build -t faceapi ~/face-detection/face-detection'
ssh root@188.166.178.217 'docker run -idt -e MODULE_NAME="run" -e PORT="3000" -e PRODUCTION=true -p 3000:3000 --name=faceapi faceapi'