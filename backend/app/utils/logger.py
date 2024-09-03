import logging
from fastapi.logger import logger


uvicorn_logger = logging.getLogger('uvicorn')
logger.handlers = uvicorn_logger.handlers
logger.setLevel(logging.DEBUG)
