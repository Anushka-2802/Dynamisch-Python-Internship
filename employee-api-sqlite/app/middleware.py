import time
from logger import logger

async def log_requests(request, call_next):

    start = time.time()

    response = await call_next(request)

    end = time.time()

    logger.info(
        f"{request.method} {request.url.path} completed in {end-start:.4f} seconds"
    )

    return response