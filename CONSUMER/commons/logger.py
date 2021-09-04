import logging
import logging.config
import yaml

with open('log4py.yaml', 'r') as f:
    CONFIG = yaml.safe_load(f.read())
    logging.config.dictConfig(CONFIG)

def get_logger(logger_name):
    logger_instance = logging.getLogger(logger_name)
    return logger_instance

"""
import asyncio
import websockets
from jobs.mail import delegate
from commons.logger import get_logger

logger = get_logger('main.py')

async def handler(path):
    async with websockets.connect(path) as websocket:
        async for message in websocket:
            await delegate(message)

URI = "ws://localhost:8080/ws/chat/TOPIC/CONSUMER"
asyncio.get_event_loop().run_until_complete(handler(URI))

logger.info('   End of the main file')
"""