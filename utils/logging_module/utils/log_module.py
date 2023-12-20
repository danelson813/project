import logging
import colorlog

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handle = logging.StreamHandler()
handle.setLevel(logging.DEBUG)
fmt = colorlog.ColoredFormatter(
    "%(name)s: %(white)s%(asctime)s%(reset)s %(log_color)s%(levelname)s%(reset)s %(process)d >>> %(log_color)s%(message)s%(reset)s")
handle.setFormatter(fmt)
logger.addHandler(handle)

file_handler = logging.FileHandler("data/info.log")
file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(fmt)
file_handler.setFormatter(logging.Formatter("%(asctime)s | %(pathname)s - %(lineno)d | %(levelname)s: %(message)s"))
logger.addHandler(file_handler)

logger.info('Logging has been started')
