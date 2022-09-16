from asyncio.log import logger
import logging

FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
logging.basicConfig(level = logging.DEBUG, format = FORMAT)

logger = logging.getLogger(name='gcba_api')