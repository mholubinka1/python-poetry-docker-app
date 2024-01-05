import logging.config
from logging import Logger, getLogger

from app.common.constants import APP_LOGGER_NAME
from app.common.logging import config

logging.config.dictConfig(config)
logger: Logger = getLogger(APP_LOGGER_NAME)

print("Hello World!.")
