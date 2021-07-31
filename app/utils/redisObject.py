import aioredis
from utils.const import REDIS_URL,TEST_REDIS_URL,TESTING

redis = None
async def check_test_redis():
    global redis
    if TESTING:
        redis = await aioredis.create_redis_pool(TEST_REDIS_URL)

