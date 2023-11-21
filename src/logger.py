import logging


def setup_logging():
    logger = logging.getLogger(__name__)

    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('../data/log_file.log')

    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    logger.setLevel(logging.DEBUG)

    return logger
