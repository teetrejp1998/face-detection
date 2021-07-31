from datetime import datetime
from os import getenv

JWT_SECRET_KEY = "1520125a46591e031d29c744f6d0091924530bc06c1081de530ff5659999db67"
JWT_ALGORITH = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 60 * 24 * 5

TOKEN_DESC = "It checks username and password if they are true, it return JWT token to you"
TOKEN_SUMMARY = "It return JWT token"

DB_USER = "admin"
DB_HOST_PRODUCTION = "10.104.0.4"
DB_PASSWORD = "admin"
DB_NAME = "face"
DB_HOST = "167.71.212.119"
DB_URL = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
DB_URL_PRODUCTION = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST_PRODUCTION}/{DB_NAME}"

TESTING = False
IS_PRODUCTION = True if getenv("PRODUCTION")=='true' else False

TEST_DB_USER = "testface"
TEST_DB_PASSWORD = "testface"
TEST_DB_NAME = "testface"
TEST_DB_HOST = "localhost"
TEST_DB_URL = f"postgres://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}/{TEST_DB_NAME}"

NOW = datetime.now()

DATE_TIME= NOW.strftime("%m-%d-%Y_%H:%M:%S")
IMAGE_PATH = f"images/{DATE_TIME}_detected_face.png"

REDIS_URL = f"redis://{DB_HOST}"
TEST_REDIS_URL = f"redis://{TEST_DB_HOST}"
REDIS_URL_PRODUCTION = f"redis://{DB_HOST_PRODUCTION}"

SERVER_DEPLOY_IP = "188.166.178.217"