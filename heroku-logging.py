import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime
import time


class JsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(JsonFormatter, self).add_fields(log_record, record,
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
formatter = JsonFormatter("%(timestamp)s %(level)s %(name)s %(message)s")
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


number = 0


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


while True:
    level = number % 4
    if level == 0:
        logger.info("New number", extra={"Number": number})
    elif level == 1:
        logger.debug("New number", extra={"Number": number})
    elif level == 2:
        logger.error("New number", extra={"Number": number})

    time.sleep(1)
    if number == 7:
        logger.debug("Lucky number 7", extra={"Number": number})
        time.sleep(1)
    elif is_prime(number):
        logger.critical("Prime found!", extra={"Prime Number": number})
        time.sleep(1)
    number += 1
