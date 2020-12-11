import logging
import os

logging.basicConfig(filename="mylog.log", filemode="a",  level=logging.DEBUG, )
a =10
logging.debug(f"a value is {a}")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_name = os.path.join(os.path.dirname(__file__), 'mylog.log')
formatter = logging.Formatter('%(asctime)12s: %(name)s: %(levelname)s: %(message)s')

file_handler = logging.FileHandler(file_name, mode='a')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info("I am doing logging using handler")

