import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime
import time


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record,
                                                    message_dict)
        if not log_record.get("timestamp"):
            now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logHandler = logging.StreamHandler()
formatter = CustomJsonFormatter("%(timestamp)s %(level)s %(name)s %(message)s")
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

while True:
    logger.debug("Request made.", extra={"key": "value", "num": 12})
    time.sleep(1)
    logger.info("A user has logged in.", extra={"username": "testuser"})
    time.sleep(1)
    logger.warning("Low disk space.", extra={"size": 25})
    time.sleep(1)
    logger.error("Error connecting to database.", extra={"dbname": "maindb"})
    time.sleep(1)
    logger.critical("Application crashed.", extra={"code": 12345})
    time.sleep(1)
