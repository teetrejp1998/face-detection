from socket import socket,AF_INET,SOCK_STREAM,gethostname,gethostbyname
import threading
# from utils.const import SERVER_DEPLOY_IP

PORT = 3000
SERVER = gethostbyname(gethostname())
ADDR = (SERVER,PORT)


s = socket(AF_INET,SOCK_STREAM)
deviceRTSP = ""


