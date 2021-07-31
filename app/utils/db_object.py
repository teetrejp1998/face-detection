from utils.const import DB_URL, TESTING,TEST_DB_URL,IS_PRODUCTION,DB_URL_PRODUCTION
from databases import Database

if TESTING:
    db=Database(TEST_DB_URL)
elif IS_PRODUCTION:
    db = Database(DB_URL_PRODUCTION)
else:
    db=Database(DB_URL)