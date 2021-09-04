import asyncio
from commons.logger import get_logger

log = get_logger('mail.py')

def delegate(msg:str):
    log.debug(msg)
    message = parse(msg)
    log.debug(message)
    return message

def parse(message:str):
    log.debug(message)
    return message
