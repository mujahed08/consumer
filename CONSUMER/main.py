"""
websockets
"""
import websocket
from commons.logger import get_logger
from jobs.mail import delegate

log = get_logger('main.py')

def on_message(app, message):
    log.info(app)
    delegate(message)

wsapp = websocket.WebSocketApp("ws://localhost:8080/ws/broker/main/topic/CONSUMER", on_message=on_message)
wsapp.run_forever()
