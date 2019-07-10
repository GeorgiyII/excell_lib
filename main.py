import logging

from table_executor import start
from configs import Config


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(module)-12s %(funcName)-12s %(message)s',
    datefmt='%m-%d %H:%M'
)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)


config = Config

if __name__ == '__main__':
    start(config)
