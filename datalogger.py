import logging


logname = "data"


def _create_logger(filename: str) -> None:
    # create logger
    logger = logging.getLogger(logname)

    # create console handler and set level to debug
    # https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler
    filehandler = logging.FileHandler(filename=filename, mode="w")

    # add ch to logger
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)


def createDataLogger() -> None:
    _create_logger("./output/data_logs.txt")


createDataLogger()


def write_log(data: dict) -> None:
    # create logger
    logger = logging.getLogger(logname)

    logger.info(str(data))